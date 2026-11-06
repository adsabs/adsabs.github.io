{% comment %}
Outreach collage. SciX only: the materials are SciX branded, so there is no ADS
twin of this page.

The page leads with authorship. Yueyi Che designed every piece shown here, so
her name is the largest type on the page and sits above the artwork.

Layout is deliberately asymmetric. Nothing here is a centred row: the masthead
runs type against a full plate, the cast is two interlocking courses that
overlap, and the printed matter sits on an uneven grid. Captions are labels
only, no prose.

Content lives in _data/outreach.yml, styling in _sass/_outreach.scss.

Display only: no download links, so we never have to make a licensing decision
about redistributing the artwork.
{% endcomment %}
{% assign designer = site.data.outreach.designer %}
{% assign pieces = site.data.outreach.pieces %}
{% assign f = site.data.outreach.figures %}
<div class="outreach-page outreach-page--collage">

  <header class="or-masthead">
    <div class="or-masthead-credit">
      <p class="outreach-eyebrow">Artwork and design</p>
      <h2 class="or-masthead-name" id="outreach-credit-title">
        <a href="{{ site.baseurl }}{{ designer.bio_url }}">{{ designer.name }}</a>
      </h2>
      <div class="or-masthead-who">
        <img class="or-masthead-portrait" src="{{ site.baseurl }}{{ designer.photo }}" alt="{{ designer.photo_alt | escape }}" width="120" height="120">
        <p class="or-masthead-role">
          {{ designer.role }}<br>
          <span>{{ designer.affiliation }}</span>
        </p>
      </div>
      <p class="outreach-credit-links">
        <a class="outreach-viewall" href="{{ site.baseurl }}{{ designer.bio_url }}">Read her bio</a>
        <a class="outreach-viewall" href="{{ site.baseurl }}/scixabout/ambassador/">Meet the ambassadors</a>
      </p>
    </div>
    <figure class="or-masthead-plate">
      <img src="{{ site.baseurl }}{{ f.night.file }}" alt="{{ f.night.alt | escape }}">
      <figcaption>{{ f.night.caption | escape }}</figcaption>
    </figure>
  </header>

  {% comment %}
  The honeycomb. Yueyi's square originals, masked to pointy-top hexagons and
  tessellated 3 / 2 / 3 so the middle course nests in the valleys of the one
  above. No labels: the drawings say which discipline they are.
  {% endcomment %}
  <section class="or-hive" aria-label="The SciX science explorers">
    <ul class="or-hive-row">
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/astro.jpg" alt="An astrophysicist adjusting a telescope under a sky of yellow stars." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/helio.jpg" alt="A heliophysicist in a knitted vest gesturing at a solar flare." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/planetary.jpg" alt="A planetary scientist in a wheelchair reaching towards a large banded planet." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/earth.jpg" alt="An Earth scientist in a field hat holding a rock hammer and a rock sample." loading="lazy"></li>
    </ul>
    <ul class="or-hive-row or-hive-row--offset">
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/ocean.jpg" alt="An ocean scientist diving beside a boulder on the sea floor." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/bio.jpg" alt="An astronaut and a researcher in a pink headscarf working together on a tablet." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/astrobio.jpg" alt="An astrobiologist surrounded by lab glassware, microbes and planets." loading="lazy"></li>
      <li class="or-hex"><img src="{{ site.baseurl }}/help/img/outreach/hex/together.jpg" alt="Five scientists around a table under the words We use SciX for open science." loading="lazy"></li>
    </ul>
  </section>

  {% comment %}
  The zines, as flip books. Each booklet is one folded sheet, and pages 2-3,
  4-5 and 6-7 are facing pages: the lettering runs across those gutters, so
  each spread is cropped whole rather than cut into separate pages. Views are
  built by scripts/build-outreach-assets.py.

  Every view is in the markup and visible by default, so the whole booklet is
  readable with no JavaScript. The script below hides all but one and adds the
  controls.
  {% endcomment %}
  <section class="or-books" aria-label="Zines">
    <figure class="or-book" data-book>
      <figcaption class="or-book-title">Explore Science to the Moon and Back</figcaption>
      <div class="or-book-stage">
        <img class="or-book-page" data-book-page data-book-label="Cover" src="{{ site.baseurl }}/help/img/outreach/zine-1-1.jpg" alt="Cover. Explore Science to the Moon and Back, by SciX Ambassador Yueyi Che. A child holds up a globe against a purple sky." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 2 and 3" src="{{ site.baseurl }}/help/img/outreach/zine-1-2.jpg" alt="An Earth scientist sits on a boulder with her arm raised, and an astrophysicist in a flowered shirt stands by an observatory dome on a mountain peak." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 4 and 5" src="{{ site.baseurl }}/help/img/outreach/zine-1-3.jpg" alt="A heliophysicist works at a laptop beside an enormous sun, and a planetary scientist in a lilac dress holds Mars in her palm." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 6 and 7" src="{{ site.baseurl }}/help/img/outreach/zine-1-4.jpg" alt="A bioastronautic researcher waves from orbit in a white suit, and a child with a tablet is told that she can be a Science Explorer too." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Back cover" src="{{ site.baseurl }}/help/img/outreach/zine-1-5.jpg" alt="Back cover. A QR code, scixplorer.org, and the five curated discipline collections: Earth science, astrophysics, heliophysics, planetary science, and biological and physical science." loading="lazy">
      </div>
      <div class="or-book-nav" hidden data-book-nav>
        <button type="button" class="or-book-btn" data-book-prev>
          <i class="fa fa-chevron-left" aria-hidden="true"></i> Back
        </button>
        <ol class="or-book-pips" data-book-pips></ol>
        <p class="sr-only" role="status" aria-live="polite" data-book-status></p>
        <button type="button" class="or-book-btn" data-book-next>
          Next <i class="fa fa-chevron-right" aria-hidden="true"></i>
        </button>
      </div>
    </figure>
    <figure class="or-book" data-book>
      <figcaption class="or-book-title">Tiny Book of Literature Review</figcaption>
      <div class="or-book-stage">
        <img class="or-book-page" data-book-page data-book-label="Cover" src="{{ site.baseurl }}/help/img/outreach/zine-2-1.jpg" alt="Cover. Tiny Book of Literature Review, by SciX Ambassador Yueyi Che. A student works at a laptop at night." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 2 and 3" src="{{ site.baseurl }}/help/img/outreach/zine-2-2.jpg" alt="Didi introduces herself as a first year PhD student starting her literature search, and shows the author network graph SciX built from her keywords." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 4 and 5" src="{{ site.baseurl }}/help/img/outreach/zine-2-3.jpg" alt="Didi expands her search with the useful, trending, reviews and similar functions, following citations backward and forward from one core paper." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Pages 6 and 7" src="{{ site.baseurl }}/help/img/outreach/zine-2-4.jpg" alt="Didi saves what she finds into a SciX library to share with her group, and sends feedback to the curators." loading="lazy">
        <img class="or-book-page" data-book-page data-book-label="Back cover" src="{{ site.baseurl }}/help/img/outreach/zine-2-5.jpg" alt="Back cover. Try SciX now, with a QR code, scixplorer.org, and the words search knowledge smarter." loading="lazy">
      </div>
      <div class="or-book-nav" hidden data-book-nav>
        <button type="button" class="or-book-btn" data-book-prev>
          <i class="fa fa-chevron-left" aria-hidden="true"></i> Back
        </button>
        <ol class="or-book-pips" data-book-pips></ol>
        <p class="sr-only" role="status" aria-live="polite" data-book-status></p>
        <button type="button" class="or-book-btn" data-book-next>
          Next <i class="fa fa-chevron-right" aria-hidden="true"></i>
        </button>
      </div>
    </figure>
  </section>

  <figure class="or-sheet">
    <img src="{{ site.baseurl }}{{ f.coloring.file }}" alt="{{ f.coloring.alt | escape }}" loading="lazy">
  </figure>

  {% comment %}
  The photographed record: the same materials on the table at real meetings.
  The span classes come from the data, so this grid is already uneven.
  {% endcomment %}
  <section class="outreach-section" aria-labelledby="outreach-gallery-title">
    <div class="outreach-section-head">
      <h2 class="outreach-section-title" id="outreach-gallery-title">On the table</h2>
      <p class="outreach-section-intro">{{ pieces | size }} pieces, photographed at SciX booths and poster sessions between February and May 2026.</p>
    </div>

    <div class="outreach-grid">
      {% for piece in pieces %}
      <figure
        class="outreach-tile outreach-tile--{{ piece.variant }} outreach-span-{{ piece.span }} outreach-tone-{{ piece.tone }}"
        id="outreach-{{ piece.id }}"
      >
        <div class="outreach-tile-media outreach-tile-media--{{ piece.fit }}">
          {% comment %}
          Keep the img on one line and escape the alt text: the descriptions
          quote the sticker captions, and kramdown drops the whole tag if a raw
          double quote lands inside an attribute.
          {% endcomment %}
          <img src="{{ site.baseurl }}{{ piece.image }}" alt="{{ piece.alt | escape }}" loading="lazy">
        </div>

        <figcaption class="outreach-tile-body">
          <p class="outreach-eyebrow">{{ piece.type }}</p>
          <h3 class="outreach-tile-title">{{ piece.title }}</h3>
          <p class="outreach-tile-meta">
            <span class="outreach-meta-venue">{{ piece.venue }}</span>
            <span class="outreach-meta-date">{{ piece.date }}</span>
          </p>
          {% if piece.source_url %}
          <p class="outreach-tile-source">
            <a class="outreach-viewall" href="{{ site.baseurl }}{{ piece.source_url }}">{{ piece.source_label }}</a>
          </p>
          {% endif %}
        </figcaption>
      </figure>
      {% endfor %}
    </div>
  </section>

  <footer class="or-endmark">
    <figure class="or-endmark-crest">
      <img src="{{ site.baseurl }}{{ f.crest.file }}" alt="{{ f.crest.alt | escape }}" loading="lazy">
    </figure>
    <div class="or-endmark-credit">
      <p class="outreach-eyebrow">{{ f.crest.caption | escape }}</p>
      <p class="or-endmark-line">
        Artwork by <a href="{{ site.baseurl }}{{ designer.bio_url }}">{{ designer.name }}</a>, {{ designer.role }}.
      </p>
      <p><a class="outreach-viewall" href="{{ site.baseurl }}/scixblog/">Conference write-ups</a></p>
    </div>
  </footer>
