---
layout: about_scix
title: "Team"
---

Science Explorer (SciX) Personnel:
{% for member in site.data.team.team_members %}{% unless member.role_type %}- [{{ member.name }}](../team/team/{{ member.id }}.html) - {{ member.title_scix }}
{% endunless %}{% endfor %}

Community Engagement Coordinator: 
{% for member in site.data.team.team_members %}{% if member.role_type == "community" %}- [{{ member.name }}](../team/team/{{ member.id }}.html)
{% endif %}{% endfor %}

SciX Research Associates:
{% for member in site.data.team.team_members %}{% if member.role_type == "research_associate" %}- [{{ member.name }}](../team/team/{{ member.id }}.html)
{% endif %}{% endfor %}

The late [Stephen S. Murray](https://www.cfa.harvard.edu/news/stephen-s-murray-high-energy-astrophysicist-dies-age-70) served as the Principal Investigator of the Astrophysics Data Service (ADS) from its inception in 1993 until his passing in August 2015. SciX is the expansion of that digital library to heliophysics, earth science, and planetary science that began in 2021.

If you have comments or questions about the SciX, you are welcome to contact any of us directly, although the preferred way to get in touch with SciX staff is through our support email ([help [at] scixplorer.org](mailto:help@scixplorer.org)), which guarantees a timely reply to your inquiry.

<div>
<div style="float:left;">
  <div class="floated_img">
   <img src="{{ site.baseurl }}/about/team/img/Team_photo_Mar2024.jpeg" alt="Team photo from March 2024 Retreat" style="max-width: 100%; height: auto; float: left; margin: 4px 10px 0px 0px; border: 1px solid #000000;">
  </div>
  <div class="textlabel">
    <p><B>Team photo from March 2024 Retreat</B></p>
  </div>
</div>
