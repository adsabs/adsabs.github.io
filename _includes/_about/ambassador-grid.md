{% comment %}
Ambassador photo cards. include.root is /scixabout/ambassador/team or /about/ambassador/team.
{% endcomment %}
{% assign root = include.root %}
{% for cohort in site.data.ambassadors.cohorts %}
<h3 class="about-group-title">{{ cohort.title }}</h3>
<ul class="amb-grid">
  {% for m in cohort.members %}
  <li class="amb-card">
    <a class="amb-card-link" href="{{ site.baseurl }}{{ root }}/{{ m.slug }}.html">
      <span class="amb-card-photo">
        <img src="{{ site.baseurl }}{{ m.photo }}" alt="{{ m.photo_alt | escape }}" width="280" height="280" loading="lazy">
      </span>
      <span class="amb-card-name">{{ m.name }}</span>
      <span class="amb-card-field">{{ m.field }}</span>
    </a>
  </li>
  {% endfor %}
</ul>
{% endfor %}
