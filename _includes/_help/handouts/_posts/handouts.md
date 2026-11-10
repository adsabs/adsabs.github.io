# {{ include.site }} Handouts

These handouts were created for conferences but also provide a quick reference guide for many {{ include.site }} features.

{% if include.ads %}* [Affiliations](http://ads.harvard.edu/handouts/ADS_affiliations_handout.pdf)
* [API](http://ads.harvard.edu/handouts/ADS_API_handout.pdf)
* [Metrics](http://ads.harvard.edu/handouts/ADS_metrics_handout.pdf)
* [my{{ include.site }}](http://ads.harvard.edu/handouts/ADS_myADS_handout.pdf)
* [ORCID](http://ads.harvard.edu/handouts/ADS_ORCiD_handout.pdf)
* [Second order operators](http://ads.harvard.edu/handouts/ADS_2ndorder_operators.pdf)
* [Visualizations](http://ads.harvard.edu/handouts/ADS_visualizations_handout.pdf){% else %}{% comment %}
The SciX PDFs live in scixhelp/handouts-scix/pdf/. To update a handout, replace its
PDF there and keep the file name, so these links keep working.
{% endcomment %}{% assign pdf = site.baseurl | append: "/scixhelp/handouts-scix/pdf/" %}* [Affiliations]({{ pdf }}SciX_affiliations_handout.pdf)
* [API]({{ pdf }}SciX_API_handout.pdf)
* [Email notifications]({{ pdf }}SciX_emailNotifications_handout.pdf)
* [Metrics]({{ pdf }}SciX_metrics_handout.pdf)
* [ORCID]({{ pdf }}SciX_ORCiD_handout.pdf)
* [Second order operators]({{ pdf }}SciX_2ndorder_operators.pdf)
* [Visualizations]({{ pdf }}SciX_visualizations_handout.pdf){% endif %}