</div>

<script>
  // Flip book. Every page is in the markup and visible without JavaScript, so
  // this only ever hides pages and adds controls: if the script does not run,
  // the booklet still reads top to bottom.
  (function () {
    var books = document.querySelectorAll('[data-book]');

    Array.prototype.forEach.call(books, function (book) {
      var pages = book.querySelectorAll('[data-book-page]');
      var nav = book.querySelector('[data-book-nav]');
      var status = book.querySelector('[data-book-status]');
      var prev = book.querySelector('[data-book-prev]');
      var next = book.querySelector('[data-book-next]');
      if (!pages.length || !nav) return;

      var pips = book.querySelector('[data-book-pips]');
      var at = 0;
      var dots = [];
      book.classList.add('is-paged');
      nav.hidden = false;

      // One dot per view, each a shortcut to that view. The visible label is
      // the dot; the page wording stays in the status region for screen
      // readers, where it is actually useful.
      Array.prototype.forEach.call(pages, function (page, i) {
        var li = document.createElement('li');
        var dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'or-book-pip';
        dot.setAttribute('aria-label', page.getAttribute('data-book-label'));
        dot.addEventListener('click', function () { show(i); });
        li.appendChild(dot);
        pips.appendChild(li);
        dots.push(dot);
      });

      function show(i) {
        at = Math.max(0, Math.min(pages.length - 1, i));
        for (var n = 0; n < pages.length; n++) {
          pages[n].hidden = n !== at;
        }
        prev.disabled = at === 0;
        next.disabled = at === pages.length - 1;
        for (var d = 0; d < dots.length; d++) {
          if (d === at) {
            dots[d].setAttribute('aria-current', 'true');
          } else {
            dots[d].removeAttribute('aria-current');
          }
        }
        status.textContent =
          pages[at].getAttribute('data-book-label') +
          ', ' + (at + 1) + ' of ' + pages.length;
      }

      prev.addEventListener('click', function () { show(at - 1); });
      next.addEventListener('click', function () { show(at + 1); });

      book.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') { show(at - 1); }
        else if (e.key === 'ArrowRight') { show(at + 1); }
        else { return; }
        e.preventDefault();
      });

      show(0);
    });
  })();
</script>
