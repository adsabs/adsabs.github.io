{%- comment -%}
Media page content, shared by about/media/ and scixabout/media/.

Usage:
  {% include _media/media.md ads=true %}   for the ADS site
  {% include _media/media.md ads=false %}  for the SciX site

All coverage comes from _data/press.yml.
{%- endcomment -%}
{%- if include.ads -%}
  {%- assign site_name = "ADS" -%}
  {%- assign site_accent_class = "media-page--ads" -%}
  {%- assign blog_path = "/blog/" -%}
  {%- assign press_email = "adshelp@cfa.harvard.edu" -%}
  {%- assign primary_handle = "@adsabs" -%}
  {%- assign primary_social = "https://twitter.com/adsabs" -%}
{%- else -%}
  {%- assign site_name = "SciX" -%}
  {%- assign site_accent_class = "media-page--scix" -%}
  {%- assign blog_path = "/scixblog/" -%}
  {%- assign press_email = "help@scixplorer.org" -%}
  {%- assign primary_handle = "@SciXCommunity" -%}
  {%- assign primary_social = "https://twitter.com/SciXCommunity" -%}
{%- endif -%}
{%- assign all_items = site.data.press.coverage -%}
{%- assign release_items = all_items | where: "kind", "press-release" -%}
{%- assign coverage_items = all_items | where: "kind", "coverage" -%}
{%- assign team_items = all_items | where: "about", "team" -%}
{%- assign hero_items = all_items | where: "variant", "hero" -%}
{%- assign featured_items = all_items | where: "variant", "featured" | sort: "date" | reverse -%}
{%- assign compact_items = all_items | where: "variant", "compact" | sort: "date" | reverse -%}
{%- assign collage_items = hero_items | concat: featured_items | concat: compact_items -%}
<div class="media-page media-page--editorial {{ site_accent_class }}">
  <p class="media-intro">Press releases, interviews, and news coverage about {{ site_name }}, the Science Explorer, and the people who build them. For interview requests or background material, write to <a href="mailto:{{ press_email }}">{{ press_email }}</a>.</p>

  <div class="media-filters" role="group" aria-label="Filter coverage by category">
    <button type="button" class="media-pill is-active" data-media-filter="all" aria-pressed="true">All <span class="media-pill-count">({{ all_items | size }})</span></button>
    <button type="button" class="media-pill" data-media-filter="press-release" aria-pressed="false">Press releases <span class="media-pill-count">({{ release_items | size }})</span></button>
    <button type="button" class="media-pill" data-media-filter="coverage" aria-pressed="false">News coverage <span class="media-pill-count">({{ coverage_items | size }})</span></button>
    <button type="button" class="media-pill" data-media-filter="team" aria-pressed="false">Team members <span class="media-pill-count">({{ team_items | size }})</span></button>
  </div>
  <p class="media-filter-status" data-media-status role="status" aria-live="polite">Showing all {{ all_items | size }} items.</p>

  <div class="media-collage" data-media-list>
    {%- for item in collage_items -%}
    {%- if item.date_precision == 'year' -%}
      {%- assign item_date = item.date | date: "%Y" -%}
    {%- elsif item.date_precision == 'month' -%}
      {%- assign item_date = item.date | date: "%B %Y" -%}
    {%- else -%}
      {%- assign item_date = item.date | date: "%B %-d, %Y" -%}
    {%- endif -%}
    {%- assign tone_n = forloop.index0 | modulo: 5 -%}
    {%- if tone_n == 0 -%}{%- assign tone = "ink" -%}
    {%- elsif tone_n == 1 -%}{%- assign tone = "cyan" -%}
    {%- elsif tone_n == 2 -%}{%- assign tone = "paper" -%}
    {%- elsif tone_n == 3 -%}{%- assign tone = "teal" -%}
    {%- else -%}{%- assign tone = "orange" -%}
    {%- endif -%}
    {%- if item.variant == "hero" -%}{%- assign tone = "ink" -%}{%- endif -%}
    <article class="media-print media-print--{{ item.variant | default: 'compact' }} media-print--{{ tone }} media-reveal" data-media-kind="{{ item.kind }}" data-media-about="{{ item.about }}">
      <a href="{{ item.url }}" target="_blank" rel="noopener">
        {%- if item.image %}
        <span class="media-print-art">
          <img src="{{ site.baseurl }}{{ item.image }}" alt="{{ item.image_alt | escape }}" loading="lazy">
        </span>
        {%- endif %}
        <span class="media-print-copy">
          <span class="media-print-outlet">{{ item.outlet_short | default: item.outlet }}</span>
          <h3 class="media-print-title">{{ item.title }}</h3>
          <p class="media-print-meta">
            <span class="media-print-date">{{ item_date }}</span>
            {%- if item.person %}
            <span class="media-print-person">{{ item.person }}</span>
            {%- endif %}
          </p>
        </span>
      </a>
    </article>
    {%- endfor -%}
  </div>

  <section class="media-socials" aria-labelledby="media-socials-heading">
    <div class="media-section-head">
      <h3 id="media-socials-heading">Follow along</h3>
      <a class="media-viewall" href="{{ site.baseurl }}{{ blog_path }}">Read the blog</a>
    </div>
    <p class="media-socials-intro">We are {{ primary_handle }} on the channels below. Announcements, release notes, and conference plans go out here first.</p>
    <ul class="media-social-row">
      <li><a class="media-social" href="{{ primary_social }}" target="_blank" rel="noopener"><i class="fa fa-twitter" aria-hidden="true"></i><span class="media-social-label">{{ primary_handle }}</span><span class="media-social-platform">X / Twitter</span></a></li>
      {%- if include.ads %}
      <li><a class="media-social" href="https://twitter.com/SciXCommunity" target="_blank" rel="noopener"><i class="fa fa-twitter" aria-hidden="true"></i><span class="media-social-label">@SciXCommunity</span><span class="media-social-platform">X / Twitter</span></a></li>
      {%- endif %}
      <li><a class="media-social" href="https://www.linkedin.com/company/scixcommunity" target="_blank" rel="noopener"><i class="fa fa-linkedin" aria-hidden="true"></i><span class="media-social-label">SciX Community</span><span class="media-social-platform">LinkedIn</span></a></li>
      <li><a class="media-social" href="https://www.facebook.com/SciXCommunity" target="_blank" rel="noopener"><i class="fa fa-facebook" aria-hidden="true"></i><span class="media-social-label">SciXCommunity</span><span class="media-social-platform">Facebook</span></a></li>
      <li><a class="media-social" href="https://www.instagram.com/scixcommunity/" target="_blank" rel="noopener"><i class="fa fa-instagram" aria-hidden="true"></i><span class="media-social-label">scixcommunity</span><span class="media-social-platform">Instagram</span></a></li>
      <li><a class="media-social" href="https://youtube.com/@SciXCommunity" target="_blank" rel="noopener"><i class="fa fa-youtube-play" aria-hidden="true"></i><span class="media-social-label">SciXCommunity</span><span class="media-social-platform">YouTube</span></a></li>
      <li><a class="media-social" href="https://mastodon.social/@SciXCommunity" target="_blank" rel="noopener"><i class="fa fa-globe" aria-hidden="true"></i><span class="media-social-label">@SciXCommunity</span><span class="media-social-platform">Mastodon</span></a></li>
      <li><a class="media-social" href="https://web-cdn.bsky.app/profile/scixcommunity.bsky.social" target="_blank" rel="noopener"><i class="fa fa-cloud" aria-hidden="true"></i><span class="media-social-label">scixcommunity</span><span class="media-social-platform">Bluesky</span></a></li>
    </ul>
  </section>
