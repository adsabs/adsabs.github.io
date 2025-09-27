### How do you build a library?
*Note: the Quick Start series is designed to get you started with the new interface. More advanced information on libraries can be found in the [Creating and Editing a Library help page]({% if include.ads %}../libraries/creating-libraries{% else %}../../libraries-scix/creating-libraries{% endif %}) and other pages in the "{{ include.site }} Libraries" sections.*

{{ include.site }} libraries allow you to save collections of papers to view later. These libraries can be private (by default) or public. In addition to viewing and sorting saved papers, you can export the collection in a variety of formats, view citations and other metrics, explore visualizations such as the paper or author networks, and check for related papers.  Libraries are a popular way to build reference lists when writing papers, or keeping one's bibliography to use in a CV.

***Note: to save papers to a library, you must be logged into your {{ include.site }} account.***

Add papers to a new or existing library directly from the search results. You can add all papers returned in the search to a library, or only a selection:

{% if include.ads %}<figure>
   <img src="/help/img/library-add.gif"  class="img-responsive" alt="a short
   animated image showing adding a paper to a library">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-library-add.gif"  class="img-responsive" alt="a short
   animated image showing adding a paper to a library">
</figure>{% endif %}

<br>
The same function is available on the abstract page of a single paper.

### Export
The contents of a library can be [exported in a variety of formats]({% if include.ads %}../actions/export{% else %}../../actions-scix/export{% endif %}), including BibTeX and AASTeX. This was designed to facilitate the development of a {{ include.site }} library as a bibliography for a paper in progress, and allow its export into the appropriate format for the journal when ready.

{% if include.ads %}<figure>
   <img src="/help/img/library-export.png"  class="img-responsive">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-library-export.gif"  class="img-responsive">
</figure>{% endif %}
 
{% if include.ads %}
### Citation helper
The [library citation helper](../libraries/citation-helper) is a unique feature specifically available to help build and maintain complete collections. It's designed to evaluate the papers already in a library and suggest related papers that should possibly also be included. 

<figure>
   <img src="/help/img/library-citation-helper.png"  class="img-responsive">
</figure>
{% endif %}

### Metrics: citations and reads
The [citations and read statistics]({% if include.ads %}../actions/analyze{% else %}../../actions-scix/analyze{% endif %}) for a library are available, similar to those available from the search results page or an abstract page. Click on the Metrics button within the library to view.

{% if include.ads %}<figure>
   <img src="/help/img/library-metrics.png"  class="img-responsive">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-library-metrics.gif"  class="img-responsive">
</figure>{% endif %}

### Visualizations: paper network, author network, word cloud
The same [visualizations]({% if include.ads %}../actions/visualize{% else %}../../actions-scix/visualize{% endif %}) available in the search results page are available within a {{ include.site }} library. 

{% if include.ads %}<figure>
   <img src="/help/img/author_network.png"  class="img-responsive">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-author_network.gif"  class="img-responsive">
</figure>{% endif %}
