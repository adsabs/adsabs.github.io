{% comment %}
Bibliography page, shared by ADS (/about/bibliography) and SciX (/scixabout/bibliography).
Call with ads=true for ADS, ads=false for SciX. Content comes from _data/bibliography.yml,
which scripts/fetch-bibliography.py regenerates weekly; edit the script, not the data.
{% endcomment %}
{% if include.ads %}{% assign abs_root = site.ads_base_url %}{% else %}{% assign abs_root = site.scix_base_url %}{% endif %}
<p>Papers about ADS and SciX, the research that cites them, and the work of the people who build them. The lists are drawn from SciX and refreshed every week. Each section shows the newest papers; follow the link to see the full list in SciX.</p>

{% for section in site.data.bibliography.sections %}
<h3 id="{{ section.id | replace: '_', '-' }}">{{ section.title }}</h3>
<p>{% if section.papers.size < section.total %}The newest {{ section.papers.size }} of {{ section.total }} papers. {% else %}{{ section.total }} papers. {% endif %}<a href="{{ section.link }}">See all in SciX</a></p>
<ul>
{% for paper in section.papers %}  <li>{{ paper.authors }} ({{ paper.year }}), <a href="{{ abs_root }}/abs/{{ paper.bibcode | url_encode }}/abstract">{{ paper.title }}</a>{% if paper.pub != "" %}, <em>{{ paper.pub }}</em>{% endif %}.</li>
{% endfor %}</ul>
{% endfor %}

<p>Papers about {% if include.ads %}ADS{% else %}SciX{% endif %} that are missing from these lists can be sent to <a href="mailto:{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}">{% if include.ads %}adshelp@cfa.harvard.edu{% else %}help@scixplorer.org{% endif %}</a>.</p>
