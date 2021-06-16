---
layout: blog_post
title: "User-Developed Tools for ADS"
author: "Kelly Lockhart"
position: "ADS"
category: blog
label: general
thumbnail: blog/images/blog_2019_07_30_3rd-party-tools.png
---

<meta property="og:image" content="https://ui.adsabs.harvard.edu/blog/images/blog_2019_07_30_3rd-party-tools.png">
<meta property="og:description" content="User-Developed Tools for ADS">

ADS [was started](https://ui.adsabs.harvard.edu/about/history/) in the late 1980s by astronomers, for astronomers, and has long received public funding via NASA grants. This history has meant that we’ve long been open to community involvement, and we’ve taken this a step further with the new ADS. The new ADS’s [codebase](https://github.com/adsabs) is open-source, which means that the code that makes up our website and data pipelines is available for users to look at, contribute to, or use for their own projects. Also, we’ve made our database more accessible by allowing users to access our holdings via [our API](https://github.com/adsabs/adsabs-dev-api).

The API in particular has enabled users to develop an ecosystem of new tools to keep up with the literature and to maintain professional and personal bibliographies. In this post, we highlight a few of these third-party tools developed by our user community. Note that these tools were all developed independently of ADS, so if you have questions about them, please contact the developers directly.

The **ADS Python library** ([Github](https://github.com/andycasey/ads), [Read the Docs](https://ads.readthedocs.io/en/latest/), [PyPI](https://pypi.org/project/ads/)) was developed by [Andy Casey and collaborators](https://ads.readthedocs.io/en/latest/#authors). While the API can be [accessed via Python](https://github.com/adsabs/adsabs-dev-api/blob/master/Converting_curl_to_python.ipynb) without using this library, the library provides a more user-friendly interface and more efficient memory usage.

The Kepler Guest Observer Office’s [publications list](https://keplerscience.arc.nasa.gov/publications.html) is maintained with their **kpub** tool  ([Github](https://github.com/KeplerGO/kpub)), using the ADS Python library highlighted above. Casual browsers can view mission publication lists and statistics on the KeplerGO website, while astronomers involved in the mission can add relevant publications to the Kepler bibliography with the kpub tool.

[Astropy](https://www.astropy.org/)'s **astroquery** ([Github](https://github.com/astropy/astroquery), [Read the Docs](https://astroquery.readthedocs.io/en/latest/)) package is a standardized interface for querying various astronomical databases. A module for querying ADS via our API is included in the larger package.

**Ads2gephi** ([Github](https://github.com/03b8/ads2gephi)), written by Theodor Costea for [a project](../blog/concepts-at-work) run by historian of science Karin Pelte, is a package that queries ADS and returns the results in a format compatible with Gephi, a popular network visualization tool. In these networks, individual papers serve as graph nodes, while citations and references serve as the edges connecting them. The ads2gephi tool enables this data extraction and readies the extracted data for visualization.

Several users have created bibliography management tools to make it easier for astronomers to manage their reference lists:
* **ADS to BibDesk** ([Github](https://github.com/r-xue/ads2bibdesk), [PyPI](https://pypi.org/project/ads2bibdesk/)), written by Rui Xue for MacOS, is based on an older version of a package by the same name ([Github](https://github.com/jonathansick/ads_bibdesk)) originally developed for Classic by Jonathan Sick but updated by Xue to use the new ADS’s API. Like the older package, ADS to BibDesk uses ADS to update and maintain the user’s local [BibDesk](https://bibdesk.sourceforge.io/) database.
* **Bibmanager** ([Github](https://github.com/pcubillos/bibmanager), [Read the Docs](https://bibmanager.readthedocs.io/en/latest/), [PyPI](https://pypi.org/project/bibmanager/)), written by Patricio Cubillos, is a combination bibliography manager, LaTeX .bib file generator, and ADS query tool. With bibmanager, at the command line you can search ADS for new or updated papers, add them to your main bibliography database, and generate the bibliography file for a LaTeX document that already contains citations.
* **Adstex** ([Github](https://github.com/yymao/adstex), [PyPI](https://pypi.org/project/adstex/)), written by Yao-Yuan Mao, allows you to bypass downloading BibTeX or other paper metadata to a master local database. Instead, you write your paper using TeX and cite commands as normal, then run adstex on the TeX document. The tool checks your paper for any cite commands, queries ADS, and downloads the necessary BibTeX entries to a .bib file for the paper.

Let us know if you’ve written or if you use any other tools that use our API! We may include them in an updated version of this post in the future. And if you haven’t yet tried out our API for your own projects, find our Jupyter notebooks with instructions and example code on our [Github repo](https://github.com/adsabs/adsabs-dev-api).