</div>
<script>
  (function () {
    var page = document.querySelector('.media-page');
    if (!page) return;

    var pills = page.querySelectorAll('[data-media-filter]');
    var prints = page.querySelectorAll('[data-media-list] .media-print');
    var status = page.querySelector('[data-media-status]');

    function labelFor(filter) {
      var pill = page.querySelector('[data-media-filter="' + filter + '"]');
      if (!pill) return filter;
      return pill.textContent.replace(/\s*\(\d+\)\s*$/, '').trim();
    }

    function applyFilter(filter) {
      var shown = 0;
      for (var i = 0; i < prints.length; i++) {
        var print = prints[i];
        var match =
          filter === 'all' ||
          print.getAttribute('data-media-kind') === filter ||
          print.getAttribute('data-media-about') === filter;
        print.hidden = !match;
        if (match) shown++;
      }
      for (var j = 0; j < pills.length; j++) {
        var active = pills[j].getAttribute('data-media-filter') === filter;
        pills[j].setAttribute('aria-pressed', active ? 'true' : 'false');
        pills[j].classList.toggle('is-active', active);
      }
      if (status) {
        status.textContent =
          filter === 'all'
            ? 'Showing all ' + shown + ' items.'
            : 'Showing ' + shown + ' of ' + prints.length + ' items in ' + labelFor(filter) + '.';
      }
    }

    for (var k = 0; k < pills.length; k++) {
      pills[k].addEventListener('click', function () {
        applyFilter(this.getAttribute('data-media-filter'));
      });
    }

    if (!('IntersectionObserver' in window)) return;

    page.classList.add('media-reveal-ready');

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.05 }
    );

    var targets = page.querySelectorAll('.media-reveal');
    for (var n = 0; n < targets.length; n++) observer.observe(targets[n]);
  })();
</script>
