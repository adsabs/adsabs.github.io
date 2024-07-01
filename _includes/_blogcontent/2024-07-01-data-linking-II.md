# Introduction

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f1.png" />
<br>
</div>
<br>

In the [first part](https://scixplorer.org/scixblog/data-linking-I) of this blog series, we provided a general description of the holdings in the [NASA Science Explorer](https://scixplorer.org/) (NASA SciX); in this second part, we highlight a specific aspect of these holdings and place it in the context of the Research Life Cycle. The concept of a Research Life Cycle is not anything new; it represents the way in which scholarly research is done and has, in principle, not changed for a long time, probably centuries. It has fundamentally changed, however, in the way it is expressed. 

The first of these changes happened in the late 1990s: the introduction of electronic publishing of scholarly articles. In the same era, the discovery of these articles was also revolutionized with the introduction of the World Wide Web. Jumping to the here and the now, there is very little left in the Research Life Cycle that is not or cannot be expressed electronically. Let's refer to these elements as "research artifacts"; each of these artifacts carries specific knowledge related to a specific stage of this life cycle. With the promotion of Open Science, there is a growing realization that this movement is best supported if these artifacts are accurately and formally represented in the process of exposing scholarly research. 

Traditionally, scholarly articles were the sole means of exposing scholarly research; however, they just represent one aspect of this research: that of useful outcomes. Everything else that goes into and supports research is important too, especially within the context of preservation, reusability and reproducibility; this context is the purview of the [FAIR Principles](https://www.go-fair.org/fair-principles/). Examples of other artifacts include data, software, proposals, and presentations. The overall goal of FAIR is to enhance the sharing, preservation and communication of data-intensive research (like Astronomy, Heliophysics, Earth Science and Space Sciences). In other words, the digital-born, scholarly articles now exist as entities linked to other electronic artifacts; it is up to publishers and discovery platforms, like NASA SciX, to make these linkages possible electronically and discoverable. Perhaps to state the obvious: NASA SciX is a publication-centric discovery platform, so it supports the discovery of research artifacts as they are linked to the scholarly literature. To search directly for specific data or software products a dedicated service will need to be used; the [NASA Science Discovery Engine](https://sciencediscoveryengine.nasa.gov/) is an example to search for NASA's science data, documentation, and code. 

Since the whole of the artifacts referenced by a scholarly article forms the best representation of the science discussed in the article, having a proper coverage of these sources will help in properly representing different aspects and stages of research life cycles. Just capturing citations to other scholarly publications would not only leave out important information, it would also omit proper attribution to researchers who contribute as authors of non-traditional research products. The NASA Science Explorer has implemented a workflow for capturing software citations; this workflow allows the detection and ingestion of citations to software products used in scholarly publications. Since both data and software citations are crucial for the transparency of research results and for the transmission of credit, NASA SciX will implement indexing of high-level and reused data products, in particular those published by NASA Archives, and track their citations.

Citations are just one form of the linkages we are referring to. Linkages are essentially so-called semantic triples (figure 2): a triple is a sequence of three entities that codifies a statement about semantic data in the form of subject–predicate–object expressions.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f2.png" />
<br>
</div>
<br>

The predicate describes the relationship between two entities, one the subject and the other the object. The relationship within the framework of NASA SciX can be one of two: *cites* or *mentions*. Also, within this framework, the subject always refers to a publication and currently the object refers to either a data product or software. At this point it is good to explain the difference between the treatment of these two relationships within the SciX context, in particular the consequences. Table 1 summarizes the difference between the two scenarios in SciX. The row "Form" corresponds to another limitation within SciX: only objects that have a URL associated with them can be considered; objects without URL are per definition not actionable.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_t1.png" />
<br>
<em>Table 1: Difference between mentions and citations. In the case of cites, only DOIs are in principle actionable because they have harvestable metadata associated with them. Cites with other identifiers are actionable if the cited work is already indexed.
</em>
</div>
<br>

In this blog, we focus on the cases where the object is a data product. In the next sections, we discuss the support of data links and data citations, respectively.

# Linked data products

One of the distinguishing features of SciX is the presence of links from its records to research archives and databases. This is particularly significant for the core astronomy journals which work with archive curators to create and maintain rich online resources associated with the articles they publish. As an example, 70% of articles published in the main astronomy journals during 2023 have links to data products. Historically, the links have been created by curators upon the ingestion of datasets published with the article (as is the case for [VizieR data tables](https://scixplorer.org/search?q=bibstem%3AyCat&sort=score+desc%2Cdate+desc&p=1)), cross-referencing of astronomical object measurements (SIMBAD and NED), or telescope bibliographies (Astrophysics Data Archives such as Chandra, MAST, IRSA, HEASARC, etc). The ADS, and now SciX, has been working with collaborators at these institutions to enable links between its records and these datasets on a regular basis, allowing for the curated links to be exposed to the end user.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f3.png" />
<br>
</div>
<br>

In their response to the call for Open Science, many publishers have started to incorporate so-called Data Availability Statement sections in the articles they publish. We mine links from these sections for most journals we index from the AGU, Elsevier, Springer and the AAS. Currently we simply mine these links and do little curation. The only part that needs action from the SciX curation team is the fact that we label these links for their display in the ADS user interface (figure 3). At this moment, these labels are based on heuristics. For example, certain DOI prefixes can be associated uniquely with a particular repository, just like some URL patterns. As of the writing of this blog, we have mined about 110k links this way.

# Working with linked data in SciX

In general, the only discovery tools at your disposal are the ability to find records that have linked data in general or linked data associated with a particular data source (if you happen to know the abbreviation used in SciX). For any additional filtering you will need to use circumstantial evidence using other SciX search fields. The query *property:data* will find records that linked data associated with them in general, while the query *data:MAST* will find records with data products hosted at the Mikulski Archive for Space Telescopes (MAST); some labels used in SciX for data links are obvious (e.g. when they are the same as the acronym of the data center). Whenever we were unable to assign a descriptive label to a data link, we assigned the vanilla label *DATASOURCE*.

A good strategy for finding data sources associated with a particular topic is to do a general search on that topic and filter the results on records that link to data (*property:data*). For example, if you are interested in carbonaceous chondrites in the context of the Moon, you can query [Lunar carbonaceous chondrites](https://scixplorer.org/search?q=Lunar+carbonaceous+chondrites&sort=score+desc%2Cdate+desc&p=1) and find close to 1,500 records; [adding the filter property:data](https://scixplorer.org/search?q=Lunar+carbonaceous+chondrites+property%3Adata&sort=score+desc%2Cdate+desc&p=1&n=10) will limit this set to 68 records. Opening the *Data* facet will show that most records are associated with the label *Astromat*; this label corresponds to the [NASA Astromaterials Data System](https://www.astromat.org/). A little bit more insight can be obtained by switching on the highlights for this search. Finding records that link a publication to a specific data product is currently not supported. If you happen to know a uniquely identifying string or phrase for that data product, you could try doing a full text search. For example, if you try to find mentions of various versions of the PDS dataset identified by *urn:nasa:pds:ast-lightcurve-database*, you can run the query

> [full:"urn:nasa:pds:ast-lightcurve-database"](https://scixplorer.org/search?q=full%3A%22urn%3Anasa%3Apds%3Aast-lightcurve-database%22&sort=score+desc%2Cdate+desc&p=1&n=10)

Even though SciX does not offer ways to find links to specific data products, the service does provide a powerful discovery environment to explore the context for data associated with or generated in specific missions, by certain instruments, for particular science topics or hosted in a certain repository. 

For the first example we will explore the science topics covered by refereed Open Access publications, with links to data, that mention the [Near Infrared Camera and Multi-Object Spectrometer](https://www.stsci.edu/hst/instrumentation/legacy/nicmos) (NICMOS) in their title, abstract or keywords:

> [NICMOS property:(data refereed openaccess)](https://scixplorer.org/search?q=NICMOS+property%3A(data+refereed+openaccess)+&sort=score+desc%2Cdate+desc&p=1)

The *Author* facet will show you the most prolific authors associated with these publications, one of whom is Marcia Rieke who recently was awarded the Catherine Wolfe Bruce Gold Medal. 

To get some insight into the science topics covered by these publications we generate the [Paper Network](https://scixplorer.org/search/paper_network?q=NICMOS+property%3A%28data+refereed+openaccess%29+&sort=score+desc%2Cdate+desc&p=1). By default, this network is generated for the first 400 publications; some additional details can be generated by increasing this amount (with a maximum of 1,000) and regenerating this network diagram. Figure 4 (left) shows the results.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f4.png" />
<br>
</div>
<br>

The diagram shows a number of high level science topics. The exploration does not need to end here; if one's particular interest is circumstellar disks and protoplanetary nebulae, the results can be explored further by clicking on the blue segment, clicking on the button "Add to filter" (to the right of the Group 1 header) and hitting the search button. This generates an overview of just the publications in this group. If there are sufficient publications in this group, we can generate another Paper Network. This second network splits the original, larger category up into smaller, more detailed segments, providing more insight into the topics covered (figure 4, right diagram).

In a similar way we can explore the use of data links from a specific data repository. The following query returns all refereed, Open Access publications, published in the period 2020-2024 with a link to data available at the [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/)

> [data:NOAA property:(refereed openaccess) year:2020-2024
> ](https://scixplorer.org/search?q=data%3ANOAA+property%3A(refereed+openaccess)+year%3A2020-2024&sort=score+desc%2Cdate+desc&p=1)

Just like before, the Paper Network can be used to indicate the range of topics discussed in the publications returned by the query. Figure 5 shows the results for data hosted at NOAA (left) and data hosted at the Oak Ridge National Laboratory Distributed Active Archive Center, as an additional example (right).

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f5.png" />
<br>
</div>
<br>

The next example is to illustrate how to find publications that may be able to provide us with data products if we are interested in building on existing research in a particular topic. As a topic we select exoplanet atmospheres and we will start our exploration with recent, refereed Open Access publications, with links to data. The following query will generate the publications that correspond to this

> ["exoplanet atmosphere" property:(refereed data openaccess) year:2020-2024](https://scixplorer.org/search?q=%22exoplanet+atmosphere%22+property%3A(refereed+data+openaccess)+year%3A2020-2024&sort=score+desc%2Cdate+desc&fq_selection=(docs(cb91d308eb354bbc3a9b0b62b92b79c5))&p=1&fq=%7B%21type%3Daqp+v%3D%24fq_selection%7D)

The results are shown in figure 6. The diagram on the left shows the results for the initial query and the diagram on the right shows the results when we generate the paper network for the publications in the orange segment only.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/data_linking_II_f6.png" />
<br>
</div>
<br>

Finally, the powerful SciX query language allows us to find Open Access, refereed publications, from the period 2010-2023, in the Earth Science collection, which have at least one link to data and cite at least one software product:

> property:(refereed openaccess data) year:2010-2023 citations(doctype:software) collection:earthscience

