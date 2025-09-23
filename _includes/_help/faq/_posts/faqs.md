# Frequently Asked Questions (FAQs)

[Searching](#searching) •
{% if include.ads %}[Submitting Grant Applications](#submitting-grant-applications) •{% endif %}
{% if include.ads %}[Transitioning from Classic](#transitioning-from-classic) •{% endif %}
[{{ include.site }} Libraries](#{{ include.site | downcase }}-libraries) •
[ORCID](#orcid) •
[Data and Curation](#data-and-curation) •
[Database Coverage](#database-coverage) •
[Other](#other)

## Searching

##### Q: Typing a fielded query for an author query (e.g. author:"huchra, j." or author:"^huchra, j.") or clicking on the search term dropdown is a lot of work.
There are two options. First, a first-author query can usually be entered as *^huchra, j.*---the *author:* tag is not necessary for first-author searches (note, though, that this format does not work well for authors with multi-part last names). Second, many search tags will autocomplete in the search box. Begin typing the search tag, such as *author:*, and either press the return key or the right arrow key when the tag autocompletes to accept it.

##### Q: Is it possible to search using the second author of a paper?
Positional searches are supported. To search for a second author, use *pos(author:"huchra,j.",2)*. See the Help page for [positional field searches]({% if include.ads %}../search/positional{% else %}../search-scix/positional{% endif %}) for more info.

##### Q: How do I exclude a term from my search?
Either prepend a negative sign (e.g. *-doctype:"proposal"*) or use the Boolean operator NOT (e.g. *NOT doctype:"proposal"*) while searching. See the Help page for [Boolean queries]({% if include.ads %}../search/search-syntax#combining-search-terms-to-make-a-compound-query{% else %}../search-scix/search-syntax#combining-search-terms-to-make-a-compound-query{% endif %}) for more info, paying special attention to the note on when differences in behavior between NOT and the negative sign may arise.

##### Q: Records are missed when searching from the 1st of one month to the end of the current month, e.g. pubdate:[2016-01-01 TO 2016-06-30].
Records do not generally have a publication day, just a month and year. The missing day is set to 00 (e.g. January 2016 is set to 2016-01-00). Searches starting on the 1st of a given month will exclude all records with publication days of 00. It is preferable to not use a day when searching over a publication date range; specifying only a month will include records with publication days of 00. This is similarly true for the small number of records missing publication months. Searches beginning in January of a given year may miss records with publication months of 00. To search for records from the first half of the year, employ a search term such as *pubdate:[2016 TO 2016-06]*.

##### Q: How can I search for an acronym that is the same as a common word?
{{ include.site }} treats search terms entered in all caps as acronyms and will only return records that contain the all caps acronym form, not the lowercase common word form. In addition, some acronyms will auto-expand in the search (e.g. searching for "ADS" will find both "ADS" and "Astrophysics Data System" but will ignore "ads").

##### Q: My new paper is not appearing in {{ include.site }}.
New papers appearing on arXiv are ingested daily, though there may be a delay of one day for them to appear in the new {{ include.site }}. Published articles are ingested as the publisher provides them on a weekly basis, generally over the weekend.

##### Q: Searching for an author's name plus their affiliation doesn't give a complete list of results.
Not all publishers provide authors' affiliations for search indexing, even if the affiliations are listed in the PDF or HTML form of the article itself. Also, note that searching using the *aff:* search tag searches the raw affiliation text provided by the publisher, such that searching for "Harvard-Smithsonian Center for Astrophysics" or for "CfA" will give different results. Use the *inst:* search tag to search the canonical affiliations; more information is available on the [Search Syntax help page]({% if include.ads %}../search/search-syntax{% else %}../search-scix/search-syntax{% endif %}).

##### Q: How do I build a URL using a known identifier of a paper?
You can access the abstract page of a known paper by inserting an identifier (bibcode, DOI, arXiv ID) into a URL, following a set pattern. The base URL is `{% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/<identifier>`, where `<identifier>` can be one of the following:
* bibcode, e.g. [{% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/2008ApJ...689.1044G]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/2008ApJ...689.1044G)
* DOI, e.g. [{% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/10.1086/592738]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/10.1086/592738)
* arXiv ID in two ways, e.g.:
    * [{% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/arXiv:0808.2870]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/arXiv:0808.2870)
    * [{% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/0808.2870]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/0808.2870)

{% if include.ads %}## Submitting Grant Applications
##### Q: My NSF grant application requires that I provide a list of all of my recent co-authors. Can {{ include.site }} provide that list?
We have a tool specifically for this purpose: the "Author Affiliation" report option on the Export menu (accessible from the search results page). For more, see the [Author Affiliation help page](../actions/author-affiliation).

##### Q: My NSF application requires I build a CV via SciENcv. Can {{ include.site }} help with that?
There are two options to use {{ include.site }} to help build your SciENcv:  
1. The first option is to export your publications from {{ include.site }} in the [RIS format](../actions/export). The SciENcv citations manager will then allow you to import your citations in this format.  
2. The second option is to link your ORCID account with SciENcv and import your citations from there. You can use {{ include.site }} to [add citations to your ORCID profile](../orcid/claiming-papers), then link your updated ORCID profile to your account in SciENcv.{% endif %}

{% if include.ads %}## Transitioning from Classic
##### Q: How do I transfer a private library from Classic to the new {{ include.site }}?
Link your Classic account to your the new {{ include.site }} account and [use our import tool to transfer your library](../libraries/legacy-importing#importing-libraries).

##### Q: I have some links to Classic pages on my website - do I need to update all of these to the new {{ include.site }} links?
Nope! Existing Classic URLs now redirect to the corresponding URLs in the new {{ include.site }}.

##### Q: Where do I find the utility ***Get citation lists for selected articles*** and similar second order queries?
In general, the function **Reviews** in the **Explore** menu will generate the same list of publications as selecting all records in Classic and clicking on the button *Get citation lists for selected articles*. The only difference is the fact that the new {{ include.site }} does not show the frequency, but the results are sorted by the number of cites to the original set (when sorted by score).

The new function **Useful** can be used in a similar way to generate the same results you would get the with button *Get reference lists for selected articles* in the old {{ include.site }}. When "score" is selected for sorting, the records are sorted by the number of cites by the original set.

The **Co-reads** function corresponds with *Get also-read lists for selected articles*.{% endif %}

## {{ include.site }} Libraries
##### Q: The number of papers listed in the header of my library differs from the actual number in the library.
When you create or update your library, the bibcodes of the new records are stored in a database. Currently this list does not get updated when records are merged or deleted within the {{ include.site }} index, rather these changes get reflected at display time of the contents of an {{ include.site }} Library.

## ORCID
##### Q: I just claimed some papers using my ORCID ID but they're not showing up in the public search.
ORCID claims can take up to 24 hours to be processed and approved in our system. Please check the search again tomorrow.

##### Q: I have records on my ORCID profile that do not appear in {{ include.site }}.
First, if you haven't yet, you'll need to log into ORCID in {{ include.site }}, using the ORCID dropdown menu in the top bar. If you've published under multiple names, you'll need to enter these on your [ORCID settings page]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/user/settings/orcid). Papers on your ORCID profile also need to exist in {{ include.site }} and need to have an identifier we recognize (generally a bibcode, arXiv ID, or DOI). Finally, if you've recently entered or updated these records, note that it can take up to 24 hours for them to be registered in our system.

## Data and Curation
For data and curation questions, see our [data and curation FAQs]({% if include.ads %}../data_faq/data-faq{% else %}../data_faq-scix/data-faq{% endif %}).

## Database Coverage
##### Q: How complete is {{ include.site }}?
{% if include.ads %}{{ include.site }} aims to be the complete and authoritative source for the astrophysics literature. This includes not only published refereed articles and arXiv e-prints, but also the gray literature, comprised of conference proceedings, books, proposals, etc. We aim to not only index these resources but also enrich them with links to data or other resources when available. We also index published refereed papers and conferences that are likely to be cited by the core astrophysics literature, such as papers from physics, geophysics, and planetary science. If a record is missing, please let us know via our [Submit Abstract Form]({{ site.ads_base_url }}/feedback/correctabstract).{% else %}{{ include.site }} aims to be a comprehensive source for scientific literature. This includes published refereed articles and arXiv e-prints, as well as conference proceedings, books, and other scholarly works. We aim to not only index these resources but also enrich them with links to data or other resources when available. If a record is missing, please let us know via our [Submit Abstract Form]({{ site.scix_base_url }}/feedback/correctabstract).{% endif %}

##### Q: Why are citations from an arXiv record missing? Why is an arXiv record missing its references?
For arXiv sources, we attempt to extract references from the full text and from there create citations. However, as papers can be submitted to the arXiv with a bibliography in a non-standard format, this process is not always successful. When the published version of an arXiv paper becomes available, we will use the publisher-provided reference list and disregard the arXiv reference list.

##### Q: For how many records is the full text available for searching?
The full text is available for searching for many records, including most recent publications. You can search for records with full text using the query [has:body]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q=has:body{% else %}/search?q=has:body{% endif %}). Note that the searchable full text resides in our database and is separate from the links to publisher or arXiv sources; not all records with source links have searchable full text.

## Other
{% if include.ads %}##### Q: I'm trying to use the new interface but I'm getting a message about JavaScript / it's stuck on a loading screen.
This issue is commonly seen when users have JavaScript turned off in their browser, or they're using security software or browser plugins (such as NoScript) that block JavaScript, or are accessing the site from a network that blocks content from certain domains (e.g. google.com).  The full version of the new {{ include.site }} requires JavaScript in order to function (note: the basic HTML version, linked from the bottom of the search page or from the loading page when JavaScript is not detected, offers limited functionality without requiring JavaScript).  At an absolute minimum you must have JavaScript turned on.  Further, if you have any security settings or plugins that require sites to be whitelisted before running JavaScript, you must whitelist two domains for basic functionality: harvard.edu, and google.com.{% endif %}

##### Q: What internet browsers are supported by {{ include.site }}?
We support all current versions (within the last 5 years) of Chrome, Firefox, Safari, and Edge. We also support Internet Explorer 11. This includes Firefox ESR (extended service release) versions, but does not include versions of any browser newer than 5 years old that have been officially retired.

##### Q: How should I acknowledge {{ include.site }}?
If you wish to acknowledge us in a publication, kindly use a phrase such as the following: {% if include.ads %}"This research has made use of the Astrophysics Data System, funded by NASA under Cooperative Agreement 80NSSC21M00561."{% else %}"This research has made use of SciX, a scientific literature search and discovery platform."{% endif %} If you are using the {{ include.site }} as a tool for bibliometric studies, please make sure you have an in-depth understanding of the system, its features and limitations, by reading and citing as appropriate the relevant published literature about {{ include.site }} ([refereed]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/#/public-libraries/aI9-ox_2RNeZK-gm-4DpVQ), [non-refereed]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/#/public-libraries/iETdWs2pSGajhFBI30X3UQ)).

{% if include.ads %}##### Q: Do you have any mirror sites? 
No, once we moved our site to the cloud in 2018, we no longer host mirror sites. See our [mirror policy page](../policies/mirrors) for more information.{% endif %}
