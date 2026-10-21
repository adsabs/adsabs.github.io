{% comment %}
Shared awards content for both services. Pass ads=true for ADS branding
(rendered by about/awards.md) and no flag for SciX branding (rendered by
scixabout/awards.md).

Content lives in _data/awards.yml; styling lives in _sass/_awards.scss.

Awards are stored in strictly descending year order and render in that order,
so the wall reads newest first, left to right and top to bottom. Each tile's
width comes from `span` and each tile's tint comes from its decade, so colour
tracks age instead of being decorative.
{% endcomment %}
{% if include.ads %}{% assign team_url = '/about/team/' %}{% else %}{% assign team_url = '/scixabout/team/' %}{% endif %}
{% assign award_count = 0 %}
{% assign years = '' | split: '' %}
{% for section in site.data.awards.sections %}
  {% for award in section.awards %}
    {% assign award_count = award_count | plus: 1 %}
    {% assign y = award.year | append: '' %}
    {% unless years contains y %}
      {% assign years = years | push: y %}
    {% endunless %}
  {% endfor %}
{% endfor %}
{% assign years = years | sort | reverse %}
<div class="awards-page">
  <header class="awards-intro">
    <p class="awards-count"><span>{{ award_count }}</span> honors, {{ years | last }} to {{ years | first }}</p>
    <p class="awards-lede">
      {% if include.ads %}
      NASA, the Smithsonian, scientific societies, and the United Nations have recognized ADS and SciX for open, linked scientific literature.
      {% else %}
      NASA, the Smithsonian, scientific societies, and the United Nations have recognized SciX and ADS for open, linked scientific literature.
      {% endif %}
    </p>
  </header>

  {% for section in site.data.awards.sections %}
  <section class="awards-section awards-section--{{ section.id }}" id="awards-{{ section.id }}" aria-labelledby="awards-{{ section.id }}-title">
    <div class="awards-section-head">
      <h3 class="awards-section-title" id="awards-{{ section.id }}-title">{{ section.title }}</h3>
      {% if include.ads %}{% assign section_intro = section.intro_ads %}{% else %}{% assign section_intro = section.intro_scix %}{% endif %}
      {% if section_intro %}
      <p class="awards-section-intro">{{ section_intro }}</p>
      {% endif %}
    </div>

    <div class="awards-grid">
      {% for award in section.awards %}
      {%- comment -%}
      Colour is keyed to the awarding body, so the three UN commendations
      match each other, the Special Libraries Association awards match, and so
      on. It carries information rather than decorating by position.
      {%- endcomment -%}
      {% assign org = award.organization %}
      {% if org contains 'United Nations' %}{% assign body = 'un' %}
      {% elsif org contains 'Special Libraries' %}{% assign body = 'sla' %}
      {% elsif org contains 'Smithsonian Institution' %}{% assign body = 'si' %}
      {% elsif org contains 'NASA' %}{% assign body = 'nasa' %}
      {% elsif org contains 'Astrophysics' %}{% assign body = 'cfa' %}
      {% elsif org contains 'Royal Astronomical' %}{% assign body = 'ras' %}
      {% elsif org contains 'American Astronomical' %}{% assign body = 'aas' %}
      {% elsif org contains 'National Academy' %}{% assign body = 'nas' %}
      {% elsif org contains 'Minor Planet' %}{% assign body = 'mpc' %}
      {% elsif org contains 'Information Science' %}{% assign body = 'asist' %}
      {% else %}{% assign body = 'other' %}
      {% endif %}
      <article class="awards-card awards-card--{{ body }}{% if award.variant == 'hero' %} awards-card--hero{% elsif award.variant == 'featured' %} awards-card--featured{% endif %} awards-span-{{ award.span }}" id="award-{{ award.id }}">
        <p class="awards-year">{{ award.year }}</p>
        <p class="awards-org">{{ award.organization }}</p>
        <h4 class="awards-card-title">{% if award.url %}<a href="{{ award.url }}">{{ award.name }}</a>{% else %}{{ award.name }}{% endif %}</h4>
        {% if award.program %}
        <p class="awards-program">{{ award.program }}</p>
        {% endif %}
        {% if award.recipient %}
        <p class="awards-recipient">Awarded to {{ award.recipient }}</p>
        {% endif %}
        {% if award.blurb %}
        <p class="awards-blurb">{{ award.blurb }}</p>
        {% endif %}
        {% if award.quote %}
        <blockquote class="awards-quote">
          <p>{{ award.quote }}</p>
        </blockquote>
        {% endif %}
        {% if award.honorees %}
        <div class="awards-honorees">
          <p class="awards-honorees-label">Honorees</p>
          <ul class="awards-honoree-list">
            {% for honoree in award.honorees %}<li>{{ honoree }}</li>{% endfor %}
          </ul>
        </div>
        {% endif %}
        {% if award.attribution or award.links %}
        <div class="awards-card-foot">
          {% if award.attribution %}
          <p class="awards-attribution">{{ award.attribution }}</p>
          {% endif %}
          {% if award.links %}
          <p class="awards-links">
            {% for link in award.links %}<a class="awards-viewall" href="{{ link.url }}">{{ link.label }}</a>{% endfor %}
          </p>
          {% endif %}
        </div>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <p class="awards-footnote">
    Every award above rests on work done by a team.
    <a class="awards-viewall" href="{{ site.baseurl }}{{ team_url }}">Meet the team</a>
  </p>
</div>

<script>
  // Scroll reveal for the award tiles. Tiles are only hidden once this script
  // runs, so the page stays readable without JavaScript.
  (function () {
    var page = document.querySelector('.awards-page');
    if (!page || !('IntersectionObserver' in window)) {
      return;
    }
    if (
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches
    ) {
      return;
    }
    page.classList.add('awards-reveal-on');
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: '0px 0px -5% 0px', threshold: 0.02 }
    );
    var cards = page.querySelectorAll('.awards-section--heritage .awards-card');
    for (var i = 0; i < cards.length; i += 1) {
      observer.observe(cards[i]);
    }
  })();
</script>
