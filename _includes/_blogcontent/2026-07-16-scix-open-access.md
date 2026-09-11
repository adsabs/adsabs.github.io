NASA has long been one of the most visible leaders in providing Open Access (OA) to scientific data and publications. Supporting this goal has long been a core tenet of the Astrophysics Data System (ADS) and is a crucial part of the mission of the Science Explorer (SciX).

Part of how SciX supports this goal is to prioritize the inclusion of open access journal content and other OA publications, such as preprints and theses. But another, equally important part is to ensure that SciX users can access OA content wherever it exists.

To that end, the SciX team has recently rolled out [links]{% if include.ads %}(https://ui.adsabs.harvard.edu/search/q=esources%3Apmc*){% else %}(https://scixplorer.org/search?q=esources%3Apmc*){% endif %} to the full text of articles in the [PubMed Central Open Access Subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/) and the [Europe PMC Open Access Subset](https://europepmc.org/downloads/openaccess).

[PubMed Central](https://pmc.ncbi.nlm.nih.gov/) (PMC) is a free full-text archive of biomedical and life sciences journal literature, hosted by the U.S. National Institutes of Health's National Library of Medicine (NIH/NLM). As of July 2026, it contains records for over 12 million articles. PMC makes several [datasets](https://pmc.ncbi.nlm.nih.gov/tools/textmining/) available for automated retrieval, one of which is the [Open Access Subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/), containing nearly 8 million articles. The PMC Open Access Subset includes the full-text of articles and preprints made available under Creative Commons or similar licenses that allow redistribution and reuse.

Likewise, Europe PMC is an archive that provides access to life sciences literature, including content from PMC and several other collections of published and preprint articles. It is hosted by EMBL’s European Bioinformatics Institute (EMBL-EBI), and contains more than 48 million records. Like PMC, Europe PMC also provides an Open Access Subset, containing nearly 8 million articles.

When a publication in the SciX collection is also in either of these OA collections, you will see a link to that record, allowing you to easily access the full text. Most of these records have accompanying PDFs, to which SciX also links. When you are viewing a record in {% if include.ads %}ADS{% else %}SciX{% endif %}:

{% if include.ads %}
* Find the Full Text Sources box in the top right of the page
* Note the icons to the right of the text that says PubMed Central or Europe PMC
* Click on the HTML icon to link to the record for this item in PubMed Central or Europe PMC, or
* Click on the PDF icon (when available) to download the full text of this item

<img src="{{site.baseurl}}/blog/images/blog_2026-07-16_ads_pubmed_screenshot.png" 
	 alt="Screengrab of the ADS interface showing a record view page with a right-hand menu that provides full-text links, one of which is a link to the PubMed Central source."
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 750px;">
{% else %}
* Find the Full Text Sources box in the top left of the page
* Note the icons to the right of the text that says PubMed Central or Europe PMC
* Click on the HTML icon to link to the record for this item in PubMed Central or Europe PMC, or
* Click on the PDF icon (when available) to download the full text of this item

<img src="{{site.baseurl}}/blog/images/blog_2026-07-16_pubmed_screenshot.png" 
	 alt="Screengrab of the SciX interface showing a record view page with a left-hand menu that provides full-text links, one of which is a link to the PubMed Central source."
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 750px;">
{% endif %}

If an article is in both PMC and Europe PMC, the Full Text Sources box will show links to both. Of course, not every record in SciX has an OA copy. Links to OA versions appear in the Full Text Sources box when an OA version exists in the PMC and Europe PMC collections.

As of July 2026, SciX contains 1.9 million records that link to PMC, and 1.4 million that link to Europe PMC. This set includes publications in more than 4,000 unique journals going back to 1894, across all SciX collections. As you might expect for a corpus of life sciences literature, more than half of these records are in the [SciX General Science collection]{% if include.ads %}(https://ui.adsabs.harvard.edu/search/q=esources%3Apmc%2A+collection%3Ageneral&d=general){% else %}(https://scixplorer.org/search?q=esources%3Apmc%2A+collection%3Ageneral&d=general){% endif %}, though about a third are in [Earth Science]{% if include.ads %}(https://ui.adsabs.harvard.edu/search/q=esources%3Apmc%2A+collection%3Aearthscience&d=general){% else %}(https://scixplorer.org/search?q=esources%3Apmc%2A+collection%3Aearthscience&d=general){% endif %}, and about a quarter in [Physics]{% if include.ads %}(https://ui.adsabs.harvard.edu/search/q=esources%3Apmc%2A+collection%3Aphysics&d=general){% else %}(https://scixplorer.org/search?q=esources%3Apmc%2A+collection%3Aphysics&d=general){% endif %}. (Note that the SciX collections are not mutually exclusive; a publication can be in more than one.) There are even several thousand in the [Astronomy]{% if include.ads %}(https://ui.adsabs.harvard.edu/search/q=esources%3Apmc%2A+collection%3Aastronomy){% else %}(https://scixplorer.org/search?q=esources%3Apmc%2A+collection%3Aastronomy){% endif %} collection.

And the number of SciX records containing links to the full text of these OA articles will only increase: PMC and Europe PMC add thousands of new articles to their collections every day. SciX will update these links regularly, which will hugely increase the percentage of SciX-linked research that is Open Access. Providing links to OA materials in PMC and Europe PMC is a significant step forward for SciX in providing access to OA materials wherever it exists.

