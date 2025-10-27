[General](#general) •
[arXiv](#arxiv) •
[Refereed status](#refereed-status) •
[Submissions](#submissions)

## General

##### Q: How often do new articles get added to the database?
This depends on the source. We ingest from arXiv daily; from astronomy journals and other sources weekly, over the weekend; and from physics journals and other sources about once every 3 weeks, also over a weekend.

##### Q: How do I submit missing articles or corrections to an existing article? Missing references?
* [Missing articles/corrections to existing article]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %})
* [Missing references]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/feedback/missingreferences)
* [Link two associated articles]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/feedback/associatedarticles)

Note that these forms do not work if you're using the basic HTML version of {{ include.site }}, and occasionally, some users encounter errors when submitting these forms; [email us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}) if you run into issues.

##### Q: My paper is visible at the publisher but not in {{ include.site }} yet.
Published articles are added to the database at regular intervals; see the publishing schedule above. In addition, for most journals, we do not add the article until it has a published volume and page number.  While we appreciate the early access versions, we have found that matching them after the fact and tracking all citations correctly is difficult to do correctly.

If sufficient time has passed since the publication date and the article is still unavailable, it may be in a journal we don't index by default. It's also possible that the article has been added, but is not appearing the expected collection (astronomy or physics); this is generally the case if the article appears in a general science journal (Nature, Science) where we need keyword information to assign it to a specific collection. Finally, in rare cases deliveries from publishers are missing some articles. If you believe your article should be in the database already, [email us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}) for help.

##### Q: What are bibliographic groups (bib groups)? These appear in a left-side filter.
Bibliographic groups are hand curated by librarians and/or curators at various institutions and generally contain a list of publications produced by researchers at a given institution or using specific telescope(s). If you're a librarian or curator interested in curating a publicly available collection, [email us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}).

##### Q: My name is incorrect in an {{ include.site }} record.
We receive author names and other metadata directly from the publisher. First check that your name is correct on the published article; if it isn't, first contact the publisher directly to fix it with them. However, if your name is correct with the publisher and wrong in the {{ include.site }} database, [fill out this form]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %}) and we'll correct it.

##### Q: My name has changed since I first started publishing. How can I ensure people find all of my papers when searching for my name?
We offer three options; one or more of these may suit your needs. [Email us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}) for help deciding which option(s) are best for you and for making any necessary updates:
* We maintain a list of author synonyms, so searches for one author name return results for both names. Let us know all of the names you've published under to have your names added to this list. (Note that common name variations, such as publishing under your entire first name vs. just an initial, are already included in searches.)
* You may also consider [registering for an ORCID ID]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/blog{% else %}/scixblog{% endif %}/orcid-claims) and using that to maintain a personal bibliography.
* If you'd prefer that previous names not be visible in {{ include.site }}, we can modify our searchable metadata on papers published under the previous name(s) to reflect your current name. With this option, all pages within {{ include.site }} (e.g. search results, paper abstract pages) will reflect the new name; note, however, that we cannot modify external data and links, such as publisher-provided PDFs.

For more information, see our [name change policy]({% if include.ads %}../policies/name-changes{% else %}../policies-scix/name-changes{% endif %}).

##### Q: What journals and other material do you index?
Complete lists of the journals, conferences, and other sources we index may be found [here]({% if include.ads %}http://adsabs.harvard.edu/abs_doc/journal_abbr.html{% else %}{{ site.scix_base_url }}/journalsdb{% endif %}).

##### Q: What papers do you have the full text for?
In general, we have searchable full text for most major journals in astronomy and physics, especially recent volumes. This includes articles in the arXiv.

##### Q: How do I get my conference proceeding in {{ include.site }}?
Full instructions for submitting conference proceedings can be found [here]({% if include.ads %}../data_faq/conf_proc{% else %}../data_faq-scix/conf_proc{% endif %}).

##### Q: Why is my citation count different on other platforms?
While we do our best to capture citations accurately, there are a few reasons we would have more or fewer citations than you may see on other platforms. The primary reasons are as follows:
- We merge the arXiv record with the published record, so that a citation for either version counts as one citation. This avoids double counting a citation.
- Citations to books, book chapters, and other less formally structured content is often difficult to resolve in an automated fashion. Our citations to this content is likely under-counted.
- In order for a citation to count in our system, both the cited record and the citing record must be in our system. Users are always welcome to submit missing content through the [Missing articles]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %}) form linked off our feedback menu.

## arXiv
##### Q: My arXiv paper is missing its references.
We extract references directly from the PDF for arXiv records, which doesn't always work well, depending on reference and document format. If the paper will be published, we will get the reference list from the publisher and will update the references on the record at that point. Note also that we're working on a new module for extracting references directly from PDFs and arXiv reference extraction should improve at that point.

##### Q: My arXiv paper had some citations before it was published. Will these be lost once the published version is out?
We automatically merge the arXiv and published versions of papers, including citations.

##### Q: The author list of the arXiv and the published versions of my paper are different. What happens when the two versions are merged?
Author metadata from the published version takes precedence, so arXiv-only coauthors will be removed from the record.

