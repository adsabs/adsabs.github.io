{% comment %}
  Presentations page, shared by ADS (/about/documents) and SciX
  (/scixabout/presentations). Call with ads=true for ADS, ads=false for SciX.
  Content comes from _data/presentations.yml; styling from _sass/_presentations.scss.
{% endcomment %}
{% assign all_presentations = site.data.presentations.presentations | sort: 'date' | reverse %}
{% assign hero = all_presentations | where: 'variant', 'hero' | first %}
{% assign featured = all_presentations | where: 'variant', 'featured' %}
{% assign blog_dir = 'scixblog' %}
{% if include.ads %}{% assign blog_dir = 'blog' %}{% endif %}
<div class="pres-page">

<p class="pres-lede">
  Talks, posters, workshops, demonstrations, and recordings from the
  {% if include.ads %}ADS/SciX{% else %}SciX{% endif %} team, covering both the
  project itself and the research of the people who build it. Slides, posters, and
  recordings are linked wherever they are publicly available.
</p>

{% if hero %}
<h3 class="pres-section-title">Highlights</h3>

{% assign hero_type_label = site.data.presentations.types[hero.type] %}
{% if hero.url %}{% if hero.url contains '://' %}{% assign hero_href = hero.url %}{% assign hero_external = true %}{% else %}{% assign hero_href = hero.url | prepend: site.baseurl %}{% assign hero_external = false %}{% endif %}{% endif %}
<div class="pres-hero{% unless hero.image %} pres-hero--flat{% endunless %} pres-reveal">
  {% if hero.image %}<img class="pres-hero-image" src="{{ site.baseurl }}{{ hero.image }}" alt="{{ hero.image_alt | escape }}" />{% endif %}
  <span class="pres-watermark" aria-hidden="true">{{ hero.date | date: "%Y" }}</span>
  <div class="pres-hero-body">
    <p class="pres-eyebrow">{% if hero.eyebrow %}{{ hero.eyebrow }}{% else %}{{ hero.venue }}{% endif %}</p>
    <h4 class="pres-hero-title">
      {% if hero_href %}<a href="{{ hero_href }}"{% if hero_external %} target="_blank" rel="noopener"{% endif %}>{{ hero.title }}</a>{% else %}{{ hero.title }}{% endif %}
    </h4>
    {% if hero.summary %}<p class="pres-hero-summary">{{ hero.summary }}</p>{% endif %}
    <p class="pres-hero-meta">
      <span class="pres-badge pres-badge--{{ hero.type }}">{% if hero.type == 'video' %}<i class="fa fa-play" aria-hidden="true"></i> {% endif %}{{ hero_type_label }}</span>
      <span class="pres-meta-date">{% if hero.date_display %}{{ hero.date_display }}{% else %}{{ hero.date | date: "%-d %b %Y" }}{% endif %}</span>
      {% if hero.people %}<span class="pres-meta-people">{{ hero.people }}</span>{% endif %}
    </p>
  </div>
</div>
{% if hero.blog_slug %}
{% assign hero_slug = hero.blog_slug %}{% unless include.ads %}{% if hero.blog_slug_scix %}{% assign hero_slug = hero.blog_slug_scix %}{% endif %}{% endunless %}
<p class="pres-hero-aside"><a href="{{ site.baseurl }}/{{ blog_dir }}/{{ hero_slug }}">Read the related blog post</a></p>
{% endif %}
{% endif %}

