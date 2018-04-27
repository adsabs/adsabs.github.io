---
title: ADS BLOG
author: Karin Pelte
date: April 2018
bibliography: NETWORKLit_2.bib
---

# How research on multiple and interacting galaxies evolved: an epistemological and bibliometric investigation

<br>

<span style="font-size:larger;">Karin Pelte (Technische Universität Berlin Germany)</span>

<span style="font-size:larger;">Edwin Henneken (ADS)</span>

## Introduction

Authors publish because they want to transfer information. They have been doing so for centuries, resulting in a vast body of scholarly literature, recording the emergence and evolution of a broad spectrum of ideas and quests for answers. This universe of scientific literature is a rich source of information for people interested and involved in the study of the history of science. This field, as a science by itself, started in the 18th century. Until the advent of electronic media and the ability to transfer printed to electronic media, studying the history of science meant getting stacks and stacks of books and spending many hours in libraries combing through texts and making notes. Even though this may very well still be true, access to electronic media and the ability to search intelligently has greatly empowered data mining and allowed scientists to discover patterns. The introduction of the ADS API, with its access to the powerful query language in the new ADS, has given those interested in the history of astronomy a powerful tool. The ADS has had numerous requests, asking us permission to use the ADS API for some sort of research purpose. It is necessary to send us such requests, because we have provided Terms of Use. These Terms of Use are there for good reasons. We also ask people and projects using our data to acknowledge this fact in publications by including the phrase "This research has made use of NASA's Astrophysics Data System". A great example of such research is that being done within the context of the "Concepts At Work" project.

## Origin and Scope of the Project

The research project "Concepts at work" was originally developed in a workshop which planned a long term investigation into astrophysics research practices in the light of philosophical, sociological and historical questions. Inspired by the epistemology of Polish immunologist Ludwik Fleck (1896–1961) (Fleck, 1979), this multidisciplinary enterprise was fixed to study how astrophysical facts come into being and evolve.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/LudwikFleck.jpg" />
<br>Ludwik Fleck (credit: Archiv für Zeitgeschichte Zürich)
</div>

The historical project which was granted a three year funding by the DFG (German Research Foundation) in 2015, still profits from these initial discussions between philosophers, sociologists and historians of science, and continues to work along the lines which were then sketched out.

