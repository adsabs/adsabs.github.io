# {{ include.site }} Terms and Conditions of Use

Use of the {{ include.site }} services implies that the user has read and agrees to the following terms and conditions:

1. Full-text articles and abstracts of papers available from the {{ include.site }} databases are copyrighted by the respective publishers and are subject to all applicable copyright protection under the laws of the United States and other countries. The reproduction of full-text articles or abstracts requires express written permission from the publisher.

2. Individual users may download, store and print copies of such abstracts and articles for personal use only and provided that such copies are not sold or redistributed.

3. Users may not perform systematic downloads of articles, abstracts, or tables of contents for any purpose, whether commercial or not, without the written permission of the {{ include.site }}. This includes indiscriminate, mass downloads of search results and the use of robots.

4. The {{ include.site }} makes reasonable efforts to ensure that the contents of its archives are accurate. However, the {{ include.site }} does not guarantee the completeness, accuracy or usefulness of its databases and search interfaces. The {{ include.site }} is not to be considered liable for any delay, downtime, or other failure of performance in providing its services.

### Acknowledgements

If you wish to acknowledge the services provided by the {{ include.site }} in a publication, kindly use a phrase such as the following:

> This research has made use of the Astrophysics Data System, funded by NASA under Cooperative Agreement 80NSSC21M00561.

<hr>

# {{ include.site }} API Terms and Conditions of Use

The {{ include.site }} encourages the use of [its API]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/help/api) to create and release new and interesting ways to access and use the information held in our corpus and promotes tools made by the community, for the community.

However, to stop abuse of our systems, and to ensure the {{ include.site }} runs smoothly for other users and developers, there are some rules and regulations that API developers must follow.

<hr>

Use of the {{ include.site }} API implies that the developer has read and agrees to the following terms and conditions:

  1. Don't try to circumvent the restrictions placed on the API client tokens (e.g., rate limits and scopes) so that you can exceed your allowed quota of requests to our services. Contact us at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %} if you believe you need your allowed daily quota of requests to our system increased. Generally, we are able to help you modify your scripts to access our API in a more efficient manner and remain within the standard quota. On rare occasions, as we deem necessary and with proper justification, we are able to grant exceptional and temporary quota increases within the limits of our legal publisher agreements. In any case, access cannot violate the rest of our API terms of use or create a risk for the reliability and stability of our system. Also, do not try to access content that has been restricted. If the {{ include.site }} thinks you are trying to abuse its API in this way, we will have to block or delete your account.

  2. You won't try and reproduce the core experience that is given by the {{ include.site }} and its services - instead your should give us feedback for your suggested changes. You also shouldn't redistribute any data you obtain from our services to third-parties.

  3. You won't try to create a partial or full copy of the data maintained and made available by the API, either by systematically downloading or crawling our content. If you need to download and store {{ include.site }} data returned by the API on a regular basis, you should contact us first.  Failure to do so will lead to the suspension or deletion of your account.

  4. You should expect that the {{ include.site }} may change, or update the API periodically. Unfortunately, this could lead to some of your services not working due to backwards-incompatability issues, and you should handle this appropriately. Please pay attention to our [news posts]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/blog/) for possible information on API changes.

  5. It should be clear to you that if we suspect any abuse of an account that does not directly fall into the specific cases mentioned in the API terms of use, that we will still have to either suspend or delete your account. If this situation does arise, you will be notified with the e-mail address you used to sign-up with.

  6. If you feel that you do not agree with our API terms of use, then you should no longer access the API. By using the API, you are agreeing with the API terms of use outlined on this page.

  7. In the case of a dispute, we retain the possibility to share your contact information with other people who are affected by your use of the API, including users and providers of {{ include.site }} data.

  8. We encourage new applications, logos based on the {{ include.site }}, and community content. As such, you acknowledge that we may use your name, logos, content, and information, including screenshots and video captures of your application, to demonstrate or feature your use of the {{ include.site }} API, worldwide and royalty-free.

  9. To ensure our services run smoothly, and to build services based on usage from our developer community, you understand and acknolwedge that the {{ include.site }} will collect certain private information about you. The information we collect is described in our [privacy policy]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/help/privacy/), and if you do not agree with it, then you should stop using the {{ include.site }} API.

  10. As an API user, you and your application, should comply with all applicable laws or regulations. Do not violate any rights of any person, including but not limited to intellectual property rights, rights of privacy, or rights of personality.

Enjoy using the {{ include.site }} API, and please let us know at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %} if you come up with a new and interesting app!
