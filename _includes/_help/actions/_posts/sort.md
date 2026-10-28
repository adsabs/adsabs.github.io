Results lists can be sorted in both descending and ascending order. Choose the desired sort order on the search results page using the dropdown menu at the top of the page, below the search box. {% if include.ads %}The default sort order is [Date](../actions-scix/sort#date) from most recent to oldest.{% else %}The default sort order is usually [Relevance](../actions-scix/sort#relevance) from most to least. For ADS compatibility mode, the default sort order is [Date](../actions-scix/sort#date) from most recent to oldest. You can set your personal default order in your free [SciX account](../userpreferences-scix/scix-account).{% endif %}
<br/>

{% unless include.ads %}<figure> <img src="{{site.baseurl}}/scixhelp/sciximg/scix-sortresults-layout.jpg"
	 alt="Annotated screenshot of the SciX by ADS astrophysics search results page for `first_author:&quot;van de Kamp, P&quot;`, showing 309 results. The sort menu is expanded with options such as relevance, date, author count, citation count, entry date, first author, and normalized citation count. Two blue callouts explain that the sort order defaults to relevance and that the sort direction control, beside the menu, is usually descending.."
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 650px; border: 3px solid #049DD9; border-radius: 6px;"> </figure>{% endunless %}
<br/>

<h4>Author Count</h4>
This option sorts based on a record's number of authors.

{% if include.ads %}<h4>Bibcode</h4>
This option sorts based on bibcode.{% endif %}

<h4>Citation Count</h4>
This option sorts based on a paper's number of citations.

{% if include.ads %}<h4>Classic Factor</h4>
This option sorts based on a prestige score, designed to more highly rank papers that are popular now. It is calculated via an age-normalized combination of reads and citation, and is very similar to the ranking applied to results from Classic's one-box search.{% endif %}

{% if include.ads %}{% else %}<h4>Credit Count</h4>
This option sorts based on a record's number of credits.{% endif %}

<h4>Date</h4>
This option sorts based on a paper's publication date (month and year). {% if include.ads %}It is the default sort order in {{include.site}}.{% endif %}
<br/>

<h4>Normalized Citation Count</h4>
This option sorts based on a paper's normalized citation count, which is its total number of citations divided by its number of authors. 
<br/>

<h4>Entry Date</h4>
This option sorts based on a paper's entry date in the {{ include.site }} database.
<br/>

<h4>First Author</h4>
This option sorts based on the last name of a paper's first author.
<br/>

<h4>Read Count</h4>
This option is a measure of <b>recent popularity</b>. It sorts on the 90-day read count of a paper: the number of times a paper has been accessed in {{include.site }} or on arXiv in the last 90 days.

{% if include.ads %}<h4>Score</h4>
This option is currently a combination of two factors: the first is the raw search score, or how well the results match the search terms. For unfielded searches, or those that don't use search tags, commonly searched fields such as author and publication year are more heavily weighted in determining the score. The second factor is a boost factor for more highly read and cited papers. This boost factor is designed to more highly rank papers that are relevant and popular now and is calculated via an age-normalized combination of reads and citation.

{% else %}<h4>Relevance</h4>
This option is usually the default sort in {{include.site }}, although ADS compatibility mode uses [Date](../actions-scix/sort#date) as its default sort order. Relevance sorts records based on a combination of four factors. 
- The Lucene score from the search enginetakes into account how well a given result matches [the search terms](../search-scix/search-syntax). Matches to certain fields are valued more highly than others; a match to an author name, for example, is weighted more highly than a match to a keyword. For unfielded searches, or those that do not use search tags, commonly searched fields, such as author and publication year, are more heavily weighted in determining the score (for example, see the weights within the "qf" parameter [here](https://github.com/adsabs/montysolr/blob/main/deploy/adsabs/server/solr/collection1/conf/solrconfig.xml)). 
- A popularity boost is applied to articles that are more highly cited or read. An age-normalized cite boost and recency boost are in development that will jointly replace this factor. (For more, see the  [cite_read_boost](https://github.com/adsabs/montysolr/blob/main/deploy/adsabs/server/solr/collection1/conf/schema.xml).)
- A document-type boost is applied so that articles are returned more highly than other documents, such as conference proceedings or books. (For details, see the [DOCTYPE_BOOST_FACTORS](https://github.com/adsabs/ADSBoostPipeline/blob/main/config.py).)
- A disciplinary boost is applied (defined as  the [COLLECTION_RANKINGS](https://github.com/adsabs/ADSBoostPipeline/blob/main/config.py)), so that results from collections more applicable to the selected discipline (in the top-left menu) are returned more highly. For example, if "Astrophysics" is selected, results from the astrophysics subcollection are weighted most, while articles from physics, general, planetary science, heliophysics, and earth science, in that order, are weighted with gradually decreasing boosts. (Astrophysics, planetary science, and heliophysics are developmental subcollections of the astronomy collection.)
Feedback regarding both well-ranked and poorly ranked results would be welcome.
  {% endif %}
