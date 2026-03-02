---
layout: about
title: "Team"
---

Astrophysics Data Systems (ADS) Personnel:

{% for member in site.data.team.team_members %}{% unless member.role_type %}- [{{ member.name }}](../team/team/{{ member.id }}.html) - {{ member.title }}  
{% endunless %}{% endfor %}

Community Engagement Coordinator: 
{% for member in site.data.team.team_members %}{% if member.role_type == "community" %}- [{{ member.name }}](../team/team/{{ member.id }}.html)
{% endif %}{% endfor %}

ADS Research Associates:
{% for member in site.data.team.team_members %}{% if member.role_type == "research_associate" %}- [{{ member.name }}](../team/team/{{ member.id }}.html)
{% endif %}{% endfor %}

The late [Stephen S. Murray](https://www.cfa.harvard.edu/news/stephen-s-murray-high-energy-astrophysicist-dies-age-70) served as the Principal Investigator of the project from its inception in 1993 until his passing in August 2015.

If you have comments or questions about the ADS, you are welcome to contact any of us directly, although the preferred way to get in touch with ADS staff is through our support email (<a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}), which guarantees a timely reply to your inquiry.

<div>
  <div class="floated_img">
    <img src="{{ site.baseurl }}/about/team/img/Team_photo_Mar2024.jpeg" alt="Team photo from March 2024 Retreat" style="max-width: 100%; height: auto;">
  </div>
  <div class="textlabel">
    <p><b>Team photo from March 2024 Retreat</b></p>
  </div>
</div>
