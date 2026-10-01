{% comment %}
SciX team mosaic. include.group is staff | community | research_associate.
Staff are members with no role_type. Shapes cycle so the cluster is not a square grid.
{% endcomment %}
{% assign n = 0 %}
<ul class="team-mosaic">
{% for member in site.data.team.team_members %}
  {% assign show = false %}
  {% if include.group == "staff" %}
    {% unless member.role_type %}{% assign show = true %}{% endunless %}
  {% elsif member.role_type == include.group %}
    {% assign show = true %}
  {% endif %}
  {% if show %}
    {% assign shape_n = n | modulo: 6 %}
    {% assign size_n = n | modulo: 5 %}
    {% assign tone_n = n | modulo: 5 %}
    {% if shape_n == 0 %}{% assign shape = "circle" %}
    {% elsif shape_n == 1 %}{% assign shape = "pentagon" %}
    {% elsif shape_n == 2 %}{% assign shape = "squircle" %}
    {% elsif shape_n == 3 %}{% assign shape = "arch" %}
    {% elsif shape_n == 4 %}{% assign shape = "hex" %}
    {% else %}{% assign shape = "petal" %}
    {% endif %}
    {% if size_n == 0 %}{% assign size = "lg" %}
    {% elsif size_n == 3 %}{% assign size = "sm" %}
    {% else %}{% assign size = "md" %}
    {% endif %}
    {% if tone_n == 0 %}{% assign tone = "navy" %}
    {% elsif tone_n == 1 %}{% assign tone = "cyan" %}
    {% elsif tone_n == 2 %}{% assign tone = "teal" %}
    {% elsif tone_n == 3 %}{% assign tone = "green" %}
    {% else %}{% assign tone = "orange" %}
    {% endif %}
    {%- comment -%}
    First initial plus surname initial. A hyphenated first name keeps both of
    its initials, so Jean-Claude Paquin reads JCP and Jeffrey Pomerantz JP
    rather than the two colliding on JP.
    {%- endcomment -%}
    {% assign parts = member.name | remove: "Dr. " | split: " " %}
    {% assign given_parts = parts.first | split: "-" %}
    {% assign initials = "" %}
    {% for given in given_parts %}{% assign g = given | slice: 0 %}{% assign initials = initials | append: g %}{% endfor %}
    {% assign surname_initial = parts.last | slice: 0 %}
    {% assign initials = initials | append: surname_initial %}
  <li class="team-chip team-chip--{{ shape }} team-chip--{{ size }} team-chip--{{ tone }}">
    <a href="{{ site.baseurl }}/scixabout/team/team/{{ member.id }}.html">
      <span class="team-chip-photo">
        {% if member.photo %}
        <img src="{{ site.baseurl }}{{ member.photo }}" alt="{{ member.name | escape }}" width="220" height="220" loading="lazy">
        {% else %}
        <span class="team-chip-initials" aria-hidden="true">{{ initials }}</span>
        {% endif %}
      </span>
      <span class="team-chip-name">{{ member.name }}</span>
      <span class="team-chip-title">{{ member.title }}</span>
    </a>
  </li>
    {% assign n = n | plus: 1 %}
  {% endif %}
{% endfor %}
</ul>
