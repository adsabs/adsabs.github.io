---
layout: about_scix
title: Initiatives
subtitle: "Work the SciX team takes on alongside the library itself"
---

<div class="about-story">
<p>Collaborations and side projects the SciX team contributes to, separate from running the search service.</p>
<ul class="about-initiatives">
{% for initiative in site.data.initiatives.initiatives %}
  <li class="about-initiative">
    <a href="{{ site.baseurl }}/scixabout/initiatives/{{ initiative.id }}.html">{{ initiative.title }}</a>
  </li>
{% endfor %}
</ul>
</div>
