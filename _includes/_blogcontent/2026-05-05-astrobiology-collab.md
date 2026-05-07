<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_nasa-astrobiology-poster.jpg" 
	 alt="Illustration of a planet with diverse microbial life beneath a star-filled galaxy"
	 class="img-responsive"
	 style="float: left; margin: 0 20px 10px 0; width: 300px;">
Keeping track of scientific publications sounds straightforward - until you’re working in a field as interdisciplinary as astrobiology. Astrobiology sits at the intersection of astronomy, geology, chemistry, biology, and planetary science, which means its research is scattered across a wide range of journals, repositories, and formats. For teams trying to maintain a comprehensive, up-to-date bibliography, the task quickly becomes an ongoing challenge.

With the launch of Science Explorer (SciX) and its growing focus on interdisciplinary science, we’ve had the opportunity to collaborate with the [NASA Astrobiology Program](https://science.nasa.gov/astrobiology/) to rethink how their publications are tracked, curated, and shared. What began as an effort to streamline internal tracking has evolved into something much more impactful: a living, publicly accessible [NASA Astrobiology bibliography](https://scixplorer.org/public-libraries/UTViEyO9T7izQP7i_r6yqA) that now helps power how the program shares its research with the world.

{% if include.ads %}{% else %}<h3 style="margin-top: 0; color: #5FBFAE;">Building the Astrobiology Library</h3>             
{% endif %}
At its core, this project is driven by a simple goal: to make astrobiology research more findable, organized, and usable. Through SciX, we’ve built a library that aggregates publications from multiple sources, normalizes metadata, and ensures consistency across records.

One of the most rewarding outcomes of this collaboration is that the SciX library is no longer just an internal tool. It now serves as the publications bibliography featured on the NASA Astrobiology website, providing a reliable, continuously updated resource for researchers, collaborators, and the public.

The collaboration came together pretty organically. We connected with the NASA Astrobiology team to discover more literature to add to our growing collections. We compared notes on publication tracking workflows, and quickly found a path forward that built on what they were already doing - just with a bit more automation and structure layered in.

It started with a simple CSV list of publications maintained by the Astrobiology team. From there, we developed a Python-based workflow to transform that list into a fully realized SciX library: Using the SciX API, we first check which publications already exist in the system. For anything missing, we generate new records using curation-focused scripts that clean, standardize, and enrich the metadata. Once everything is in place, we use the API again to maintain a dedicated SciX Library that brings the full set of NASA Astrobiology publications together in one place. The Astrobiology team now includes us on their monthly publication digest, which means this isn’t a one-time effort - it’s a sustained, evolving collaboration that keeps the library continuously up to date.
{% if include.ads %}{% else %} 
<h3 style="margin-top: 0; color: #5FBFAE;">Using the Astrobiology Library</h3>

As a researcher, you can access the Astrobiology library via [the link here](https://scixplorer.org/public-libraries/UTViEyO9T7izQP7i_r6yqA) or from the “For Researchers” dropdown menu on the [NASA Astrobiology Program](https://science.nasa.gov/astrobiology/) home page. 

<div style="display: flex; gap: 20px; align-items: flex-start;">
<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure1.png" 
	 alt="SciX interface showing the NASA Astrobiology Publications library with a list of papers and sorting options"
	 class="img-responsive"
	 style="width: 400px; margin: 0 0 10px 0; border: 3px solid #049DD9; border-radius: 6px;">
	 
<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure2.png" 
	 alt="SciX library sorting controls showing a dropdown menu and sort order toggle"
	 class="img-responsive"
	 style="width: 250px; border: 3px solid #049DD9; border-radius: 6px;">
</div>

Within the Astrobiology library view, you can sort the papers several ways, including `Time Added` to see the latest additions to the library, `Date` to see the latest publications, or `First Author` to find a specific paper. 

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure3.png" 
	 alt="SciX article view with options for full text, citations, data products, and sharing"
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 650px; border: 3px solid #049DD9; border-radius: 6px;">
   
The icons on the right side of each individual entry provide you quick links to the abstract, full text, references and citations, data products, and copied URL or citation. Here you can quickly initiate the most common requests with regards to the astrobiology literature.

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure4.png" 
	 alt="SciX paper list with one entry expanded to display its abstract and action icons"
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 650px; border: 3px solid #049DD9; border-radius: 6px;">
   
To read the abstract of any paper, you can click on the down caret or the note-taking icon. 

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure5.png" 
	 alt="Screenshot of a SciX by ADS article detail page for a paper titled 'Analytic Light Curve for Mutual Transits of Two Bodies Across a Limb-darkened Star' by Gordon, Tyler A. and Agol, Eric. The top center shows the title, authors, and badges indicating the article is refereed and an 'Article.' A long abstract paragraph appears beneath. On the right of the abstract is a bibliographic table listing: publication (The Astronomical Journal, Volume 164, Issue 3, id.111, 23 pp.), publication date (September 2022), DOI links, arXiv ID, bibcode, collection (astronomy), keyword chips (e.g., Exoplanets, Exoplanet detection methods, Binary stars, Exoplanet systems), UAT-generated keywords, and bibgroups such as Kepler and NASA Astrobiology. At the bottom is an 'E-Print Comment(s)' field noting page and figure counts plus a GitHub code link, and a 'Make Corrections' link. On the left side, a vertical navigation pane lists sections and resources: Full Text Sources (with IOP and Preprint marked OPEN), Data Products (SIMBAD (12)), Related Materials (a proposal link), and sections like Abstract, Citations, References, Credits, Mentions, Co-Reads, Similar Papers, Volume Content, Graphics (18), Metrics, and Export Citation."
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 650px; border: 3px solid #049DD9; border-radius: 6px;">
 
If you click on a paper’s title, you can explore all the resources of our full-featured [Abstract View](https://www.scixplorer.org/scixhelp/actions-scix/article-view) of that paper. The individual abstract view is a hub for identifying and accessing a wealth of resources related to that particular astrobiology resource.

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure6.png" 
	 alt="Screenshot of part of the SciX by ADS interface, focused on the controls above a library entry. Near the top is a dark navigation bar with menu items (About, Help, Account) and a moon icon. Below, a blue share icon button appears on the right. In the middle of the image, a blue, oval callout surrounds a link labeled “View as search results” and a row of small blue icons below it (edit, dropdown arrow, document, list, database, and share), indicating tools for changing how the library contents are displayed."
	 class="img-responsive"
	 style="float: left; margin: 0 20px 10px 0; width: 250px; border: 3px solid #049DD9; border-radius: 6px;">

“View as search results” takes you out of the library view and into a standard SciX results view, where you can [apply filters](https://www.scixplorer.org/scixhelp/search-scix/filter), [visualize relationships](https://www.scixplorer.org/scixhelp/actions-scix/visualize) ('Author' or 'Paper Networks', 'Concept Clouds', or metrics), and [request papers based on their relationship to those in this library](https://www.scixplorer.org/scixhelp/search-scix/second-order), or a subset of it, ('Reviews', "Userful', or 'Similar').  Here you can perform a thorough literature review of an astrobiology topic or otherwise engage with the astrobiology literature in a more individualized manner. 

<img src="{{site.baseurl}}/blog/images/blog_2026-05-05_figure5.png" 
	 alt="Screenshot of the SciX by ADS search results page with explanatory overlays. At the top is a search bar showing a library search that returned 4,966 results. A black header bar contains the SciX logo, collection selector (Astrophysics), and links such as Tour, Feedback, ORCiD, About, Help, and Account. On the left, a vertical filters panel is visible, topped by a histogram labeled 'Year(s)' and followed by many collapsible filter categories (Author, Collections, Refereed, Institutions, Award, Keywords, Publications, Bibgroups, SIMBAD Objects, NED Objects, Data, Vizier Tables, Publication Type, UAT, and 'Show hidden filters'). A large vertical annotation reads 'Many Filters to Narrow Your Selection.' The main pane shows a numbered list of article titles with authors, dates, and journals. Above the list are controls for sorting by Date and buttons for 'Bulk Actions' and “Explore.” The Explore menu is open, showing visualization and analysis tools such as Overview, Metrics, Author Network, Paper Network, Concept Cloud, Results Graph, and Citation Helper, plus operations like Trending, Reviews, Useful, and Similar. Two blue annotated labels on the right say 'Visualize relationships in literature' pointing at the visualization tools, and 'Find papers based on sets of papers' pointing at the operations list."
	 class="img-responsive" 
	 style="display: block; margin: 1em auto; width: 650px; border: 3px solid #049DD9; border-radius: 6px;">
	 
For more assistance with using SciX libraries or to get started creating your own, review our help section starting with “[Creating and Editing a Library](https://www.scixplorer.org/scixhelp/libraries-scix/creating-libraries).”
{% endif %}

<div style="clear: both; margin-bottom: 10px;"></div>
