---
layout: post_scix
title: "Searching for a specific paper"
order: 1
---

### How do you search for a specific paper?
*Note: the Quick Start series is designed to get you started with the
new interface. More advanced information on searching can be found in
the [Search Syntax help page]({{ site.baseurl }}/help/search/search-syntax) and other pages in the "Making a Query"  and "Search Results" sections.*

A common task in the SciX is locating a specific paper, often for
download or for retrieval of the bibliographic data. In this case, a
user usually knows an author name (often the name of the first
author), plus a publication year. This type of search is simple, but
knowing some tips and tricks can make the process proceed more quickly
and smoothly.

### Tips
- Use fielded queries to ensure you receive the expected results.
- Use the [Classic ADS Form](https://ui.adsabs.harvard.edu/#classic-form) to automatically create fielded queries and replicate the ADS Classic look and feel. (Note: advanced and fulltext search fields are not available in the Classic Form.)
- Make use of tag auto-completion when entering fielded queries to speed up search term entry.
- It is not generally recommended that you initially search on author affiliation as a number of publishers do not provide this information to SciX. Additionally, variants on institution name may confuse the search results.

### Fielded vs. unfielded queries
The one-box search field accepts both fielded queries, where the user specifies the field being searched (such as *year:*) along with the search terms, and unfielded queries, where no search fields are explicitly specified. Unfielded queries automatically search all metadata fields; this may not produce the expected results.

We recommend that you use the field tags (e.g. *author:*) when searching for a known author and/or year of publication. However, you do not have to type the full tag or select it from the list each time you search. Auto-completion is enabled, so you can start typing the tag, then press Return to accept the auto-complete when the appropriate tag is shown. The cursor will automatically be moved to the appropriate spot within the tag to type the search term.

### Querying when author and year of publication are known
1. Click on the author tag in the Quick Field area, or start typing *author:* and press Return to accept the auto-completion.
2. Fill in the author name.
3. Do the same for the year: tag and year of publication.
4. Press Return or click the Search button to begin the search.

<figure>
   <img src="/scixhelp/img/author.gif"  class="img-responsive" alt="a short
   animated image showing querying by author and year">
</figure>

### Querying when the first author is known
Follow the same procedure as for a known author, but to trigger the first-author tag autocompletion, use the standard caret (^) operator or start typing “first author.”

Note: for a first-author search using the ^ operator, you do not have to specify the author tag. Typing *^last_name* is an abbreviation for *author:”^last_name”* and will produce the expected results.

<figure>
   <img src="/scixhelp/img/caret_firstauthor.gif"  class="img-responsive" alt="a short
   animated image showing querying by first author using the caret operator">
</figure>

### Filtering
If your search by author and/or publication year returns too many results, you can use [interactive filtering]({{ site.baseurl }}/help/search/filter) to narrow down the results instead of editing your original search query. Filtering by author or publication is often useful when a paper is known. 

<figure>
   <img src="/scixhelp/img/filter-facet.png"  class="img-responsive">
</figure>



