const turnOnDarkMode = (options, save) => {
  const darkSwitch = document.getElementById('darkSwitch');
  const rapidoc = document.querySelector('rapi-doc');
  document.body.setAttribute('data-theme', 'dark');
  rapidoc.setAttribute('theme', 'dark');
  rapidoc.setAttribute('bg-color', options.dark.bgColor);
  rapidoc.setAttribute('text-color', options.dark['text-color']);
  rapidoc.setAttribute('nav-bg-color', options.dark['nav-bg-color']);
  rapidoc.setAttribute('nav-text-color', options.dark['nav-text-color']);
  rapidoc.setAttribute('nav-accent-color', options.dark['nav-accent-color']);
  document
    .querySelector('#logo')
    .setAttribute(
      'src',
      (src =
        'https://ui.adsabs.harvard.edu/help/common/images/transparent_logo.svg')
    );
  document.querySelector('#logo-container').style.backgroundColor = '#000';
  document.querySelector('#logo-text').style.color = '#c9d1d9';
  darkSwitch.classList.add('darkModeOn');
  darkSwitch.setAttribute('title', 'Turn off dark mode');

  // Change main content link color
  if (options.dark['main-link']) {
    const style = rapidoc.shadowRoot.querySelector('#custom-style');
    style.innerHTML =
      `*,:after,:before{box-sizing:border-box}:host{${options.dark['main-link']}}`;
  }
  // save to local storage
  if (save) localStorage.setItem('darkSwitch', 'on');
};

const turnOffDarkMode = (options, save) => {
  const darkSwitch = document.getElementById('darkSwitch');
  const rapidoc = document.querySelector('rapi-doc');
  document.body.removeAttribute('data-theme');
  rapidoc.setAttribute('theme', 'light');
  rapidoc.setAttribute('bg-color', options.light['bg-color']);
  rapidoc.setAttribute('text-color', options.light['text-color']);
  rapidoc.setAttribute('nav-bg-color', options.light['nav-bg-color']);
  rapidoc.setAttribute('nav-text-color', options.light['nav-text-color']);
  rapidoc.setAttribute('nav-accent-color', options.light['nav-accent-color']);
  document
    .querySelector('#logo')
    .setAttribute(
      'src',
      (src = '/help/img/bbb_assets/ads_partial_logo_dark_background.svg')
    );
  document.querySelector('#logo-container').style.backgroundColor = '#EEE';
  document.querySelector('#logo-text').style.color = '#5D5D5D';
  darkSwitch.classList.remove('darkModeOn');
  darkSwitch.setAttribute('title', 'Turn on dark mode');

  // Change main content link color
  if (options.light['main-link']) {
    const style = rapidoc.shadowRoot.querySelector('#custom-style');
    style.innerHTML =
      `*,:after,:before{box-sizing:border-box}:host{${options.light['main-link']}}`;
  }
  // save to local storage
  if (save) localStorage.setItem('darkSwitch', 'off');
};

const toggle = (options) => {
  const darkSwitch = document.getElementById('darkSwitch');
  if (darkSwitch.classList.contains('darkModeOn')) {
    turnOffDarkMode(options, true);
  } else {
    turnOnDarkMode(options, true);
  }
};

const init = (options) => {
  const darkSwitch = document.getElementById('darkSwitch');
  if (options.light['main-link']) {
    const style = document.createElement('style');
      style.setAttribute('id', 'custom-style');
      document.querySelector('rapi-doc').shadowRoot.appendChild(style);
  }
  // 1. check app setting
  if (localStorage.getItem('darkSwitch') !== null) {
    if (localStorage.getItem('darkSwitch') === 'on') {
      turnOnDarkMode(options, false);
    } else {
      turnOffDarkMode(options, false);
    }
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    // 2. check system setting
    turnOnDarkMode(options, false);
  } else {
    // 3. default to light
    turnOffDarkMode(options, false);
  }
  darkSwitch.addEventListener('click', function () {
    toggle(options);
  });
};

const initTheme = (options) => {
  document.addEventListener('DOMContentLoaded', function () {
    init(options);

    // hide body until theme is set to avoid flashing
    document.body.style.visibility = 'visible';
  });
}
