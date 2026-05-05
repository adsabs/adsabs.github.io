<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_nasa-astrobiology-poster.jpg" 
	 alt="Illustration of a planet with diverse microbial life beneath a star-filled galaxy"
	 class="img-responsive"
	 style="float: left; margin: 0 10 1em 1em; width: 300px;">
Keeping track of scientific publications sounds straightforward - until you’re working in a field as interdisciplinary as astrobiology. Astrobiology sits at the intersection of astronomy, geology, chemistry, biology, and planetary science, which means its research is scattered across a wide range of journals, repositories, and formats. For teams trying to maintain a comprehensive, up-to-date bibliography, the task quickly becomes an ongoing challenge.

With the launch of Science Explorer (SciX) and its growing focus on interdisciplinary science, we’ve had the opportunity to collaborate with the [NASA Astrobiology Program](https://science.nasa.gov/astrobiology/) to rethink how their publications are tracked, curated, and shared. What began as an effort to streamline internal tracking has evolved into something much more impactful: a living, publicly accessible [NASA Astrobiology bibliography](https://scixplorer.org/public-libraries/UTViEyO9T7izQP7i_r6yqA) that now helps power how the program shares its research with the world.

<h3 style="margin-top: 0; color: #5FBFAE;">Building the Astrobiology Library</h3>             

The collaboration came together pretty organically. We connected with the NASA Astrobiology team to discover more literature to add to our growing collections. We compared notes on publication tracking workflows, and quickly found a path forward that built on what they were already doing - just with a bit more automation and structure layered in.

It started with a simple CSV list of publications maintained by the Astrobiology team. From there, we developed a Python-based workflow to transform that list into a fully realized SciX library. Using the SciX API, we first check which publications already exist in the system. For anything missing, we generate new records using curation-focused scripts that clean, standardize, and enrich the metadata. Once everything is in place, we use the API again to maintain a dedicated SciX Library that brings the full set of NASA Astrobiology publications together in one place. The Astrobiology team now includes us on their monthly publication digest, which means this isn’t a one-time effort - it’s a sustained, evolving collaboration that keeps the library continuously up to date.

At its core, this project is driven by a simple goal: to make astrobiology research more findable, organized, and usable. Through SciX, we’ve built a library that aggregates publications from multiple sources, normalizes metadata, and ensures consistency across records.

One of the most rewarding outcomes of this collaboration is that the SciX library is no longer just an internal tool. It now serves as the publications bibliography featured on the NASA Astrobiology website, providing a reliable, continuously updated resource for researchers, collaborators, and the public.

<h3 style="margin-top: 0; color: #049DD9;">Using the Astrobiology Library</h3>

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure1.png" 
	 alt="SciX interface showing the NASA Astrobiology Publications library with a list of papers and sorting options"
	 class="img-responsive"
	 style="float: right; margin: 0 10px 1em 1em; width: 300px;">
As a researcher, you can access the Astrobiology library via [the link here](https://scixplorer.org/public-libraries/UTViEyO9T7izQP7i_r6yqA) or from the “For Researchers” dropdown menu on the [NASA Astrobiology Program](https://science.nasa.gov/astrobiology/) home page. 

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure2.png" 
	 alt="SciX library sorting controls showing a dropdown menu and sort order toggle"
	 class="img-responsive"
	 style="float: right; margin: 0 10px 1em 1em; width: 300px;">
Within the Astrobiology library view, you can sort the papers several ways, including `Time Added` to see the latest additions to the library, `Date` to see the latest publications, or `First Author` to find a specific paper. 

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure3.png" 
	 alt="SciX article view with options for full text, citations, data products, and sharing"
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 550px;">
   
The icons on the right side of each individual entry provide you quick links to the abstract, full text, references and citations, data products, and copied URL or citation. Here you can quickly initiate the most common requests with regards to the astrobiology literature.

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure4.png" 
	 alt="SciX paper list with one entry expanded to display its abstract and action icons"
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 550px;">
   
To read the abstract of any paper, you can click on the down caret or the notetaking icon. If you click on a paper’s title, you can explore all the resources of our full-featured [Abstract View](https://www.scixplorer.org/scixhelp/actions-scix/article-view) of that paper. The individual abstract view is a hub for identifying and accessing a wealth of resources related to that particular astrobiology resource.

“View as search results” takes you out the library view and into a standard SciX results view, where you can [apply filters](https://www.scixplorer.org/scixhelp/search-scix/filter), [visualize relationships](https://www.scixplorer.org/scixhelp/actions-scix/visualize) (authors, papers, metrics, concepts), and [request papers based on their relationship to those in this library](https://www.scixplorer.org/scixhelp/search-scix/second-order) or a subset of it (similar, review, useful).  Here you can perform a thorough literature review of an astrobiology topic or otherwise engage with the astrobiology literature in a more individualized manner. 

For more assistance with using SciX libraries or to get started creating your own, review our help section starting with “[Creating and Editing a Library](https://www.scixplorer.org/scixhelp/libraries-scix/creating-libraries).”  

<div style="clear: both; margin-bottom: 40px;"></div>