##### Q: The published version of my paper is out and indexed on {{ include.site }}, but the arXiv version is listed separately.
The published and the arXiv versions of a paper should merge into a single entry automatically. Occasionally that doesn't work; [let us know]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/feedback/associatedarticles) and we'll fix it.

##### Q: My name is correct on arXiv but wrong in {{ include.site }}.  How can I fix it?
Submit your corrections using [this form]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %}).

##### Q: My name is wrong in arXiv, will you fix it?
You'll need to contact the arXiv directly for corrections to your papers on their site.

## Refereed status
##### Q: Why is my PhD thesis listed as refereed?
{{ include.site }} has decided to list PhD theses as refereed because they go under the review of a thesis committee and are thus "peer reviewed." However, if you prefer to not see PhD theses appear in your search results, restrict your search results to articles only using the "Publication Type" filter in the left-side column.

##### Q: A conference proceeding is listed as non-refereed even though it underwent peer review.
Most conference proceedings are not refereed. They may be reviewed by an editor, but rarely is there the kind of rigorous review as is done by many journals. (In general, users and editors and librarians and publishers all have different opinions on what constitutes "peer-reviewed.")

If a publication or a conference is generally not peer-reviewed, all articles/proceedings within that publication/conference will automatically be listed as non-refereed. If a particular article/proceeding within the generally non-refereed publication/conference is peer-reviewed, have the editors [email us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}) to confirm and we can correct the listing.

## Submissions
##### Q: How do I submit my PhD thesis?
Some institutions send us their recent PhD theses directly, though it may take a few months post-defense for us to receive them. However, if your institution does not send us your thesis, you have several options to add it to our database:
* [Zenodo Astronomy Thesis](https://zenodo.org/communities/astrothesis) collection: This is an open-source repository of astronomy theses and dissertations which is automatically ingested into {{ include.site }} roughly once a month. If your thesis is already indexed by {{ include.site }} but the text is not openly accessible, you can upload a copy of the PDF to make it openly available. This is a good option if you'd like your thesis to  be openly available and it's not currently accessible online.
* [{{ include.site }} submission]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %}): You can submit your thesis metadata directly to {{ include.site }} for indexing. If you want the PDF to be linked to the record, it will first need to be hosted somewhere online and then you can provide the URL and other metadata using this form. If the text of your thesis is not already available online and you'd like it to be, consider submitting it to the Zenodo collection.

##### Q: My name (or title, etc.) is misspelled on my paper.
If it is wrong on the publisher's website, you'll need to contact them to correct the error, as we've agreed with the publishers to reflect the data they pass on to us.

If it's right on the publisher's website but wrong on ours, we're sorry for the error! [Contact us]({% if include.ads %}{{ site.ads_base_url }}/feedback/correctabstract{% else %}{{ site.scix_base_url }}/feedback/missingrecord{% endif %}) so we can fix it.

##### Q: How can I get my software package indexed in {{ include.site }}?
Software records are automatically indexed in {{ include.site }} once they have a Zenodo record and have been cited at least once. If you'd like to make your software records eligible for indexing in {{ include.site }}, complete the following steps:
1. Upload your software code to [Zenodo](https://zenodo.org/). You can do this directly or by linking to a Github repository. If you link to a Github repository, you can specify a specific release or version, or you can link to the top-level repository to create a non-version-specific record.
2. Get the BibTeX (or other bibliographic format) record from Zenodo and cite it in your paper as normal. Your software will not yet be in {{ include.site }}, so make sure to get the citation information from Zenodo.
3. Once your paper has been published and is indexed in {{ include.site }}, the system will recognize that the bibliography contains a software record and will automatically create a corresponding software record in the {{ include.site }} database. The publisher will be listed as Zenodo and the bibstem (the abbreviation that appears in the bibcode) will be [zndo]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}bibstem%3A%22zndo%22&sort=date%20desc%2C%20bibcode%20desc&p_=0). The publication type for these records is [software]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}doctype%3Asoftware&sort=date%20desc%2C%20bibcode%20desc&p_=0).

Some things to keep in mind:
* Zenodo allows you to create different records for different versions of your software, which generally correspond to different releases in Github. This can be beneficial if the software has changed substantially with time, or if different authors have worked on different versions of the code and need to be acknowledged as appropriate. {{ include.site }} will index each Zenodo version of your software separately, as long as each has citations. Currently, citations are counted for each version separately, but eventually it will be possible to see all citations for all versions of a software package in one record in {{ include.site }}.
* The [Astrophysics Source Code Library](http://ascl.net) indexes astronomy-related software that has been used in a publication. {{ include.site }} indexes these ASCL records (bibstem: [ascl]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}bibstem%3A%22ascl%22&sort=date%20desc%2C%20bibcode%20desc&p_=0), publication type: [software]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}doctype%3Asoftware&sort=date%20desc%2C%20bibcode%20desc&p_=0)) and they can collect citations similarly to the process above. One difference between the two processes is that ASCL indexes only the non-version-specific record while Zenodo indexes each version separately. It is possible for a given software package to be in both Zenodo and ASCL, if they fit the necessary criteria for each.

##### Q: I submitted some ORCID claims but they don't show up when I search by my ORCID ID.
These can take up to 24 hours to index. Please [contact us](mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}) if they aren't showing up after this time.
