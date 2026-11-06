{% comment %}
Bibliography page, shared by ADS (/about/bibliography) and SciX (/scixabout/bibliography).
Call with ads=true for ADS, ads=false for SciX. Content comes from _data/bibliography.yml,
which scripts/fetch-bibliography.py regenerates weekly; edit the script, not the data.
Styling from _sass/_bibliography.scss.

The six data sections are shown as four collapsible groups: refereed and non-refereed
lists share a group and are switched with pills.
{% endcomment %}
{% if include.ads %}{% assign abs_root = site.ads_base_url %}{% else %}{% assign abs_root = site.scix_base_url %}{% endif %}
{% assign bib_sections = site.data.bibliography.sections %}
{% assign groups = "about|Papers about ADS and SciX|How the system works, how it is used, and what it has meant for research.|team_refereed;team_non_refereed^citing|Papers citing ADS and SciX literature|Research that builds on the papers above.|citing_refereed;citing_non_refereed^acknowledging|Papers acknowledging ADS or SciX|Authors who thank ADS, SciX or the Science Explorer in their acknowledgments.|acknowledging^team|Research by the ADS and SciX team|Papers by current team members, found through their ORCID iDs.|team_research" | split: "^" %}
<div class="bib-page">

<p class="bib-lede">Papers about ADS and SciX, the research that cites them, and the work of the people who build them. The lists are drawn from SciX and refreshed every week. Each section shows the newest papers, with a link to the full list in SciX.</p>

<div class="bib-stats">
{% for g in groups %}{% assign g_parts = g | split: "|" %}{% assign g_ids = g_parts[3] | split: ";" %}{% assign g_total = 0 %}{% for sid in g_ids %}{% assign s = bib_sections | where: "id", sid | first %}{% assign g_total = g_total | plus: s.total %}{% endfor %}
  <a class="bib-stat" href="#{{ g_parts[0] }}" data-bib-open="{{ g_parts[0] }}">
    <span class="bib-stat-number">{% include _about/bib-number.html n=g_total %}</span>
    <span class="bib-stat-label">{{ g_parts[1] }}</span>
  </a>
{% endfor %}
</div>

{% for g in groups %}{% assign g_parts = g | split: "|" %}{% assign g_ids = g_parts[3] | split: ";" %}{% assign g_total = 0 %}{% for sid in g_ids %}{% assign s = bib_sections | where: "id", sid | first %}{% assign g_total = g_total | plus: s.total %}{% endfor %}
<details class="bib-section" id="{{ g_parts[0] }}"{% if forloop.first %} open{% endif %}>
  <summary>
    <span class="bib-summary-text">
      <span class="bib-summary-title">{{ g_parts[1] }}</span>
      <span class="bib-summary-blurb">{{ g_parts[2] }}</span>
    </span>
    <span class="bib-count">{% include _about/bib-number.html n=g_total %}</span>
  </summary>
  <div class="bib-section-body">
  {% if g_ids.size > 1 %}
    <div class="bib-filters" role="group" aria-label="Show refereed or non-refereed papers" hidden>
    {% for sid in g_ids %}{% assign s = bib_sections | where: "id", sid | first %}
      <button type="button" class="bib-pill{% if forloop.first %} is-active{% endif %}" data-bib-panel="{{ sid }}" aria-pressed="{% if forloop.first %}true{% else %}false{% endif %}">{% if sid contains "non_refereed" %}Non-refereed{% else %}Refereed{% endif %} ({% include _about/bib-number.html n=s.total %})</button>
    {% endfor %}
    </div>
  {% endif %}
  {% for sid in g_ids %}{% assign s = bib_sections | where: "id", sid | first %}
    <div class="bib-panel" data-bib-panel-id="{{ sid }}">
      {% if g_ids.size > 1 %}<h4 class="bib-list-title">{{ s.title }}</h4>{% endif %}
      <ul class="bib-list">
      {% for paper in s.papers %}
        <li class="bib-row">
          <span class="bib-row-year">{{ paper.year }}</span>
          <span>
            <a class="bib-row-title" href="{{ abs_root }}/abs/{{ paper.bibcode | url_encode }}/abstract">{{ paper.title }}</a>
            <span class="bib-row-meta">{{ paper.authors }}{% if paper.pub != "" %} · <em>{{ paper.pub }}</em>{% endif %}</span>
          </span>
        </li>
      {% endfor %}
      </ul>
      <p class="bib-seeall-wrap"><a class="bib-seeall" href="{{ s.link }}">{% if s.papers.size < s.total %}See all {% include _about/bib-number.html n=s.total %} in SciX{% else %}Open this list in SciX{% endif %} &rarr;</a></p>
    </div>
  {% endfor %}
  </div>
</details>
{% endfor %}

<p class="bib-footnote">Papers about {% if include.ads %}ADS{% else %}SciX{% endif %} that are missing from these lists can be sent to <a href="mailto:{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}">{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}</a>.</p>

<script>
  (function () {
    var page = document.querySelector('.bib-page');
    if (!page) return;

    // Refereed / non-refereed pills. Without JavaScript both lists show, each under its own heading.
    var groups = page.querySelectorAll('.bib-filters');
    for (var i = 0; i < groups.length; i++) {
      (function (filters) {
        var body = filters.parentNode;
        var pills = filters.querySelectorAll('.bib-pill');
        var panels = body.querySelectorAll('.bib-panel');
        function show(id) {
          for (var p = 0; p < panels.length; p++) {
            panels[p].hidden = panels[p].getAttribute('data-bib-panel-id') !== id;
          }
          for (var q = 0; q < pills.length; q++) {
            var on = pills[q].getAttribute('data-bib-panel') === id;
            pills[q].classList.toggle('is-active', on);
            pills[q].setAttribute('aria-pressed', on ? 'true' : 'false');
          }
        }
        for (var k = 0; k < pills.length; k++) {
          pills[k].addEventListener('click', function () { show(this.getAttribute('data-bib-panel')); });
        }
        var titles = body.querySelectorAll('.bib-list-title');
        for (var t = 0; t < titles.length; t++) titles[t].hidden = true;
        filters.hidden = false;
        show(pills[0].getAttribute('data-bib-panel'));
      })(groups[i]);
    }

    // Summary tiles and #anchors open the matching section.
    function openSection(id) {
      var section = document.getElementById(id);
      if (section && section.tagName === 'DETAILS') section.open = true;
    }
    var tiles = page.querySelectorAll('[data-bib-open]');
    for (var n = 0; n < tiles.length; n++) {
      tiles[n].addEventListener('click', function () { openSection(this.getAttribute('data-bib-open')); });
    }
    if (location.hash) openSection(location.hash.slice(1));
  })();
</script>
</div>
