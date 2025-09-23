The {{ include.site }} curation model is represented by the diagram below (see [Kurtz et al. 2021]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/abs/2021BAAS...53d.470K/abstract)). 

<figure>
    <img src="../img/curation_model.png"  class="img-responsive" alt="{{ include.site }} Curation Model">
    <figcaption><em>{{ include.site }}'s tiered curation model. The core collection represents disciplines where its curation is strongest and its coverage is authoritative. The surrounding tiers are connected to the core via the citation network.</em></figcaption>
</figure>
<br>
The Core Collection consists of the main journals for the disciplines covered, the most influential journals. For ADS, this includes astronomy, astrophysics, and closely related fields. As we move into the inner and outer rings, curation efforts decrease. A qualitative characterization of the model is given below.

### Core: main journals for discipline
* Complete, authoritative coverage of the literature
* High-level data products and software indexed
* Links to datasets and archives

### Inner Ring: closely related disciplines
* Most refereed journals covered
* Some conf proceedings, some gray literature
* Citation and fulltext coverage incomplete

### Outer Ring: connected to inner content
* Incomplete coverage of the literature because outside of disciplinary scope
* Includes content from multidisciplinary journals (e.g. Nature) or repositories (arXiv)
* No curation applied other than basic error corrections

How do we determine which journals go in which section? Once the Core Collection has been populated, appropriate journals for the Inner and Outer Rings can be determined as indicated in the diagram above. Up to now, journal selection for the Core Collection has been heuristic, based on qualitative arguments and domain knowledge. We felt it was important to formulate selection criteria based on quantitative arguments. These quantitative selection criteria are unavoidably based on journal metrics and just like any metric, journal metrics are not without controversy. We have settled on the so-called [Journal Eigenfactor](https://en.wikipedia.org/wiki/Eigenfactor) as the main indicator for journal importance. More details on how this metric was used to determine the journal selection for the Core Collection can be found in [this blog]({{ site.baseurl }}{% if include.ads %}/blog{% else %}/scixblog{% endif %}/curation-model).