{% if featured.size > 0 %}
<div class="pres-featured-pair">
  {% for item in featured limit: 2 %}
  {% assign type_label = site.data.presentations.types[item.type] %}
  {% if item.url %}{% if item.url contains '://' %}{% assign item_href = item.url %}{% assign item_external = true %}{% else %}{% assign item_href = item.url | prepend: site.baseurl %}{% assign item_external = false %}{% endif %}{% else %}{% assign item_href = false %}{% endif %}
  <div class="pres-card pres-reveal">
    <span class="pres-watermark" aria-hidden="true">{{ item.date | date: "%Y" }}</span>
    {% if item.image %}
    <img class="pres-card-image" src="{{ site.baseurl }}{{ item.image }}" alt="{{ item.image_alt | escape }}" />
    {% endif %}
    <div class="pres-card-body">
      <p class="pres-eyebrow">{% if item.eyebrow %}{{ item.eyebrow }}{% else %}{{ item.venue }}{% endif %}</p>
      <h4 class="pres-card-title">
        {% if item_href %}<a href="{{ item_href }}"{% if item_external %} target="_blank" rel="noopener"{% endif %}>{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
      </h4>
      {% if item.summary %}<p class="pres-card-summary">{{ item.summary }}</p>{% endif %}
      <p class="pres-card-meta">
        <span class="pres-badge pres-badge--{{ item.type }}">{{ type_label }}</span>
        <span class="pres-meta-date">{% if item.date_display %}{{ item.date_display }}{% else %}{{ item.date | date: "%-d %b %Y" }}{% endif %}</span>
        {% if item.people %}<span class="pres-meta-people">{{ item.people }}</span>{% endif %}
      </p>
      {% if item.blog_slug %}
      {% assign post_slug = item.blog_slug %}{% unless include.ads %}{% if item.blog_slug_scix %}{% assign post_slug = item.blog_slug_scix %}{% endif %}{% endunless %}
      <p class="pres-card-aside"><a href="{{ site.baseurl }}/{{ blog_dir }}/{{ post_slug }}">Read the related blog post</a></p>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

<p class="pres-viewall-wrap">
  <a class="pres-viewall" href="#all-presentations">View all {{ all_presentations | size }} presentations</a>
</p>
{% endif %}

<h3 class="pres-section-title" id="all-presentations">All presentations</h3>
<p class="pres-filter-label" id="pres-filter-label">Show by type</p>
<div class="pres-filters" role="group" aria-labelledby="pres-filter-label">
  <button type="button" class="pres-pill is-active" data-pres-filter="all" aria-pressed="true">All</button>
  {% for type_pair in site.data.presentations.types %}
  <button type="button" class="pres-pill" data-pres-filter="{{ type_pair[0] }}" aria-pressed="false">{{ type_pair[1] }}</button>
  {% endfor %}
</div>

<ul class="pres-catalog">
  {% for item in all_presentations %}
  {% assign type_label = site.data.presentations.types[item.type] %}
  {% if item.url %}{% if item.url contains '://' %}{% assign item_href = item.url %}{% assign item_external = true %}{% else %}{% assign item_href = item.url | prepend: site.baseurl %}{% assign item_external = false %}{% endif %}{% else %}{% assign item_href = false %}{% endif %}
  <li class="pres-catalog-card" data-pres-type="{{ item.type }}">
    <span class="pres-badge pres-badge--{{ item.type }}">{{ type_label }}</span>
    <h4 class="pres-catalog-title">
      {% if item_href %}<a href="{{ item_href }}"{% if item_external %} target="_blank" rel="noopener"{% endif %}>{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
    </h4>
    <p class="pres-catalog-meta">{{ item.venue }}{% if item.people %} · {{ item.people }}{% endif %}</p>
    <p class="pres-catalog-date">{% if item.date_display %}{{ item.date_display }}{% else %}{{ item.date | date: "%b %Y" }}{% endif %}</p>
  </li>
  {% endfor %}
</ul>

<p class="pres-footnote">
  Missing something? If you gave a {% if include.ads %}ADS/SciX{% else %}SciX{% endif %}
  presentation that belongs here, or you have slides we can link, let us know at
  <a href="mailto:{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}">{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}</a>.
</p>

<script>
  (function () {
    var page = document.querySelector('.pres-page');
    if (!page) return;

    var pills = page.querySelectorAll('[data-pres-filter]');
    var cards = page.querySelectorAll('.pres-catalog-card');
    function apply(filter) {
      for (var i = 0; i < cards.length; i++) {
        var type = cards[i].getAttribute('data-pres-type');
        cards[i].hidden = !(filter === 'all' || type === filter);
      }
      for (var j = 0; j < pills.length; j++) {
        var on = pills[j].getAttribute('data-pres-filter') === filter;
        pills[j].classList.toggle('is-active', on);
        pills[j].setAttribute('aria-pressed', on ? 'true' : 'false');
      }
    }
    for (var k = 0; k < pills.length; k++) {
      pills[k].addEventListener('click', function () {
        apply(this.getAttribute('data-pres-filter'));
      });
    }

    var targets = document.querySelectorAll('.pres-reveal');
    if (!targets.length) return;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce || !('IntersectionObserver' in window)) {
      for (var i = 0; i < targets.length; i++) targets[i].classList.add('is-visible');
      return;
    }
    for (var j = 0; j < targets.length; j++) targets[j].classList.add('pres-reveal-armed');
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -10% 0px' });
    for (var n = 0; n < targets.length; n++) observer.observe(targets[n]);
  })();
</script>
</div>