In the project at hand, [Karin Pelte](http://www.philosophie.tu-berlin.de/menue/fachgebiete/wissenschaftsgeschichte/team/wissenschaftliche_mitarbeiter/karin_pelte_ma/) studies the world wide development of the research on multiple and interacting galaxies from around 1925 to 1980. *Multiple and interacting galaxies* (MIG from here on) is used as a catch-all and represents many of the names given to such phenomena as double, binary, multiple, colliding, merging, exploding, satellite galaxies, or small groups and chains or nests of galaxies.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/VV_1977.png" />
Taken fromVorontsov-Vel'yaminov's <a href="https://ui.adsabs.harvard.edu/#abs/19771977A&AS...28....1V/abstract">Atlas and Catalogue of Interacting Galaxies II</a>, 1977
</div>

Why this specific type of research, and why this time period? During and after the so-called "Hubble Era", when our Galaxy became one amongst many in an expanding universe, another major conceptual transformation set in: the so-called "Island Universes" evolving uniformly in empty space turned into multi-frequency and multifaceted interactive systems in a universe so violent that astronomers asked whether it was actually "unsafe for a galaxy to walk the streets" (King, 1977). Karin suspects that the studies on MIG contributed substantially to this second development. Even though studies on MIG were undertaken in many different places such as Sweden, the Soviet Socialist Republics, the United States, Germany, Argentine, France, Italy, India, Japan, those scientists who contributed works over a longer stretch of time remained small in numbers. How to place their contributions in the field of galaxy studies or extragalactic astronomy as a whole, and whether they actually formed a proper research strand is hard to say. Galaxy studies and astrophysics in general developed into a great many different directions and separated domains before 1980 (Eisber, 2001; Harwit, 1973), and the history of astronomy has hardly started to draw a map of astrophysics after WW II. It seems rather that MIG remained objects of study related to various greater research areas as e.g. cosmic radio emission, quasars and missing mass (dark matter).

## Project Goal and Techniques Used

The main goal of Karin's project is to explore how the central astrophysical concept of the galaxy got reconfigured within the context of the studies on MIG. The data used for this exploration is the literature on MIG – mostly digitized astrophysics papers available on ADS – and one of the tools of investigation is citation network analysis (CNA). In a citation network the published papers become nodes and the citations connecting them become edges. In a co-citation network, however, the edges don't present direct citations but rather the fact that papers A and B were co-cited together in papers C, D, E and so forth. Direct and derived citation networks allow to identify central publications. More importantly for this project, they can provide an overview of the different research areas and discussions which informed a research dynamic over time. To this end, the co-citation network is partitioned into topical sub-networks with the help of a "community detection" algorithm such as "modularity" (Blondel, 2008). One should be aware though that in graph theory – the research area in which most of these helpful algorithms originate – the concept of "community" is not rigorously defined, and that such features as "directionality" in a direct citation network still present a challenge to those working on community detection (Fortunato, 2010; Palla, 2007).

## Data Collection and Core Data Set

At an early stage of her investigation, Karin put together a list of main actors and publications in the research on MIG. This list was based on a growing collection of original papers as well as the present historiography which includes many recollections of participating astronomers. Based on the citations and references of this first selection of papers which were provided by the online data bases Web of Science (WoS) and ADS, this selection grew into a snow ball sample. Combined keyword searches added further pertinent papers. The ADS soon proved to be the better data base especially since its search engine is open source and hence allows customized access to its data. Web of Science, by contrast, is now owned by private equity investors Onex and Baring Asia - and according to Chadegani (2013) a subscription to WoS might cost a larger institution such as an university around 100,000 dollars a year.

The open source search engine of the ADS soon came in handy. Karin's assistant Theodor Costea, who only learnt how to code in Python during the project, developed a script using the ADS API to extract the pertaining references and citations from the ADS into the open source DB browser for SQLite (<http://sqlitebrowser.org/>). The script allows not only a compound search including authors names, title and keywords as well as time intervals, but also defines the network type (e.g. co-citation or bibliographic coupling) and adds weighted attributes. A recent addition is the community detecting algorithm *InfoMap* (©<http://mapequation.org>) in the script. This algorithm takes into account the directionality of a direct citation network, as opposed to, say "modularity" (Blondel, 2008) which is integrated into the open source network visualizing software gephi (<https://gephi.org/>). Theo's script will soon be published on Github (<https://github.com/>) so that many more scholars or people simply interested in astrophysics research dynamics might profit from it.

## Things to Come

"Concepts at Work" could not have evolved without the amazingly rich source of original papers provided by the ADS. For the bibliometric investigation, however, gaps in the metadata (citations and references) in many of the pertaining articles, especially in Russian language and early publications, pose a challenge. Again, Theo together with his successor Towhidur R. Bhyian and Karin developed a 'semi-automated' workflow to complete at least the missing references. Once these works have been carried out the blog will return and offer some first results from a citation network analysis as well as further discuss the development of research on MIG.

## Contact
If you have questions/feedback with regards to the "Concepts at Work" project, you can contact Karin at [pelte(at)tu-berlin.de](http://www.tu-berlin.de/allgemeine_seiten/e_mail_anfrage/id/179204/?no_cache=1&ask_mail=WuNNdgAInnBVl0KHPneCf%2BDO%2BYAYBl5Ur1oEp94L4Ns%3D&ask_name=PELTE). For more information about the ADS API, please contact the [ADS](mailto:adshelp@cfa.harvard.edu).
 
# References
* Blondel, Vincent D., Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre. 2008. “Fast Unfolding of Communities in Large Networks.” *Journal of Statistical Mechanics: Theory and Experiment* 2008 (10):P10008. [10.1088/1742-5468/2008/10/P10008](https://doi.org/10.1088/1742-5468/2008/10/P10008)
* Chadegani, Arezoo Aghaei, Hadi Salehi, Melor Md Yunus, Hadi Farhadi, Masood Fooladi, Maryam Farhadi, and Nader Ale Ebrahim. 2013. “A Comparison Between Two Main Academic Literature Collections: Web of Science and Scopus Databases.” *Asian Social Science* 9 (5).[10.5539/ass.v9n5p18](https://doi.org/10.5539/ass.v9n5p18)
* Eisberg, Joann. 2001. “Making a Science of Observational Cosmology: The Cautious Optimism of Beatrice Tinsley.” *Journal for the History of Astronomy* 32:263–80.[2001JHA....32..263E](https://ui.adsabs.harvard.edu/#abs/2001JHA....32..263E/abstract)
* Fleck, Ludwik. 1979. Genesis and Development of a Scientific Fact. Chicago; London: The University of Chicago Press. [http://www.press.uchicago.edu/ucp/books/book/chicago/G/bo25676016.html](http://www.press.uchicago.edu/ucp/books/book/chicago/G/bo25676016.html)
* Fortunato, Santo. 2010. “Community Detection in Graphs.” *Physics Reports* 486 (3-5):75–174. [10.1016/j.physrep.2009.11.002](https://doi.org/10.1016/j.physrep.2009.11.002)
* Harwit, Martin. 1973. “Astrophysical Concepts.” New York: Wiley. [1973asco.book.....H](https://ui.adsabs.harvard.edu/#abs/1973asco.book.....H/abstract)
* King, Ivan R. 1977. “Galaxies and Their Populations - the View on a Cloudy Day.” In *Evolution of Galaxies and Stellar Populations, Proceedings of a Conference at Yale University, May 19-21*, edited by Beatrice Tinsley and Richard B. Larson, 1–17. New Haven. [1977egsp.conf....1K](https://ui.adsabs.harvard.edu/#abs/1977egsp.conf....1K/abstract)
* Palla, Gergely, Illes J. Farkas, Peter Pollner, Imre Derenyi, and Tamas Vicsek. 2007. “Directed Network Modules.” *New Journal of Physics* 9 (6):186–86. [10.1088/1367-2630/9/6/186](https://doi.org/10.1088/1367-2630/9/6/186)
