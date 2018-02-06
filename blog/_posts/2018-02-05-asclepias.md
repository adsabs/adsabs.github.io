---
layout: blog_post
title: "Asclepias - Enabling software citation & discovery workflows"
author: "Edwin Henneken"
position: "ADS Developer"
category: blog
label: technical
thumbnail: blog/images/blog_2016-09-19_adsbumblebee.png
---
Soon, if not already, the research lifecycle will be fully digital. Every stage can be captured by one or more digital objects, each of which carries specific knowledge with regards to that stage. The most obvious inhabitant of this digital cosmos is the scholarly publication, but there are many more species, ranging from observation proposals, datasets, software to posters and presentations. With repositories like mission data archives, [Figshare](https://figshare.com/) and [Zenodo](https://zenodo.org/), all of these objects can, in principle, be made discoverable and citable. In this blog we focus on one particular digital object: software. Enter ***Asclepias***! Asclepias, “*Enabling software citation and discovery workflows*”, is a project funded through a grant from the Alfred P. Sloan Foundation to the American Astronomical Society (AAS), and it involves collaboration between the AAS, Zenodo, the ADS and Thomas Robitaille as freelancer. Why this collaboration? It reflects the fact that no one stakeholder can “solve” the problem of software citation.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2018_02_05_lifecycle.jpg" />
    Figure source: "Research Life Cycle" image from UC Irvine [Library Digital Scholarship Services](https://www.lib.uci.edu/dss)
</div>

|         |           | 
| :------------- |:-------------| 
| <img src="{{site.baseurl}}/blog/images/blog_2018_02_05_AAS_logo.png" alt="AAS" class="img-responsive">        | Gus Muench           | 
| <img src="{{site.baseurl}}/blog/images/blog_2018_02_05_ADS_logo.png" alt="ADS" class="img-responsive">      | Alberto Accomazzi, Sergi Blanco-Cuaresma, Edwin Henneken | 
| <img src="{{site.baseurl}}/blog/images/blog_2018_02_05_Zenodo_logo.png" alt="Zenodo" class="img-responsive">      | Lars Holm Nielsen, Krzysztof Nowak , Alexander Ioannidis      |  
| <img src="{{site.baseurl}}/blog/images/blog_2018_02_05_TR_logo.png" alt="Robitaille" class="img-responsive"> | Thomas Robitaille      | 

What is so special about software citation that it takes so many parties to deal with it properly? This becomes clear when you think about how to move from a position where the curation and preservation of software products has been taken care of, to one where these products are discoverable, together with their links to the scholarly literature (by means of citations or otherwise). One challenge is that currently, there is no established standard or policy for citing software in scholarly publications. Writing a “software paper” may seem like a work-around, but it is not a very good one. It can work if you just write one, static piece of software. You describe how it works, acknowledge contributors and, perhaps, where people can get a copy, and you’re done. In all other cases, even though it is better than nothing, a “software paper” is just a bad proxy for representing all aspects. Software is a highly dynamical object, especially when it evolves from version to version, with different contributors and different characteristics. For this reason, it is important to capture the acknowledgement of actual software products. Since reworking the entire, established process of capturing scholarly acknowledgement (read: “citations”) is extremely hard, to say the least, adapting the existing mechanism of finding citations to include software, will be the next best thing. 

This is exactly what the Asclepias project focuses on. Its goal is to **promote scientific software** into an identifiable, citable, and preservable object. The project focuses on the needs of two of the most important roles researchers play in the scholarly ecosystem: **authors** of scholarly manuscripts and **developers** of scientific software. This goal can only be reached if the research community participates, and the research community can only be expected to participate if there are tools and workflows in place that make the citation of software products just as easy as citing a publication. What needs to be in place to make this happen? The publisher (AAS) will need to implement practices and tools that will support the integration of software citations into the scholarly publishing workflow. From the viewpoint of bibliographic indexing services (ADS), the implementation means the development of first-class support of a software framework to detect software citations and take all necessary steps to attribute and expose these citations. For repositories (Zenodo), implementation means interoperability with Github and similar codebases (like Bitbucket). The minting of DOIs is one step in this integration, and being able to send out notifications that (astronomy related) software has been released, including version updates, is another. All these steps are only possible if **metadata standards** for software packages are adopted. Just slapping a DOI on a digital object is not a structural solution, not by a long shot. It may help an object location be persistent, but that is not how you discover something. That is where the metadata is essential! Within the Asclepias project, the development of metadata is guided by the software citation practices put forward by the FORCE11 Software Citation Implementation Group. When all of this is in place, the three stakeholders will have put in place the framework that will provide the research community with simple instructions for how to make software discoverable and how to include software citations in the process of writing a scholarly paper.

What does all of this mean in practice? Let’s look at an example. The Python module *corner.py* (previously known as *triangle.py*) is widely used in astronomy. Its main developer, Daniel Foreman-Mackey, made it available on [Github](https://github.com/dfm/corner.py) and published an [entry](http://joss.theoj.org/papers/10.21105/joss.00024) in the Journal of Open Source Software (JOSS). The ADS has a [record](http://ui.adsabs.harvard.edu/#abs/2016JOSS.2016...24F/abstract) for this JOSS software paper, and as a result citations are being captured (provided people cite this record properly). As of November 9, 2017, this JOSS paper accumulated 77 citations.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2018_02_05_JOSS_corner.png" />
</div>

Thanks to Zenodo’s interoperability with Github, records were created for both *triangle.py* and *[corner.py](https://doi.org/10.5281/zenodo.53155)*. Zenodo mints a DOI for each software version and also a so-called concept DOI. The concept DOI is available for when you don’t want to cite a specific software version, but just “the latest”. The crucial step that make this interoperability possible is the authentication within Zenodo, using your Github account, allowing Zenodo to view and retrieve your repositories on Github. For details, see: https://guides.github.com/activities/citable-code/.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2018_02_05_zenodo.png" />
</div>

The next step is to go through the reference data in the ADS holdings and see if we find any evidence of the Zenodo DOIs, corresponding with the different versions of both *triangle.py* and *corner.py*. The table below shows the results (as of Feburary 5, 2018).

|        |           |  |
| ------------- |:-------------:| -----:|
| 10.5281/zenodo.10598      | triangle | 2 |
| 10.5281/zenodo.11020      | triangle      |   40 |
| 10.5281/zenodo.45906 | corner      |    16 |
| 10.5281/zenodo.53155 | corner      |    7 |

This analysis shows that authors are already citing the different versions of both modules, but also that it results in a significant amount of additional citations! 

The bottom line is that all of this is great in many ways. From the researcher’s perspective, it provides proper attribution for their role (and impact) as software developer and it provides them with a means to monitor on how their software is being used, specifically with regards to versions. The fact that, in this process, software gets deposited in a repository and proper metadata is attached and registered, is great for the community and science in general. It supports the goals of preservation and reproducibility. In this way, these efforts greatly improve the accurate recording of crucial aspects of the research lifecycle. Of course, none of this goes anywhere if the research community does not participate. There was a special session on software citation during the 231st AAS Meeting in National Harbor (session 307 Astronomy Software Publishing: Community Roles and Services, in National Harbor 2, 10:00 am – 11:30 am). If you are interested to hear more about this project, or software citation in general, please write us ([ads@cfa.harvard.edu](ads@cfa.harvard.edu)). More details on the Asclepias project can be found here: 

* Muench, August; Accomazzi, Alberto; Holm Nielsen, Lars (2017), “Asclepias: Enabling software citation & discovery workflows”, poster presented at LISA VIII conference (https://doi.org/10.5281/zenodo.803474)
* Henneken, Edwin, Accomazzi, Alberto, Blanco-Cuaresma, Sergi, Muench, August, & Nielsen, Lars Holm. (2017). “Asclepias - Capturing Software Citations in Astronomy”, talk given at the Metrics workshop during the 2017 ASIS&T Annual Meeting (http://doi.org/10.5281/zenodo.1011088)
