---
layout: blog_post
title: Super Charge your ADS Searches with Filters
author:  Alex Holachek
position: ADS Front End Developer
category: blog
label: news
thumbnail: blog/images/filter_pic.png
comment:
---

The majority of queries in ADS are searches for authors. Author searches are simple when the author has a unique name, but what happens when the name is a common one? A search "Wu, J" might bring back a huge number of papers from many different authors with the last name "Wu" and the first name starting with “J.”

Luckily, the new ADS interface offers several quick ways to narrow your paper set down to only the papers that you're looking for.

Let's use the name of the former ADS PI, Stephen S. Murray, as an example. Since Steve occasionally published papers with a variety of name variations ("Murray, S", “Murray, Stephen”, “Murray, Steve”, and others) our initial search will have to be broad: we will search for author:&ldquo;Murray, S".

The new ADS interface provides a wealth of information along with the list of records which satisfy the original query.  While your eye may typically go directly to the search results list in the center of the screen, it can be helpful to take a look at the surrounding objects, highlighted in orange in the picture below.

<img src="/blog/images/filter_pic.png" alt="a picture of the ADS interface with orange boxes around components of interest"  class="img-responsive">

The top box highlights the number of search results: 1,593. Let’s say we know enough about Steve's research output to realize that this number is suspiciously high and probably includes papers written by other individuals with a similar name.

In order to find the right set of papers we will [filter the set](https://adsabs.github.io/help/search/filter) of results to weed out the false hits. The first filter we probably want to apply is the author filter. We can click on the caret next to "Murray, S" to find all of the names that have been grouped under this category, select all of the possible variations, then click "or" on the small dropdown menu to the right to apply the filter.  Because we know (or infer based on the list of results) that Steve’s middle initial is “S.” we include the name variations where “S” appears as middle initial and exclude the other ones.

<img src="/blog/images/author_filter_detail.png" alt="detail view of author facet" class="img-responsive" style="margin:auto">


Just that step alone gets rid of over 500 records! Next, we can use the "Collections" filter and limit the set of papers to "astronomy", since we know Steve's papers fall into this category. This step prunes the list by an additional 100 records.

We have two more filters we might want to consider. First, we can take a look at the year distribution filter to the right, and see if any of the publication years shown there should definitely be filtered out.  Enforcing the results to be in a particular date range is a good way to weed out irrelevant records (e.g. records written in the early 1900s when looking for papers written by someone born much later).  However, in this case the dates seem to align with the years that Steve was active publishing research, so that filter is not going to help us at the moment.

So let's move on to the "Bib Groups" filter on the left. We can open it up and see if there are any bibliographies groups which Steve was affiliated with, and if so restrict the results to them only. In this case as well, however, all the curated groups-- CFA, HST, and so on-- make sense given what we know about Steve's career at SAO and JHU.  Had we known that all of his publications were meant to be in the CfA bibliography, we could have used that filter to further restrict the results.

Although the final two filters didn’t provide additional narrowing of the results, the information they contained did allow us to be more confident that this final list of about 960 papers is a better representation of Steve's research output than the 1,500+ papers we retrieved initially.

<b>Bonus round:</b> What can a user do to create a list that contains, with 100% accuracy, all papers which belong to a particular set (for instance to generate metrics about a person or project)?  In general, no simple query will provide the list of required papers, but this can be accomplished with a bit of domain knowledge and curation on your part. The easiest thing to do is to create a [private library in ADS](http://adsabs.github.io/help/libraries/). Then, you can click the checkbox at the top of the list of results to select all papers, then de-select only those papers that definitely don't belong in the list.   Add the selected papers to a library by using the library widget to the right, rinse and repeat for all ensuing pages of results.  The list will be stored in a persistent collection connected to your user account, and, if you choose, it can be made public so that other people can see it.

<img src="/blog/images/hand_curate.png" alt="how to add papers to an ADS library" class="img-responsive">
