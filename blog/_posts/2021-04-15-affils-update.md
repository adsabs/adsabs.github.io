---
layout: blog_post
title: "Affiliation data in the ADS: a work in progress"
author: "Matthew Templeton and Carolyn Grant"
position: "ADS"
category: blog
label: general
---

We publicly introduced our affiliations feature in a [blog post](https://ui.adsabs.harvard.edu/blog/affiliations-feature) last year, including a discussion of how the feature was built and maintained, and how you can use it in your literature searches.  We want to reintroduce this feature, especially for those who haven't used it yet, by updating you on the developments and improvements in our affiliation data.

Users should note that while affiliation information is more than 80% complete across all literature, not all records contain an affiliation. We strongly recommend combining affiliation searches with author searches for best results.

### What are Affiliations?

An affiliation is whatever metadata a bibliographic record contains listing a contributing author's institutional location and/or membership(s).  In nearly all modern literature, affiliation metadata is specifically fielded as such by publishers, and can be extracted, tagged, and made available for search.  The ADS has always maintained affiliation data as a separate field within records and we encourage authors and publishers to include this with their author metadata. What has changed has been the inclusion of affiliation as a searchable field, and the assignment of unique identifiers to individual affiliation strings to improve their discoverability.

Authors from a given institution may publish their work in a variety of journals and other venues, all of which may have separate editorial requirements.  Likewise, publication in a less formal venue such as a conference proceeding may have no restrictions on formatting or fielding (or even inclusion) of affiliations, and authors are free to use whatever identifier they choose.  This is (sometimes) straightforward for a human being to interpret, but there is enough variation in how departmental and institutional affiliations are given by different authors over time that searching them as a simple text field will produce incomplete and sometimes inaccurate results.  The ADS has developed a curated database of affiliation identifiers where we have collected all of the various text representations of a given affiliation and assigned them [an affiliation identifier](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv) where it is possible to do so unambiguously.  This powers our affiliation search feature, allowing you to search and select literature on the basis of affiliation data.  With the ADS, you have two ways to use affiliation data in your searches: through the affiliation search filter, and directly in your search queries.  We show you how below.

### Using affiliations in your literature search

**Affiliation filtering**

The ADS interface enables you to refine your search using filters, located on the left hand side of the default view of search results.  When you search for anything in the ADS, your search results also automatically populate all of the search filters which let you refine your results.  There are several filters including: author, collection, keywords, and institutions.  The Institutions filter is where you use the affiliation data to refine your searches.  For example, if you search for "gravitational waves" and "year:2020" you'll get a list of over 3,300 papers published in the year 2020 that contain the phrase "gravitational waves".  If you click *INSTITUTIONS* in the left column, you'll get an abbreviated list of the most-frequently seen affiliations among those 3,300 papers:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-04-15_affil_drop_1.jpg" />
</div>
<br>

If you select one of those affiliations (by checking the box to the left), you'll see the following:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-04-15_affil_drop_2.jpg" />
</div>
<br>

Note especially the "limit to" and "exclude" options; if you select "limit to", your original set of results will be refined to just those 155 papers having one or more coauthors from the Max Planck Institute:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-04-15_affil_drop_3.jpg" />
</div>
<br>

Now, you can use other filters to refine your search, including the institution filter itself.  Clicking *INSTITUTIONS* again will give you a list of affiliations seen among the new result set, the list of 155 papers with an MPI coauthor.  In this way, you could (for example) search for papers with collaborators from two specific institutions, or determine which institutions collaborated most often on gravitational waves in 2020.



**Searching affiliations**

You can also use affiliations directly as part of your search, just as you can other metadata fields like title, year, and bibstem. We have a number of different keywords with which to access affiliations:

* *aff*: This field holds the raw affiliation string -- whatever text is supplied to us by a publisher or author as representing one or more authors' affiliation or host institution. (e.g. aff:"SRON"). Use this if you're looking for a specific string (rather than a specific identifier) in an affiliation; it does not use the curated identifiers as part of the search.

* *aff_id*: This field can be used to search for affiliation identifications curated by the ADS, including synonyms with other institutional identifier systems like GRID and ROR.  It requires you to use the controlled dictionary of identifiers specified <here> (https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv).  It does not expand the search to include an institution's children.

* *inst*: This field is a shortcut to enable you to search for institutions without requiring you to know their parent.  It also allows you to search the affiliation identifications curated by the ADS, including synonyms with other institutional identifier systems like GRID and ROR.  Unlike aff_id, it expands the search to include an institution's children.  It is convenient for unique institutions such as the "CfA".  However, for an institution that is not unique, such as "Inst Phy", you will want to include the parent to disambiguate.

Some examples:

* Sometimes, there are multiple ways of obtaining the same affils.  For example, all of the following will return the Center for Astrophysics: inst:"CfA" == inst:"Harvard U/CfA" == inst:"SI/CfA" = aff_id:"CfA".  Conversely, aff_id:"SI" returns only affiliation "Smithsonian Institution"

* Inst is generally more "greedy" in matching than aff_id, so while aff_id:"SI" only returns papers that are identified with only the parent "Smithsonian Institution", inst:"SI" returns affiliation "Smithsonian Institution", plus CfA (Center for Astrophysics), MNH (Museum of Natural History), Air Sp Mus (Air and Space Museum), which are children of SI.

* Likewise, 

    aff_id:"Inst Phy" returns no results

    inst:"Inst Phy" returns results from many Institutes of Physics.

* But you can use inst searches to get specific results, like,

    inst:"UNAM/Inst Phy" (National Autonomous University of Mexico's Institute of Physics)

    inst:"NTU/Inst Phy" (National Taiwan University's Institute of Physics)

    inst:"U Amsterdam/Inst Phy" (University of Amsterdam's Institute of Physics)


**Tips for searching:**

If you do not see the results you expect, one or more of the following may help:

- Check the spelling against our controlled list of institutions (we may be using an English equivalent, such as "University of" instead of "Universite de" or "Center" instead of "Centre").

* Sometimes we elevate an institution to a parent level so that it may have children/divisions (e.g. Both "NASA" and "NASA Goddard" are at the parent level so that we can subdivide "NASA Goddard" into units).  

* We may be using a non-standard abbreviation for a university in order to avoid duplication ("USC SC" for University of South Carolina versus "USC CA" for University of Southern California).

* Make the search less constrictive (try to search for a parent institution and use the facet to drill down to the unit level).



### Curated affiliation metadata: by the numbers

We significantly expanded curated affiliation coverage in the ADS over the past twelve months.  In January 2020, the ADS contained about 38.6 million individual author-affiliation pairs -- each affiliation of each author of all the papers, articles, and books in the ADS.  Today, that number is about 42 million, an increase of 3.2 million (8%).  Of those 42 million strings, 34.7 million (83%) have been matched to identifiers and can be searched via the affiliation filter.  The remaining 7.3 million (17%) have not; they can be searched as a text field (i.e. with the "aff" keyword), but not via the *INSTITUTIONS* filter.

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-04-15_matched.jpg" />
</div>
<br>

This is a large improvement over last year's numbers, where only 22 million (57%) of the 38.6 million pairs were matched, and 16.6 million (43%) were not.  We have not only kept up with assigning affiliation identifiers to new publications over the past year, but we have significantly expanded coverage of our existing metadata, meaning that more of our papers can be searched using our affiliations tools.


<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-04-15_unmatched.jpg" />
</div>
<br>

We streamlined the process of matching identifiers in 2020; matching strings to identifiers is still done by hand but we sped up the process by scripting aspects of the text manipulation and extraction process, searching for substrings common to different affiliation strings, and then using simple text processing and human analysis to confirm identifications.  We placed particular emphasis on looking for substrings that appeared thousands of times, even if the individual affiliations containing those substrings may be less common.  Many affiliations fell into this category, particularly individual universities represented in multiple categories in the ADS, such as physics, astronomy, chemistry, computer science and engineering.  By targeting those substrings that occur most frequently, we can generate more matches overall, and we added them more quickly -- it was easier to disambiguate among departments and laboratories in a single university than across multiple institutions.  This work is still in progress, and we are shifting focus to the country-level to ensure more complete international coverage.

### Improvements and additions over the past year

Another reason our coverage increased is that we expanded the number of identifiers to nearly 7000 different entities and parent-child relationships, which lets us match more institutions that are easily assignable, and helps us disambiguate entities that may have multiple parents or warrant better subdivision at the department or institution level.

Many of the IDs were added simply to pick up frequently observed affiliations that were not already in the list, including (for example) medical research institutes and commercial entities involved in physics-related fields.  But a significant number of our additions have targeted specific classes of institutions: more universities and institutions from the Global South; more complete coverage of US federally-recognized Historically Black Colleges and Universities (HBCU); and Tribal Colleges and Universities (mainly in the United States).

**Institutions in the Global South**

We've increased coverage of educational and research institutions in the [Global South](https://en.wikipedia.org/wiki/Global_South) to improve the discovery and searchability of work from authors outside of historical centers of research.  Prior to this past year, our identifiers covered some of this territory, particularly in regions of the Global South with historical involvement in astronomy (South America, South Africa, India, and China).  Over the past year, we've worked to expand this coverage to include more countries and institutions involved in science that falls outside of our astronomy coverage but may be very active in related fields such as physics and materials science, computer science and engineering, or geology.  Further, researchers from these regions are often involved in collaborative science with researchers from the Global North, and thus including these institutions improves the affiliation coverage of existing literature.  We expect that the fraction of scientific literature from the Global South will increase over time (including among our core literature of Astronomy and Physics) and making these identifiers now will make it easier to keep up with these demographic changes as they happen.  Astronomy and allied sciences are used as formal means of outreach worldwide, including the Global South, with global initiatives by organizations like the IAU's [Office of Astronomy for Development (OAD)](http://www.astro4dev.org/) being a prominent example.  An additional goal for us in improving global coverage of affiliations is that the ADS can be a resource for these outreach efforts.  We hope that this improved coverage will assist both research and outreach by our colleagues world-wide.

**Historically Black Colleges and Universities (HBCUs)**

As of last year, we already had assigned identifiers for a number of Historically Black Colleges and Universities (HBCUs) in the United States, particularly those with historically strong programs in science and engineering (most notably: Hampton University in Virginia, and Howard University in Washington, DC.)  During the past year, we have expanded our coverage to include all federally-recognized HBCUs represented in the ADS literature.  The list of HBCUs and their affiliation IDs can be accessed [here](https://github.com/adsabs/CanonicalAffiliations/blob/master/historically_black_colleges_universities.tsv).  Note that we have not assigned IDs to the entire list of federally designated schools; we excluded those not represented in literature and whose focus mostly lies outside the scope of the ADS, including business, law, and divinity schools.

**Tribal Colleges and Universities (TCUs)**

We have also added affiliation IDs for a partial list of Tribal Colleges and Universities (TCUs), primarily those in the United States that are currently represented in the ADS Literature.  The list of identified TCUs can be accessed [here](https://github.com/adsabs/CanonicalAffiliations/blob/master/tribal_colleges_universities.tsv); note that this list includes only those institutions designated as tribally-controlled, and does not include those public or private non-Tribal institutions having a significant Native American population; some of those schools are present in the list as public universities, however, mainly those that have science and engineering programs.

There are comparatively few publications by authors affiliated with these colleges: Salish Kootenai College (Montana), Northwest Indian College (Pacific NW), Din&eacute; College (Arizona) and Fond du Lac Tribal College (Minnesota) have the most publications. Papers written by TCU authors and coauthors in the ADS primarily focus on topics in Environmental Science and Science Education, which are not currently part of our core literature.  These institutions may become more frequently represented if our scope widens to include more related sciences (e.g. planetary and allied literature).  We also want to ensure that their contributions are noted in existing literature, and that their contributions will be more easily tracked if these institutions increase their participation in the ADS core fields of astronomy and physics.

### Improving Affiliation Metadata: You Can Help!

Affiliation identification is an ongoing process and always will be.  One of our tasks over the past year has been to fix errors in our affiliations metadata, including badly-parsed affiliations; we focused on papers having either the longest author list or the highest citations, but we know there are still some data that needs to be fixed.  Likewise, there are many cases where an author has multiple affiliations and our representation is correct but can't be cleanly split into independent entities -- think of an author who lists "Departments of Chemistry and Physics, University of..." where we assigned IDs to both departments.  We may identify such strings as one or the other, depending on which department we searched for first.  In these cases, our ID is technically correct, but incomplete.

If you find affiliation IDs that aren't correct, please let us know.  Likewise if there are affiliations that you think should be included or better disambiguated as parents and children, please get in touch.  We would especially welcome help with the assignment and disambiguation of French UMRs and Universities, the Russian and Chinese Academies of Science, and any institutions from the Global South especially if they conduct published research in the ADS core fields of Astronomy and Physics.
