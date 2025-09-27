### How do you find a paper by an author with a common name?
*Note: the Quick Start series is designed to get you started with the
new interface. More advanced information on searching can be found in
the [Search Syntax help page]({% if include.ads %}../search/search-syntax{% else %}../../search-scix/search-syntax{% endif %}) and other pages in the "Making a Query"  and "Search Results" sections.*

Finding a paper by an author with a common name, especially if you have little else to go on, can be like finding a needle in a haystack. However, there are some strategies that can help.

### Exact name matching

By default, {{ include.site }} returns all relevant matches when searching for author names. For example, searching for *author:"smith, j"* will return results for J. Smith, Jane Smith, and John Smith, amongst others. To disable this synonym expansion, use the equals sign operator (=). Searching for *=author:"smith, j"* will only return results where the first initial was used in place of the full spelled-out given name. 

This can be especially helpful when a given author often uses their middle initial. For example, compare the number of results for author Y. Wang:

{% if include.ads %}<figure>
   <img src="/help/img/exact-name-1.png"  class="img-responsive" alt="Exact
   name matching query with full family name and given name
   initial. 5732 total search results.">
   </figure>{% endif %}

<br>
With those for author Y. S. Wang:

{% if include.ads %}<figure>
   <img src="/help/img/exact-name-2.png"  class="img-responsive" alt="Exact
   name matching query with full family name and given name and middle name
   initials. 233 total search results.">
</figure>{% endif %}

<br>
### Filtering results

The facets are useful when trying to narrow down a large list of search results. In addition to the author facet, which allows you to include or exclude name variations of authors, try these facets. All are located in the left-hand column, unless otherwise noted:
- Collections: by default, records from all database collections (astronomy, physics, and general) are searched from the one-box modern search interface. Limit or exclude collections here as necessary
- Refereed: limit your search to refereed or non-refereed records
- Years: located in the right-hand column, the year sliders allow you to select a publication year or range of publication years to include or exclude
- Publications: if the journal or other publication name is known, select it here
- Bib Groups: some telescopes and research institutes maintain curated listings of records relevant to their institutions; these groupings are listed here
- Data: filter based on the availability of specific links to data products, such as NASA missions, archives, SIMBAD, and NED
- SIMBAD and NED Objects: filter based on a specific object 

{% if include.ads %}<figure>
   <img src="/help/img/filter-facets.png"  class="img-responsive"
   alt="Search results with filter facets highlighted.">
</figure>{% endif %}

### I'm an author with a common name; how do I make my papers easier to find?

If you're an author with a common name, there are some strategies you can follow to make your papers more discoverable.

### Tips & Tricks
- Include your full name and at least your middle initial in author lists.
- If possible, use the same form of your name (e.g. initial vs. spelled-out form of your given or middle names) when publishing.
- If you've changed your name (given or family name) since you've begun publishing, email us at {% if include.site == 'SciX' %}<a href="mailto:help@scixplorer.org">help@scixplorer.org</a>{% else %}<a href="mailto:adshelp@cfa.harvard.edu">adshelp@cfa.harvard.edu</a>{% endif %} and we can link your name variations together. Thereafter, searching for one name variation will return publications under all linked names.

### ORCID

Create an [ORCID ID](https://orcid.org/). After obtaining your ID, [claim your papers in {{ include.site }}]({% if include.ads %}../orcid/claiming-papers{% else %}../../orcid-scix/claiming-papers{% endif %}). We'll do some basic checks to make sure you haven't claimed someone else's papers by mistake and link your ORCID ID to your papers within 24 hours. As part of this process, the papers you claim within {{ include.site }} will automatically be pushed to your ORCID record on [orcid.org](https://orcid.org/). For current and future publications, many journals (such as ApJ) now accept ORCID IDs upon submission; ORCID IDs submitted this way will automatically populate in {{ include.site }} after paper publication.

After linking your ORCID ID with your publications, users will be able to search for your papers using the syntax *orcid:XXXX-XXXX-XXXX-XXXX*. You may link to the search results using this syntax: {% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}orcid%3AXXXX-XXXX-XXXX-XXXX

### Public library
In some situations, [creating a library]({% if include.ads %}../libraries/creating-libraries{% else %}../../libraries-scix/creating-libraries{% endif %}), [making it public]({% if include.ads %}../libraries/public-libraries{% else %}../../libraries-scix/public-libraries{% endif %}), and sharing the link may be useful.
