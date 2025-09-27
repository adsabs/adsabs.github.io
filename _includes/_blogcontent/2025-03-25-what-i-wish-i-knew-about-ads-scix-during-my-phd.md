As astronomers we have been lucky to have the Astrophysics Data System (ADS) as part of our available research toolkit. Now thanks to the effort of the ADS team, this amazing tool will be available to all of NASA science through the [Science Explorer (SciX)](https://scixplorer.org/scixblog/scix). Of course, this also includes astrophysics, so as an astronomer I have been enjoying and using SciX everyday and I hope to convince you that you should too. 

## What Does the Transition Mean for Astronomers?

If you have been a daily ADS user, as I have been, you might have questions about this expansion to SciX. First and foremost: do not panic. All ADS links will continue to work and ADS will not cease to exist. In summary, SciX is the future and already has the same comprehensive astrophysics collections you've relied on, and should become your primary platform to search the literature.  This transition is particularly beneficial for researchers working at disciplinary intersections, such as astrochemistry, planetary sciences, and astrobiology. And if your advisor or friends ask about the classic form, reassure them that the classic form they are accustomed to remains available.

In this blog, I'll share some of my favorite Scix features that I wish I had known earlier in my academic career, and I hope to encourage you to start integrating SciX into your daily workflow.


### 1- Astronomy is still a main area of support and interdisciplinary content is a feature and not a bug. 

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads_to_scix_image1.png" />
<br>
</div>
<br>
The classic form is still available for those who prefer it. You can access it by selecting “Astrophysics” from the drop down menu on the top left. 


The inclusion of additional scientific disciplines in SciX creates new opportunities for cross-disciplinary collaboration and discovery. Just as in ADS, you can limit your search results to astronomy by using the filter ``collection:astronomy`` in your search query or by selecting "astronomy" under the filter options on the left side of the interface.
<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads_to_scix_image2.png" />
<br>
</div>
<br>

### 2- One account to rule them all. 

Your ADS account and account settings are fully integrated and shared with SciX, this includes your ADS libraries. Libraries are one of my favorite features of ADS and SciX and if you have not used them before I encourage you to create a SciX account, if you don’t have one already, and start organizing your research. Check out [this blog post](https://scixplorer.org/scixhelp/gettingstarted-scix/build-library) about how to create a library in SciX. 

Libraries can be designated as public, shared, or private to suit your needs. **A feature currently exclusive to SciX** is the ability to add annotations to saved papers—extremely useful for documenting why you saved a particular paper in a specific library. This is one extra small reason to do the change from ADS to SciX and a reminder that future development will focus on the SciX platform and new features will be made available on SciX.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads_to_scix_image3.png" />
<br>
</div>
<br>
Make sure you have an account to be able to save papers to your libraries. 

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads_to_scix_image4.png" />
<br>
</div>
<br>
This annotation feature is currently only available in SciX. The libraries are shared both between SciX and ADS. 


### 3- Second order operators and combinating queries

SciX is more than a tool to find a specific paper from the authors and the year. Check out my fellow ambassador [Yueyi's blog](https://scixplorer.org/scixblog/scix-earth-science-literature-review) on how she uses SciX as an Earth and Planetary Science Graduate Student. As she mentioned in her tip 2, [second-order operators](https://www.scixplorer.org/scixhelp/search/second-order) are incredibly powerful and useful to find relevant papers and stay on top of the literature; especially if you combine them. I will show you just a few of my favorites, but I encourage you to read the paper [“Second Order Operators in the NASA Astrophysics Data System“](https://scixplorer.org/abs/2020BAAS...52.0207K/abstract) to learn many more examples on how to get the most out of second order operators. <br>


One of my favorite uses is to keep up with the literature using the ``similar`` second-order operator. 
``Similar``, as the name suggests, finds similar abstracts in the SciX database. For example,  if you want to find recent papers posted on arXiv that are similar to previous papers on a particular topic, let’s say for example globular clusters, you might do something like:

``similar("Globular Cluster" -entdate:[NOW-7DAYS TO *]) entdate:[NOW-7DAYS TO *] bibstem:"arXiv"``

where the ``bibstem:”arXiv”`` parameter ensures results are limited to arXiv preprints, while the ``-entdate`` command inside the similar query makes the results to include the most recents papers. You can customize the inner similar query with various inputs, such as a specific paper, citations to a paper, or a particular author. Then, [set up email notifications](https://ads.harvard.edu/handouts/SciX_emailNotifications_handout.pdf) to receive daily or weekly updates on recent papers about your selected topics or authors. 
<br>

The ``similar`` operator can also accept arbitrary text as input using this format:


``similar("input text string”, input)``

<br>
Libraries can serve as input for the [4 second-order operators](https://ads.harvard.edu/handouts/SciX_2ndorder_operators.pdf) : ``similar``, ``trending``, ``useful``, and ``reviews``. By clicking "View as search results" and then "Explore", you can select any of these operators, generating a query like: 

``useful(docs(library/bcynVbTNTK6I__4hHDhAAA))``
<br>
which you can further modify and explore.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads_to_scix_image5.png" />
<br>
</div>
<br>
The "View as search results" option allows you to transform your library into a searchable query, enabling you to apply powerful second-order operators like similar, trending, useful, and reviews to your curated collection of papers.


### 4-Discover Resources Beyond Traditional Publications

SciX is more than just a simple repository for articles. For example, you can specifically search for software relevant to your research area. To limit the search to software you can use doctype and add the relevant search commands. For example,
<br>
``doctype:software collection:astronomy abs:"LISA"``
<br>
will search for software that mentions the LISA mission in the abstract. 
<br>

Or you can search for Zenodo repositories with data:Zenodo. For example:
<br>
``data:Zenodo year:2024 title:"Black Hole"``
<br>
will search for Zenodo data products that have “black hole” in the title. 
<br>
 
SciX can also help you explore some more lighthearted research questions, such as how many astronomers have acknowledged their feline companions in their papers. You can discover this by searching with:"

``ack:"My Cat" collection:astronomy``
<br>

This blog post wasn't meant to be a comprehensive how-to guide for SciX/ADS—just a collection of some of my favorite features that I hope gives you the confidence to dive in and explore SciX more. I hope I showed you that if you are an astronomer like me, you can make the switch to SciX without any concerns. It is built on the same great resource you've relied on, just with some cool new features and more to come. So go explore, play around with those queries, and discover what this wonderful tool has to offer for your research journey!
