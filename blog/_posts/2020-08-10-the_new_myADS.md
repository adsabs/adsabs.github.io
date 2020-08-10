---
layout: blog_post
title: "Introducing the New myADS"
author: "Sergi Blanco-Cuaresma"
position: "ADS"
category: blog
label: news
thumbnail: blog/images/blog_2020-08-10_myADS_email.png
---

*[Sergi Blanco-Cuaresma](https://www.blancocuaresma.com/s/) is an astrophysicist and the Software Development & Operations Lead for the NASA Astrophysics Data System, based at the Harvard-Smithsonian Center for Astrophysics.*

The Astrophysics Data System (ADS) is pleased to introduce the new myADS email notification system! It is now more powerful than the 20-year-old ADS classic-based service thanks to the new, cutting-edge [ADS infrastructure](https://www.astrobetter.com/blog/2018/05/28/welcome-to-the-new-ads/).

Nowadays, it’s challenging to keep up with astronomical research given that thousands of new papers are published every week and that the number of papers that are relevant to you is only a small portion of what is published. The myADS service delivers customized emails based on your notification preferences to help distinguish the relevant signal from the noise.

myADS provides four main types of notifications:

- arXiv: Receive the daily list of new papers published in [arXiv](https://arxiv.org/) in a given set of categories (e.g., [Earth and Planetary Astrophysics](https://arxiv.org/list/astro-ph.EP/new) and/or [Solar and Stellar Astrophysics](https://arxiv.org/list/astro-ph.SR/new)). If an optional list of keywords is provided (e.g., *spectroscopy OR chemical abundances*), the system will automatically split the list in two: papers that match the keywords, and other articles in the selected categories. This will help you to identify the most relevant papers while still being able to browse the full list.
- Authors: Be notified of new publications from certain authors, especially from collaborators and colleagues that work in your area of interest. Authors can be disambiguated by using their [ORCID iDs](https://orcid.org/). (If you haven’t yet, please [register your ORCiD with ADS](https://adsabs.github.io/help/orcid/claiming-papers).)
- Citations: Keep track of the citations of a particular author or set of authors on a weekly basis. The most popular use case is to keep an eye on what papers are citing your own work.
- Keywords: Follow the most popular, recent, and cited papers that match a certain list of keywords (e.g., *gravitational waves OR cosmic microwave background*). 

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-08-10_myADS_settings.png" />
<em>Example of <a href="https://ui.adsabs.harvard.edu/user/settings/myads">myADS email notification settings</a></em>
</div>
<br>

No matter how many notifications you setup, they will be grouped together into a single daily or weekly email.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-08-10_myADS_email.png" />
<em>Example of a myADS weekly email</em>
</div>
<br>

These alerts cover many of the typical use cases, but the new myADS is ready to unleash the full ADS potential by allowing fully customizable notifications. Now, any valid ADS search query can be converted into a daily or weekly notification.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-08-10_myADS_general_query.png" />
<em>Create general myADS notifications from the ADS results page</em>
</div>
<br>

For instance, it’s possible to create daily or weekly notifications with useful queries such as:

- Citations to two specific papers:
    - [citations(bibcode:(2019MNRAS.486.2075B OR 2014A&A...569A.111B))](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=similar(citations(bibcode%3A(2019MNRAS.486.2075B%20OR%202014A%26A...569A.111B)))%20collection%3Aastronomy&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Citations to papers saved in a library (get the *library ID* by clicking on “View library in search results page” from the library view):
    - [citations(docs(library/L1iIrVsLTtiA8jp984C6eA))](https://ui.adsabs.harvard.edu/search/q=citations(docs(library%2FL1iIrVsLTtiA8jp984C6eA))&sort=date%20desc%2C%20bibcode%20desc&p_=0)
- Similar astronomical articles to the top 200 most recent citations to two specific papers:
    - [similar(citations(bibcode:(2019MNRAS.486.2075B OR 2014A&A...569A.111B))) collection:astronomy](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=similar(citations(bibcode%3A(2019MNRAS.486.2075B%20OR%202014A%26A...569A.111B)))%20collection%3Aastronomy&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Similar astronomical papers to the top 200 papers with Gaia-ESO in their title ranked by score:
    - [similar(title:"Gaia-ESO") collection:astronomy](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=similar(title%3A%22Gaia-ESO%22)%20collection%3Aastronomy&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Papers also read by users that read the top 200 most-read papers in which the title, abstract, or keywords contain certain words (e.g., *stellar spectroscopy*), as well as belong to the astronomy collection and were published after the year 2000:
    - [trending(topn(200, abs:(stellar spectroscopy chemical abundances) collection:astronomy year:2000-, "read_count desc"))](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=trending(topn(200%2C%20abs%3A(stellar%20spectroscopy%20chemical%20abundances%20collection%3Aastronomy)%20year%3A2000-%2C%20%22read_count%20desc%22))&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Papers also read by users that read the top 200 most frequently referenced articles by a given author:
    - [trending(useful(author:"^Blanco-Cuaresma, Sergi" collection:astronomy))](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=trending(useful(author%3A%22%5EBlanco-Cuaresma%2C%20Sergi%22%20collection%3Aastronomy))&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Papers that more frequently cite the top 200 most frequently referenced articles by a given author:
    - [reviews(useful(author:"^Blanco-Cuaresma, Sergi" collection:astronomy))](https://ui.adsabs.harvard.edu/search/fl=identifier%2C%5Bcitations%5D%2Cabstract%2Cauthor%2Cbibcode%2Ccitation_count%2Ccomment%2Cdoi%2Cid%2Ckeyword%2Cpage%2Cproperty%2Cpub%2Cpub_raw%2Cpubdate%2Cpubnote%2Cread_count%2Ctitle%2Cvolume%2Clinks_data%2Cesources%2Cdata%2Ccitation_count_norm%2Cemail%2Cdoctype&q=reviews(useful(author%3A%22%5EBlanco-Cuaresma%2C%20Sergi%22%20collection%3Aastronomy))&rows=25&sort=score%20desc%2C%20bibcode%20desc&start=0&p_=0)
- Refereed papers that talk about the open cluster M67:
    - [object:M67 property:refereed](https://ui.adsabs.harvard.edu/search/q=object%3AM67%20property%3Arefereed&sort=date%20desc%2C%20bibcode%20desc&p_=0)
- Software records that match the keyword “spectra”:
    - [doctype:software AND spectra](https://ui.adsabs.harvard.edu/search/q=doctype%3Asoftware%20AND%20spectra&sort=date%20desc%2C%20bibcode%20desc&p_=0)
- Most-read astronomical articles that contain “machine learning” in the full text:
    - [full:"machine learning" collection:astronomy](https://ui.adsabs.harvard.edu/search/q=full%3A%22machine%20learning%22%20collection%3Aastronomy&sort=read_count%20desc%2C%20bibcode%20desc&p_=0) (Sorted by read counts.)
- Articles that appeared in some arXiv categories (e.g., Earth and Planetary Astrophysics) that contain certain keywords (e.g., *stellar spectroscopy*):
    - [arxiv_class:(astro-ph.EP OR astro-ph.IM OR astro-ph.SR) (stellar spectroscopy OR chemical abundances OR atmospheric parameters)](https://ui.adsabs.harvard.edu/search/q=arxiv_class%3A(astro-ph.EP%20OR%20astro-ph.IM%20OR%20astro-ph.SR)%20(stellar%20spectroscopy%20OR%20chemical%20abundances%20OR%20atmospheric%20parameters)&sort=date%20desc%2C%20bibcode%20desc&p_=0)

Once queries are set up as myADS notifications, the system will automatically add a condition to the query to limit it to the last days or weeks (depending on the selected frequency). Hence, you will only get the most recent articles that match the specified criteria. A quick trick to simulate that time restriction is to append *entdate:[NOW-7DAYS TO NOW]* to any query, and you will see only the papers that match the criteria and that were ingested by ADS in the last week. (Just remember to remove that time restriction before creating a myADS notification.)

The weekly email will include only the top five articles for each notification (although the notification title is a link to the full list in ADS), while the daily email has a larger limit, although you can always reduce it by using the topn operator.

Notification emails from the classic myADS service were disabled on July 11, so now is the time to [learn how to create your own myADS email notifications](https://adsabs.github.io/help/userpreferences/myads) to stay on top of the latest news in your field with ADS! And as always, if you’d like to share any feedback about the new service, do not hesitate to [drop us a line](mailto:adshelp@cfa.harvard.edu) or tweet us [@adsabs](https://twitter.com/adsabs).

*This article was originally published on [AstroBetter](https://www.astrobetter.com/blog/2020/08/10/introducing-the-new-myads/).*

