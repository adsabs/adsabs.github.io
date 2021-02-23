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

Authors from a given institution may publish their work in a variety of journals and other venues, all of which may have separate editorial requirements.  Likewise, publication in a less formal venue such as a conference proceeding may have no restrictions on formatting or fielding (or even inclusion) of affiliations, and authors are free to use whatever identifier they choose.  This is (sometimes) straightforward for a human being to interpret, but there is enough variation in how departmental and institutional affiliations are given by different authors over time that searching them as a simple text field will produce incomplete and sometimes inaccurate results.  The ADS has developed a curated database of affiliation identifiers where we have collected all of the various text representations of a given affiliation and assigned them an affiliation identifier where it is possible to do so unambiguously.  This powers our affiliation search feature, allowing you to search and select literature on the basis of affiliation data.  With ADS, you have two ways to use affiliation data in your searches: through the affiliation search filter, and directly in your search queries.  We show you how below.

### Using affiliations in your literature search

Affiliation filtering

The ADS interface enables you to refine your search using filters, located on the left hand side of the default view of search results.  When you search for anything in ADS, your search results also automatically populate all of the search filters which let you refine your results.  There are several filters including: author, collection, keywords, and institutions.  The Institutions filter is where you use the affiliation data to refine your searches.  For example, if you search for “gravitational waves” and “year:2020” you’ll get a list of over 3,300 papers published in the year 2020 that contain the phrase “gravitational waves”.  If you click “INSTITUTIONS” in the left column, you’ll get an abbreviated list of the most-frequently seen affiliations among those 3,300 papers:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_1.jpg" />
</div>
<br>

If you select one of those affiliations (by checking the box to the left), you’ll see the following:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_2.jpg" />
</div>
<br>

Note especially the “limit to” and “exclude” options; if you select “limit to”, your original set of results will be refined to just those 155 papers having one or more coauthors from the Max Planck Institute:

<div class="text-center">
<img class="img-thumbnail" src="{{ site.baseurl }} /blog/images/blog_2021-03-01_affil_drop_3.jpg" />
</div>
<br>

Now, you can use other filters to refine your search, including the institution filter itself.  Clicking “INSTITUTIONS” again will give you a list of affiliations seen among the new result set, the list of 155 papers with an MPI coauthor.  In this way, you could (for example) search for papers with collaborators from two specific institutions, or determine which institutions collaborated most often on gravitational waves in 2020.



Searching affiliations

You can also use affiliations directly as part of your search, just as you can other metadata fields like title, year, and bibstem.  We have a number of different keywords with which to access affiliations:  

* aff: This field holds the raw affiliation string -- whatever text is supplied to us by a publisher or author as representing one or more authors' affiliation or host institution. (e.g. aff:"SRON").  Use this if you're looking for a specific string (rather than a specific identifier) in an affiliation; it doesn't use the curated identifiers as part of the search.

* aff_id: This field gives you access to the affiliation identifications curated by the ADS, including synonyms with other institutional identifier systems like GRiD and ROR.

* aff:














### OLD, DELETE


### Using affiliations as part of your search strategy: Direct affiliation searches

