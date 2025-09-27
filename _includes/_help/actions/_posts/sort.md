Results lists can be sorted in both descending and ascending order. Choose the desired sort order on the search results page using the dropdown menu at the top of the page, below the search box.
<br/>

<h4>Author Count</h4>
This option sorts based on a record's number of authors.

{% if include.ads %}<h4>Bibcode</h4>
This option sorts based on bibcode.{% endif %}

<h4>Citation Count</h4>
This option sorts based on a paper's number of citations.

{% if include.ads %}<h4>Classic Factor</h4>
This option sorts based on a prestige score, designed to more highly rank papers that are relevant and popular now. It is calculated via an age-normalized combination of reads and citation, and is very similar to the ranking applied to results from Classic's one-box search.{% endif %}

<h4>Date</h4>
This option sorts based on a paper's publication date (month and year).
<br/>

<h4>Entry Date</h4>
This option sorts based on a paper's entry date in the {{ include.site }} database.
<br/>

<h4>Read Count</h4>
This option is a measure of <b>recent popularity</b>. It sorts on the
90-day read count of a paper: the number of times a paper has been
accessed in {{ include.site }} or on arXiv in the last 90 days.

<h4>{% if include.ads %}Score{% else %}Relevancy{% endif %}</h4>
This option is currently a combination of two factors: the first is the raw search score, or how well the results match the search terms. For unfielded searches, or those that don't use search tags, commonly searched fields such as author and publication year are more heavily weighted in determining the score. The second factor is a boost factor for more highly read and cited papers. This boost factor is designed to more highly rank papers that are relevant and popular now and is calculated via an age-normalized combination of reads and citation.
