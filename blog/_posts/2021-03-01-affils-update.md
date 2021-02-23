---
layout: blog_post
title: "Affiliation data in ADS: a work in progress"
author: "Matthew Templeton and Carolyn Grant"
position: "ADS"
category: blog
label: general
---

We publicly introduced our affiliations feature in a [blog post](https://ui.adsabs.harvard.edu/blog/affiliations-feature) last year, including a discussion of how the feature was built and maintained, and how you can use it in your literature searches.  We want to reintroduce this feature, especially for those who haven’t used it yet, by updating you on the developments and improvements in our affiliation data.

Users should note that while affiliation information is more than 80% complete across all literature, not all records contain an affiliation. We strongly recommend combining affiliation searches with author searches for best results.

### What are Affiliations?

An affiliation is whatever metadata a bibliographic record contains listing a contributing author’s institutional location and/or membership(s).  In nearly all modern literature, affiliation metadata is specifically fielded as such by publishers, and can be extracted, tagged, and made available for search.  The ADS has always maintained affiliation data as a separate field within records and we encourage authors and publishers to include this with their author metadata. What has changed has been the inclusion of affiliation as a searchable field, and the assignment of unique identifiers to individual affiliation strings to improve their discoverability.

Authors from a given institution may publish their work in a variety of journals and other venues, all of which may have separate editorial requirements.  Likewise, publication in a less formal venue such as a conference proceeding may have no restrictions on formatting or fielding (or even inclusion) of affiliations, and authors are free to use whatever identifier they choose.  This is (sometimes) straightforward for a human being to interpret, but there is enough variation in how departmental and institutional affiliations are given by different authors over time that searching them as a simple text field will produce incomplete and sometimes inaccurate results.  The ADS has developed a curated database of affiliation identifiers where we have collected all of the various text representations of a given affiliation and assigned them [an affiliation identifier](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv) where it is possible to do so unambiguously.  This powers our affiliation search feature, allowing you to search and select literature on the basis of affiliation data.  With ADS, you have two ways to use affiliation data in your searches: through the affiliation search filter, and directly in your search queries.  We show you how below.

### Using affiliations in your literature search

**Affiliation filtering**

The ADS interface enables you to refine your search using filters, located on the left hand side of the default view of search results.  When you search for anything in ADS, your search results also automatically populate all of the search filters which let you refine your results.  There are several filters including: author, collection, keywords, and institutions.  The Institutions filter is where you use the affiliation data to refine your searches.  For example, if you search for "gravitational waves" and "year:2020" you’ll get a list of over 3,300 papers published in the year 2020 that contain the phrase "gravitational waves".  If you click *INSTITUTIONS* in the left column, you’ll get an abbreviated list of the most-frequently seen affiliations among those 3,300 papers:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_1.jpg" />
</div>
<br>

If you select one of those affiliations (by checking the box to the left), you’ll see the following:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_2.jpg" />
</div>
<br>

Note especially the "limit to" and "exclude" options; if you select "limit to", your original set of results will be refined to just those 155 papers having one or more coauthors from the Max Planck Institute:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_3.jpg" />
</div>
<br>

Now, you can use other filters to refine your search, including the institution filter itself.  Clicking *INSTITUTIONS* again will give you a list of affiliations seen among the new result set, the list of 155 papers with an MPI coauthor.  In this way, you could (for example) search for papers with collaborators from two specific institutions, or determine which institutions collaborated most often on gravitational waves in 2020.



**Searching affiliations**

You can also use affiliations directly as part of your search, just as you can other metadata fields like title, year, and bibstem.  We have a number of different keywords with which to access affiliations:  

* *aff*: This field holds the raw affiliation string -- whatever text is supplied to us by a publisher or author as representing one or more authors' affiliation or host institution. (e.g. aff:"SRON").  Use this if you're looking for a specific string (rather than a specific identifier) in an affiliation; it doesn't use the curated identifiers as part of the search.

* *aff_id*: This field gives you access to the affiliation identifications curated by the ADS, including synonyms with other institutional identifier systems like GRiD and ROR.

* *inst*:



### Curated affiliation metadata: by the numbers

We significantly expanded curated affiliation coverage in ADS over the past twelve months.  In January 2020, ADS contained about 38.6 million individual author-affiliation pairs -- each affiliation of each author of all the papers, articles, and books in ADS.  Today, that number is about 42 million, an increase of 3.2 million (8%).  Of those 42 million strings, 34.7 million (83%) have been matched to identifiers and can be searched via the affiliation filter.  The remaining 7.3 million (17%) have not; they can be searched as a text field (i.e. with the "aff" keyword), but not via the *INSTITUTIONS* filter.

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_matched.jpg" />
</div>
<br>

This is a large improvement over last year’s numbers, where only 22 million (57%) of the 38.6 million pairs were matched, and 16.6 million (43%) were not.  We have not only kept up with assigning affiliation identifiers to new publications over the past year, but we have significantly expanded coverage of our existing metadata, meaning that more of our papers can be searched using our affiliations tools.


<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_unmatched.jpg" />
</div>
<br>

We streamlined the process of matching identifiers in 2020; matching strings to identifiers is still done by hand but we sped up the process by scripting aspects of the text manipulation and extraction process, searching for substrings common to different affiliation strings, and then using simple text processing and human analysis to confirm identifications.  We placed particular emphasis on looking for substrings that appeared thousands of times, even if the individual affiliations containing those substrings may be less common.  Many affiliations fell into this category, particularly individual universities represented in multiple categories in ADS, such as physics, astronomy, chemistry, computer science and engineering.  By targeting those substrings that occur most frequently, we can generate more matches overall, and we added them more quickly -- it was easier to disambiguate among departments and laboratories in a single university than across multiple institutions.  This work is still in progress, and we are shifting focus to the country-level to ensure more complete international coverage.

### Improvements and additions over the past year

Another reason our coverage increased is that we expanded the number of identifiers to nearly 7000 different entities and parent-child relationships, which lets us match more institutions that are easily assignable, and helps us disambiguate entities that may have multiple parents or warrant better subdivision at the department or institution level.

Many of the IDs were added simply to pick up frequently observed affiliations that were not already in the list, including medical research institutes and commercial entities involved in physics-related fields.  But a significant number of our additions have targeted specific classes of institutions: more universities and institutions from the Global South; more complete coverage of US federally-recognized Historically Black Colleges and Universities (HBCU); and Tribal Colleges and Universities (mainly in the United States).

**Institutions in the Global South**

We've increased coverage of educational and research institutions in the [Global South](https://en.wikipedia.org/wiki/Global_South) to improve the discovery and searchability of work from authors outside of historical centers of research.  Prior to this past year, our identifiers covered some of this territory, particularly in regions of the Global South with historical involvement in astronomy (South America, South Africa, India, and China).  Over the past year, we've worked to expand this coverage to include more countries and institutions involved in science that falls outside of our astronomy coverage but may be very active in related fields such as physics and materials science, computer science and engineering, or geology.  Further, researchers from these regions are often involved in collaborative science with researchers from the Global North, and thus including these institutions improves the affiliation coverage of existing literature.  We expect that the fraction of scientific literature from the Global South will increase over time (including in our core literature of Astronomy and Physics) and making these identifiers now will make it easier to keep up with these demographic changes as they happen.  We hope that this improved coverage will assist research by our colleagues world-wide, and aligns with global initiatives by organizations like the IAU's [Office of Astronomy for Development (OAD)](http://www.astro4dev.org/).


**Historically Black Colleges and Universities (HBCUs)**

As of last year, we were already assigning identifiers to a number of Historically Black Colleges and Universities (HBCUs), particularly those with historically strong programs in science and engineering (most notably: Hampton University in Virginia, USA, and Howard University in Washington, DC.)  During the past year, we have expanded our coverage to include all federally-recognized HBCUs represented in ADS literature.  The list of HBCUs and their affiliation IDs can be accessed [here](https://github.com/adsabs/CanonicalAffiliations/blob/master/historically_black_colleges_universities.tsv).  Note that we have not included the entire list of federally designated schools; we excluded those not represented in literature and whose focus mostly lies outside the scope of ADS, including business, law, and divinity schools.

**Tribal Colleges and Universities (TCUs)**

We have also added affiliation IDs for a partial list of Tribal Colleges and Universities (TCUs), primarily those in the United States that are currently represented in ADS Literature.  The list of included TCUs can be accessed [here](https://github.com/adsabs/CanonicalAffiliations/blob/master/tribal_colleges_universities.tsv); note that this list includes only those institutions designated as tribally-controlled, and does not include those public or private non-Tribal institutions serving a significant Tribal population.  

There are relatively few publications affiliated with these colleges: Salish Kootenai College (Montana), Northwest Indian College (Pacific NW), Dine College (Arizona) and Fond du Lac Tribal College (Minnesota) have the most publications. Papers written by TCU authors and coauthors in ADS primarily focus on topics in Environmental Science and Science Education, which are not currently part of our core literature.  Again, our goal is to ensure contributions to ADS literature by our colleagues at these institutions can be tracked.


### You can help!

Affiliation identification is an ongoing process and always will be.  If you find affiliation IDs that aren't correct, please let us know.  Likewise if there are affiliations that you think should be included or better disambiguated as parents and children, please get in touch.  We would especially welcome help with the assignment and disambiguation of French UMRs and Universities, and Russian and Chinese Academies of Science.
