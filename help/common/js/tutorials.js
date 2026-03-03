// SciX Training Hub — tutorial progress & video management
// Uses the YouTube IFrame Player API for embedded video control.

var STORAGE_KEY = 'scix-training-hub-progress';
var players = {};
var ytApiReady = false;
var pendingInit = null;

// ── Progress tracking ─────────────────────────────────────────────────────────

function getProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  } catch (e) {
    return {};
  }
}

function saveProgress(progress) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {}
}

function updateProgressBar() {
  var rows = document.querySelectorAll('.tutorial-row');
  var total = rows.length;
  if (total === 0) return;

  var progress = getProgress();
  var completed = 0;
  rows.forEach(function (row) {
    if (progress[row.id] === true) completed++;
  });

  var pct = Math.round((completed / total) * 100);

  var bar = document.getElementById('progress-bar');
  var countEl = document.getElementById('completed-count');
  var pctEl = document.getElementById('progress-pct');

  if (bar) {
    bar.style.width = pct + '%';
    bar.setAttribute('aria-valuenow', pct);
  }
  if (countEl) countEl.textContent = completed;
  if (pctEl) pctEl.textContent = pct;
}

function setRowCompleted(tutorialId, isComplete) {
  var row = document.getElementById(tutorialId);
  var indicator = document.getElementById('indicator-' + tutorialId);
  var btn = document.getElementById('btn-' + tutorialId);

  if (!row) return;

  if (isComplete) {
    row.classList.add('completed');
    if (indicator) indicator.classList.add('completed');
    if (btn) {
      btn.classList.add('completed');
      btn.innerHTML = '<i class="fa fa-check-circle"></i> Completed';
    }
  } else {
    row.classList.remove('completed');
    if (indicator) indicator.classList.remove('completed');
    if (btn) {
      btn.classList.remove('completed');
      btn.innerHTML = '<i class="fa fa-check"></i> Mark as Complete';
    }
  }
}

// Called by the "Mark as Complete" button
function toggleComplete(tutorialId) {
  var progress = getProgress();
  progress[tutorialId] = !progress[tutorialId];
  saveProgress(progress);
  setRowCompleted(tutorialId, progress[tutorialId]);
  updateProgressBar();
}

// ── YouTube IFrame API ────────────────────────────────────────────────────────

// Called automatically by YouTube once its API script has loaded.
function onYouTubeIframeAPIReady() {
  ytApiReady = true;
  if (pendingInit) {
    initPlayer(pendingInit.tutorialId, pendingInit.videoId);
    pendingInit = null;
  }
}

function pauseAllPlayers(exceptId) {
  Object.keys(players).forEach(function (id) {
    if (id === exceptId) return;
    try {
      var p = players[id];
      if (p && typeof p.pauseVideo === 'function') {
        p.pauseVideo();
      }
    } catch (e) {}
  });
}

function initPlayer(tutorialId, videoId) {
  // Don't create a second player for the same row
  if (players[tutorialId]) return;

  players[tutorialId] = new YT.Player('player-' + tutorialId, {
    height: '360',
    width: '100%',
    videoId: videoId,
    playerVars: {
      playsinline: 1,
      rel: 0,
      modestbranding: 1
    },
    events: {
      onStateChange: function (event) {
        if (event.data === YT.PlayerState.PLAYING) {
          // Pause every other player
          pauseAllPlayers(tutorialId);
        }
        if (event.data === YT.PlayerState.ENDED) {
          // Auto-mark complete when the video finishes
          var progress = getProgress();
          if (!progress[tutorialId]) {
            progress[tutorialId] = true;
            saveProgress(progress);
            setRowCompleted(tutorialId, true);
            updateProgressBar();
          }
        }
      }
    }
  });
}

// ── Accordion ─────────────────────────────────────────────────────────────────

function toggleTutorial(tutorialId) {
  var row = document.getElementById(tutorialId);
  var body = document.getElementById('body-' + tutorialId);
  if (!row || !body) return;

  var isOpen = body.classList.contains('open');

  // Collapse all rows and pause all players
  document.querySelectorAll('.tutorial-row').forEach(function (r) {
    r.classList.remove('active');
  });
  document.querySelectorAll('.tutorial-body').forEach(function (b) {
    b.classList.remove('open');
  });
  pauseAllPlayers(null);

  if (!isOpen) {
    row.classList.add('active');
    body.classList.add('open');

    var videoId = row.getAttribute('data-video-id');
    if (videoId) {
      if (ytApiReady) {
        initPlayer(tutorialId, videoId);
      } else {
        pendingInit = { tutorialId: tutorialId, videoId: videoId };
      }
    }
  }
}

// ── Initialise on page load ───────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', function () {
  var progress = getProgress();
  document.querySelectorAll('.tutorial-row').forEach(function (row) {
    setRowCompleted(row.id, progress[row.id] === true);
  });
  updateProgressBar();
});
