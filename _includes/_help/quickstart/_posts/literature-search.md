### How do you start a literature search in {{ include.site }}?

*Note: the Quick Start series is designed to get you started with the new interface. More advanced information on searching can be found in the [Second Order Queries]({% if include.ads %}../search/second-order{% else %}../../search-scix/second-order{% endif %}){% if include.ads %}, [Citation Helper](../libraries/citation-helper),{% endif %} and [Article View]({% if include.ads %}../actions/article-view{% else %}../../actions-scix/article-view{% endif %}) help pages and other pages in the "Making a Query" and "Search Results" sections.*

Starting research on a new topic can be tricky, especially when you
don't know which papers you should be reading. How do you make sure
you've covered everything and are fully up to speed on your background
reading? {{ include.site }} has some tools to help. We've divided this quick start
guide into three sections, depending on the starting point: starting
from an individual paper, from a broad topic or keyword, or from an
existing library. Read on for more.

### Starting from an individual paper

If you have one or two reference or other papers you're starting your
search with, there are a few sources of potentially related papers. To
begin, go to the abstract page for the paper. In the left column are
links for the Citations, References, and Co-Reads. Citations list
papers that cite the given paper, while References are cited in the
given paper and listed in its bibliography. Exploring both of these is
a good starting point. Also investigate papers listed under
Co-Reads. These are papers that users who read the paper in question
also read; they may be related to the original paper in a variety of
ways and can provide interesting insights. By default, the Citations,
References, and Co-Reads lists are sorted in reverse chronological
order. To re-sort or filter the results, click the button to view the
results in a search results page.

{% if include.ads %}<figure>
   <img src="/help/img/coreads_1.png"  class="img-responsive" alt="an
   image showing the Co-Reads links on the abstract page">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-coreads_1.gif"  class="img-responsive" alt="an
   image showing the Co-Reads links on the abstract page">
</figure>{% endif %}
{% if include.ads %}<figure>
   <img src="/help/img/coreads_2.png"  class="img-responsive" alt="an
   image showing the Co-Reads listing">
   </figure>{% endif %}
   <br>
*Abstract page and Co-Reads for a canonical WMAP paper. Click "view
   this link in a search results page" to re-sort and filter the
   related papers.*

### Starting from a topic
If you want to know about a general topic (e.g. gravitational waves or
coronal mass ejections), there are three main methods to find related
papers: sorting, second-order search operators, and the paper network.

**Sorting**

The sort options available from the search results page are a natural
first step in exploring by topic. For many searches, the default sort
option is by publication date, with most recently published articles
first. However, other sorting options may be more useful. For example,
a search for *M31* returns most recently published articles
first. Sorting by **citation count** instead returns more highly cited
articles first. These results can be narrowed by publication year or
by other filters in the left and right columns. For a measure of more
recent popularity, try sorting by **read count**: this sorts the
results based on the papers most read or downloaded over the last 90
days.

**Second-order search operators**

The [second-order search operators]({% if include.ads %}../search/second-order{% else %}../../search-scix/second-order{% endif %}) are usable in the one-box
search box and are available as an autocomplete search term in the
search box, or for selection from the search term menu above the
search box. There are three main second-order search operators that
may be useful for literature searches:

* **trending()** This search operator returns papers recently read by
  people who are interested in the subject. For example, a search for
  M31 would return a set of papers about the Andromeda galaxy. A
  search for *trending(M31)* would return the papers recently read by
  people who had also read papers about M31. The results are returned
  sorted by score order, with the most relevant results first. Note
  that the co-reads for an individual article, described above, makes
  use of the trending() operator.

* **reviews()** This search operator returns papers that frequently
  cite relevant papers. For M31, *reviews(M31)* would return papers
  that cite many of the most relevant papers. Papers in this group may
  include (but are not necessarily) review articles or articles with
  in depth introduction sections.

* **useful()** This search operator returns papers frequently cited by
  relevant papers. Returning to Andromeda, a search for *useful(M31)*
  would return papers frequently cited in the most relevant M31
  papers. The results from this operator are generally papers about
  tools, methods, or data sets relevant to a field.

{% if include.ads %}<figure>
   <img src="/help/img/second-order.png"  class="img-responsive" alt="diagram showing use of the second order operators">
   </figure>{% endif %}
   <br>

**Paper Network**

The [Paper Network]({% if include.ads %}../actions/visualize#paper-network{% else %}../../actions-scix/visualize#paper-network{% endif %}), available from
the Explore dropdown menu in the upper right on the search results
page, is a useful tool for exploring subtopics within a larger
search. Results from a search are sorted into subgroups based on
shared references between those records. Clicking on one of the
resulting subgroups (the colorful wedges in the visualization) shows
the papers belonging to that subgroup. At the end of the list of
subgroup papers is a short list of papers that were highly cited by
the papers within the given subgroup but that may or may not have been
included in the original search. This list of potentially relevant
papers is similar to the useful() papers above.

Note that, by default, the paper network is built from the top 400
papers in a list of results and can only be extended to include up to
1000 papers in the results list. Therefore, it is best used with a
list that has been been previously narrowed to a few hundred papers.

{% if include.ads %}<figure>
   <img src="/help/img/paper-network-suggested-papers.png"  class="img-responsive" alt="an
   image showing Paper Network with suggested papers">
   </figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-paper-network-suggested-papers.png"  class="img-responsive" alt="an
   image showing Paper Network with suggested papers">
   </figure>{% endif %}
   <br>
*Paper network for a search for refereed papers about the MUSE
   instrument. In this subgroup, containing instrumentation papers,
   the suggested papers at the bottom contain highly relevant
   non-refereed conference proceedings and other papers.*

### Starting from a library

If you've started to assemble a library organized around a given topic
(e.g. for a paper in progress), there are tools available to ensure
you haven't forgotten any relevant references. In addition to the
paper suggestions offered by the in-library
Paper Network,
{% if include.ads %} the [Citation Helper](../libraries/citation-helper) is
designed to find related papers. It finds up to 10 papers that are
either cited by or that cite the papers in the library, but are not
contained in the library. Its results are similar to a combination of
the useful() and reviews() operators above. The suggested papers are
sorted by score, with the most relevant papers first. If you have
write access to a library, you can select desired papers and add them
to your library within this tool.
{% else %} you can use the Explore menu to discover related papers and add them to your library.{% endif %}

{% if include.ads %}
<figure>
   <img src="/help/img/citation-helper.png"  class="img-responsive" alt="an
   image showing the Citation Helper within a library">
   </figure>
   <br>
*Example of the Citation Helper for the public library containing [refereed papers about {{ include.site }}]({{ site.ads_base_url }}/#/public-libraries/aI9-ox_2RNeZK-gm-4DpVQ). The top suggested papers are papers about {{ include.site }} that are closely related to the papers in the library via citations and references.*
{% endif %}
