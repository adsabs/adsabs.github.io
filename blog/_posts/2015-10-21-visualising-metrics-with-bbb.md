---
layout: blog_post
title: "Calculating and Visualizing Publication and Citation Metrics with ADS Bumblebee"
author: "Edwin Henneken"
position: "ADS Developer"
category: blog
label: general
thumbnail: blog/images/blog_2015-10-21_thumbnail.png
---

For many scientists, it's all about the numbers and when it comes to evaluating each other, it's no different. Project managers and administrators also want to be able to evaluate the impact of programs or instruments. As a result, [publication and citation “metrics”](http://exchanges.wiley.com/blog/2014/05/15/how-to-navigate-the-world-of-citation-metrics/) are an important part of any researcher’s dossier. Like it or [not](http://exchanges.wiley.com/blog/2010/11/10/can-we-do-better-than-existing-author-citation-metrics/), individuals and committees of all kinds use [metrics to evaluate](http://ucblibraries.colorado.edu/how/impact.htm) impact and performance of scientists. As a service to the astronomy community, the ADS is providing tools for calculating and visualizing these metrics within its brand new [Bumblebee](http://www.astrobetter.com/blog/2015/07/20/updates-on-ads-interfaces-and-the-announcement-of-bumblebee/) interface.

[Bumblebee](https://ui.adsabs.harvard.edu/#index/) can calculate metrics on the results of any search but in this post, we will show how to calculate them for an individual author.


To get started, go to [ADS Bumblebee](https://ui.adsabs.harvard.edu) and perform an [author query](http://adsabs.github.io/help/search/search-syntax/):

<div class="text-center">
    <img src="{{ site.baseurl }}/blog/images/blog_2015-10-21_image02.png" class="img-responsive"/>
</div>

On the search results page, click the Explore button and select Citation Metrics:

<div class="text-center">
    <img src="{{ site.baseurl }}/blog/images/blog_2015-10-21_image00.png" class="img-responsive"/>
</div>

The top panel displayed is a graphical representation of the search results as a histogram of the number of products published per year.

<img src="{{ site.baseurl }}/blog/images/blog_2015-10-21_image01.png" class="img-responsive"/>

Use this panel as a sanity check that your search is selecting the publications you are interested in, since all of the indices are calculated based on this set. On the left side of the panel, the total number of publications and the number of those which are refereed are listed. On the histogram, you can mouse over any data point to see the actual values. The first result set is for the default amount of publications (300). If you have more, you can specify that number in the box at the top of the overview (up to the maximum of 2,000). We expect to be able to increase this maximum at some point in the future.


There are panels that display information about Citations and Reads, but let’s focus on the Indices. The panel illustrates the values of various indices on any given year.

<img src="{{ site.baseurl }}/blog/images/blog_2015-10-21_image03.png" class="img-responsive"/>

On the left, the present value of many popular indices are calculated. Mouse over the help icon next to each index to get a brief description of how it’s calculated.

In the near future, you will be able to save/print the pages showing the metrics overview. In addition, we will provide permanent links to the metrics results pages so that these results can be more easily shared.

Please don’t take the inclusion or exclusion of a particular index as an indication on our part of its usefulness.  For example, one of the most popular and widely used metrics is the h-index.  It is also a highly controversial index. Using one metric to describe productivity is like using one moment to characterize a probability distribution, so please take these numbers with a grain of salt.  If you are interested in these topics or are on any search committees, we encourage you to explore some more esoteric indices such as the [read10, tori, and riq](http://adsabs.github.io/help/actions/analyze/), [which have been invented by our own team members](http://arxiv.org/abs/1209.2124).

These metrics are also available through our API, for those of you who want to access them programmatically. Details about our API can be found in the [github repo](https://github.com/adsabs/adsabs-dev-api) and on the [discussion group](https://groups.google.com/forum/#!forum/adsabs-dev-api).

We’re eager to hear how people like this tool and what other functionality you’d like to see in the future. Please let us know in the comments, contact us by email at [adshelp@cfa.harvard.edu](mailto:adshelp@cfa.harvard.edu), or Tweet at us [@adsabs](https://twitter.com/adsabs).