Affiliations in the ADS have been indexed in several different fields, with the intention of allowing multiple use cases. We have currently assigned identifiers with parent/child relationships, such as an academic department within a university. A child may have multiple parents, but we restrict a child from having children of its own. This has required a few modifications to remain useful. For instance, so that University of California schools can identify departments, we have assigned them a parent status, even though the "University of California System" should really be the parent level.  Likewise, NASA's Goddard Space Flight Center is at a parent level, as are France's CNRS institutions to allow for further subdivision.  Further work on a schema to allow more complex relationships between institutions is under development in conjunction with work by the [ROR Community](https://ror.org/).

We've recently changed the way we index affiliations by introducing a new search field: "affil".  Affil combines all of the available affiliation data -- raw strings, canonical strings, IDs, and abbreviations into a single, searchable field.  It's intended to be a more comprehensive search of both raw strings and the enriched institution asssignments we've applied to our data.  So for example, searching for [affil:&ldquo;UCB"](https://ui.adsabs.harvard.edu/search/fl=identifier&q=affil:"UCB") will return papers where 'UCB' matches some part of the raw affiliation, but *also* return affiliations we've matched to the University of California at Berkeley.  Because "UCB" is used by some authors to abbreviate other universities (for example "Catholic University of Brasilia, Brazil" or "University of Colorado, Boulder"), the affil search also finds these, but they can be de-selected in the affiliation facet.

In addition to this new field, we've maintained the original search terms for affiliations that we deployed last year:

* aff: raw affiliation string, searchable word-by-word

* aff_id: a string containing one or more of the affiliation IDs listed in our [mapping of organizations to identifiers](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv).  This field will soon also accept 9-digit ROR IDs.

* inst: the abbreviated institution name (e.g. "U Adelaide") listed in our [mapping of organizations to identifers](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv).

So, you could search for [aff:Harvard](https://ui.adsabs.harvard.edu/search/fl=identifier&q=aff:"Harvard") and get back all affiliations that contain Harvard in the affiliation string -- including "Harvard Street".  To ensure you get only the University, you could search for [aff:&ldquo;Harvard University"](https://ui.adsabs.harvard.edu/search/fl=identifier&q=aff:"Harvard%20University") but that would return only affiliation strings with that exact phrase, excluding "Harvard Univ.", "Harvard U", etc.  Better would be to use the identifier for Harvard University by searching [aff_id:A00211](https://ui.adsabs.harvard.edu/search/fl=identifier&q=aff_id:A00211).  This returns all affiliations which contain Harvard University at the parent level. Best yet would be to search by institution, [inst:&ldquo;Harvard U"](https://ui.adsabs.harvard.edu/search/fl=identifier&q=inst:"Harvard U")  which returns affiliations which contain Harvard University at the parent level, plus all affiliations for all of Harvard University's children.

### How we got here: the curation and pipeline process

**The human element: curation**

Production of the initial affiliation database began with two human-generated projects: creating a set of institutional identifiers, and matching affiliation metadata to these identifiers as precisely as possible.  Both of these were done almost entirely by ADS Lead Curator Carolyn Grant.

There are hundreds of thousands of organizations around the world, and in principle any institution or business can be assigned an identifier.  The overwhelming majority of these are not relevant to ADS, so the first task was to establish a list of institutions that match affiliations in our metadata.   The current list stands at about 6600 departments, organizations, and parent institutions in all geographic regions of the world.  Many of these institutions are also tagged with a second identifier, namely the identifier of the parent institution.  For example, the parent institution of the Department of Physics at the University of California at Irvine is "University of California at Irvine".  For now, our affiliations have two levels only, so in this example, we do not assign "The University of California System" as the parent of UC Irvine, but our list of identifiers includes System identifiers in cases of ambiguity (e.g. a publisher-provided affiliation "Univ. of Cal." with no city or other unambiguous identifying information).

The second, and by far most time-consuming, part of this process was the initial classification of millions of individual affiliation strings from the ADS bibliographic database.  This involved both extraction of the author affiliation strings from the database and identification of the institution represented by that string.

As an example, a typical string might be "Physics Dept., UC Irvine" which would correspond to the affiliation of "Department of Physics, University of California at Irvine" and then assigning this string its corresponding alpha-numeric ID.  The process sounds straightforward, but extraction of all strings relating to "Department", "Physics", "University of California", and "Irvine" can be long and tedious, especially if you're searching thousands of possible strings.  There are ways to speed that process (e.g. by searching for "Irvine" and "Physics" in all strings, and then looking through just that set of results), but at the beginning it was an entirely human-curated process.  Complicating things is the fact that many authors are affiliated with more than one institution, for example "Astronomy Dept., U. Texas -- Austin, and UNAM-Morelia".  Publishers -- especially smaller publications and conference proceedings -- rarely use standardized text for affiliations, and even more rarely list multiple affiliations in separate entities in their metadata.  So the curation process also involves splitting those multiple affiliations and then characterizing each affiliation separately.  That process was repeated over and over for the 6600 affiliations that each occasionally had thousands or tens of thousands of different non-unique publisher-provided strings.

Cleaning the data turned out to be more of an art than a science.  There exist curation tools for cleaning up messy data -- the one we used almost exclusively was Open Refine (called Google Refine at the time).  This allowed bulk substitutions, expansions, translations and more.  But cleaning is not enough.  For example, changing all instances of "UC Irvine" to "University of California Irvine" may seem like a good idea, except that new instances of "UC Irvine" are likely to continue coming in.
		 	 	 		
**Automated Pipelines: assigning identifiers to specific author-affiliation-bibcode entities**

With the initial set of affiliation strings identified we, along with ADS backend programmer Stephen McDonald, designed an automated pipeline to add canonical affiliation identifiers to our database of 15 million references.  It's a simple process.  First we normalize all of the strings with all uppercase letters, remove spaces and a subset of punctuation marks not needed for disambiguation, which results in a reduced number of matching strings; often, strings will be identical without punctuation, such as strings with "... U.S.A." and "... USA".  We then assign the strings to a dictionary, where the strings themselves are the keys, and the identifiers are the values.  If a normalized incoming string matches a key in the dictionary, we assign it the appropriate aff_id, and the record with augmented affiliation data is sent back to our database of metadata for use in the next reindexing process.

We've entirely automated the process, so once the dictionary of affiliation strings and matched identifiers is created, it's a hands-off component of our metadata processing pipeline.  We update dictionaries about once a month, and occasionally more often if we have a large batch of incoming unmatched affiliation strings.  This process is similar to the first curation step, with the only difference being that we prioritize strings according to how many times they appear.  For example, if we receive a number of papers from collaborations with hundreds or thousands of authors *and* their affiliations don't exactly match our dictionary, we need to add them.  Early on in this process, we came across strings that had many thousands (and sometimes tens of thousands) of occurrences, but the latest batch of unclassified strings appear fewer than 550 times in our entire database. This maximum frequency drops each time we create a new dictionary.

However, we're getting close to the limit of what we can do with human classification without lots of effort.  Our most recent pass through our metadata has just over 4.8 million unique unclassified strings yielding a total of 16.6 million unclassified affiliations.  There are about 6000 unclassified affiliations that appear 100 times or more in the metadata and assigning them aff_ids would provide a lot of new information.  However, over 65 percent of unclassified affiliations occur fewer than 10 times, and **13 percent of unmatched affiliation strings only appear once in all of our affiliation metadata**.

<div class="text-center">
        <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-01-15_matched.png" width="50%" /><img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-01-15_unmatched.png" width="50%"/>
<em>Left: Nearly 90 percent of matched publisher-provided affiliation strings in our database appear at least 10 times. Right: The number of unmatched affiliation strings is dominated by those appearing fewer than 10 times.</em>
</div>
<br>

This is too much to work through by hand, but it represents valid affiliation data for millions of author-affiliation pairs. For the unmatched affiliations that occur fewer than 100 times, we're using machine learning techniques to try and assign IDs.  For now, we're using scikit-learn tools to try and match unknown strings to IDs. Specifically, we're using scikit-learn's feature_extraction tools for analyzing the known affiliation strings, and the SGDClassifier to generate models.  We then pass the unknown strings through the model and extract both a best match and a confidence estimate.  The process can be very memory intensive because of the large number of classes -- nearly 6600, one for each aff_id.  A typical data set of 25,000 unmatched strings takes about an hour on a modest workstation (Apple iMac with an Intel i5 processor and 24 GB of memory).  

We've found the process is reliable to the limits of the input dictionary, and also found that it's much more of a data curation problem than a machine learning problem.  Curation of a machine learning model isn't trivial.  It's very sensitive to both errors in assigned IDs (which are rare but do occasionally occur) and to ambiguous affiliation strings or strings that can't be split cleanly.  Examples of the latter include affiliation strings that include (say) both a national laboratory affiliation and a university one (e.g. the Italian INFN centers, NIKHEF member institutions, and US DOE Laboratories), or cases where we have an incomplete mapping of all parent-child relations (e.g. where we have an ID for a university's Department of Physics, but not a Department of Statistics or Materials Science).

For now, we're using machine learning to assist with curation, but we're not yet confident enough to pass it an affiliation string and guarantee it returns the correct ID; it's not (yet) a part of our hands-off pipeline.  It's an ongoing process of improvement, and always will be as new metadata keeps coming in.

### What's next?

Searching ADS by affiliation is already very useful for helping with disambiguation, and for helping build institutional publication lists.  We hope to make it even more powerful by integrating our system with [ROR](https://ror.org) and integrating publisher-specific identifiers in our workflow.  We are actively working with other projects to extend ROR identifiers (which are assigned one per institution) to the department level.  In addition, we hope to improve the user experience by coupling affiliation with authors, adding hover-over expansion of abbreviations, and implementing auto-complete with the institution search.  As always, we welcome feedback and corrections.
