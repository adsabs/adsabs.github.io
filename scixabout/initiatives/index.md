---
layout: about_scix
title: 'Initiatives'
---

Here you can find a list of initiatives that our project and staff members participate in. If you are interested in learning more about them, feel free to contact us.

{% for initiative in site.data.initiatives.initiatives %}- [{{ initiative.title }}](../initiatives/{{ initiative.id }}.html)
{% endfor %}
