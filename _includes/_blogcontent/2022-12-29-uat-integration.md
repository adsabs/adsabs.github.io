
The ADS Team is working in collaboration with Pavlos Protopapas and Ben Yuen of Harvard University to pilot the integration of the [Unified Astronomy Thesaurus (UAT)](https://astrothesaurus.org/) into ADS search and discovery for new, future, and legacy literature. ADS users will be able to browse results using left side facets in the query results screen, or conduct an initial search using UAT terms.

<div class="text-center">
    <img class="img-thumbnail" alt='An example search query in ADS. The example query is: full:"super Earth" property:refereed' src="{{ site.baseurl }}/blog/images/blog_2022-12-29_UAT1.png" />
<em>An example search query in ADS.</em>
</div>
<br>

<div class="text-center">
    <img class="img-thumbnail" alt="Example search results from ADS, showing UAT concepts as a facet query on the left side." src="{{ site.baseurl }}/blog/images/blog_2022-12-29_UAT2.png" />
<em>Example search results from ADS, showing UAT concepts as a facet query on the left side.</em>
</div>
<br>

<div class="text-center">
    <img class="img-thumbnail" alt='The same example search query in ADS as before, but now it includes filtering on a UAT concept. The example query is: full:"super Earth" property:refereed uat:"high contrast techniques"' src="{{ site.baseurl }}/blog/images/blog_2022-12-29_UAT3.png" />
<em>An example search query in ADS, including filtering on a UAT concept.</em>
</div>
<br>

While it is currently possible to search ADS by keywords provided by publishers, there is no single vocabulary that has been consistently used throughout the indexed literature in ADS. The Astronomical Subject Keywords that had been in use by leading astronomy journals since the 1970s hasn’t been updated since 2013, and may not cover the latest topics in the field. The "Keywords" also do not include definitions or relationships between concepts. For this reason, the American Astronomical Society (AAS) journals and the Publications of the Astronomical Society of the Pacific (PASP) elected to adopt the Unified Astronomy Thesaurus as its keyword system of choice in 2019 and 2020, respectively.  

The UAT is an open, interoperable, and community-supported project which formalizes astronomical concepts and their inter-relationships into a well-curated, freely available open resource. It reconciled divergent and isolated vocabularies from the fields of astronomy and astrophysics, such as the IAU Thesaurus, the Physics and Astronomy Classification Scheme, the Astronomy Subject Keywords, and others. The UAT’s primary mission is to support semantic enrichment of the literature, thereby enabling greater search and discovery across the astrophysics literature. In addition, the UAT is being used as a taxonomy with which to label other astronomical research products, such as software and datasets.

The ADS Team’s goal is to promote the use of UAT concepts as a standard way to describe and discover records in its astronomy collection. Ben Yuen, working under the supervision of Protopapas, is using machine learning techniques to automatically assign UAT terms to the majority of records in ADS which do not have them, such as the legacy literature. In order to produce accurate results, the system is being trained on the corpus of AAS articles which currently have UAT concepts associated with them. Validation of the results through editorial input and user feedback will be used to improve the automated process.

This pilot program is beneficial to all of ADS, as it provides a single, up-to-date set of concepts that can be used to identify all current research topics of interest to astronomers. The team intends to extend the system to use concepts drawn from other controlled vocabularies for subject areas outside the core astronomy collection. (To learn more about ADS’ recent expansion, which encompasses Planetary Science and Heliophysics literature, and will in future include Earth Science, and Biological & Physical Sciences, view [our earlier blog post](arc-ssad-project).) Development and testing of this prototype are ongoing. The ADS Team expects to release this capability in production by December 2023.

As ADS adopts use of the UAT across its astronomy collection, we encourage all astronomy and astrophysics publishers to use the thesaurus as its article keyword system to facilitate integration of this content into future ADS search and discovery. As more journals and research products, such as datasets, software, and proposals, are tagged with UAT terms, the ability to search, browse, and crosslink all of these resources by science topic will increase.

While the AAS has assumed formal ownership of the UAT, the thesaurus remains available under a Creative Commons License, ensuring its widest use while protecting the intellectual property of its contributors. Development and maintenance are stewarded by a broad group of parties with a direct stake in the UAT; this includes professional associations (IVOA, IAU), learned societies (AAS, RAS), publishers (IOP, AIP), software developers, librarians, and other curators working for major astronomy institutes and data archives.

The UAT has been implemented by an increasing number of journals, research organizations, and systems[^1].

[^1]: Current adoptees include:
    - American Astronomical Society journals, including The Astronomical Journal (AJ), The Astrophysical Journal (ApJ), ApJS, ApJL, The Planetary Science Journal (PSJ), and Research Notes of the AAS (RNAAS)
    - Astrophysics Data System (ADS)
    - Publications of the Astronomical Society of the Pacific (PASP)
    - International Virtual Observatory Alliance (IVOA)
    - Space Telescope Science Institute (STScI) for the Hubble Space Telescope (HST) and James Webb Space Telescope (JWST) proposal systems
    - Icarus - in formulation for 2023
