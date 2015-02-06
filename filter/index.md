---
layout: page
title: Filter your results
permalink: /filter/
---


#**Results list**#

A list of papers that match your initial query will be displayed and you will be able to further refine your query by using our "Limit Your Search" options or to view additional information about the articles that were returned.

The ADS utilizes bibliographic codes (bibcodes) to identify literature in our database.  Using a standard bibliographic format, as explained below, we can easily identify different articles and users can efficiently search for them.
The bibliographic code is a 19 digit identifier which describes the journal article. The format was originally adopted by the SIMBAD and NED projects, and follows the syntax: 
YYYYJJJJJVVVVMPPPPA where: 

 * YYYY: Year of publication 
 * JJJJJ: A standard abbreviation for the journal (e.g. ApJ, AJ, MNRAS, Sci, PASP, etc.). A list of abbreviations is available. 
 * VVVV: The volume number (for a serial) or an abbreviation that specifies what type of publication it is (e.g. conf for conference proceedings, meet for Meeting proceedings, book for a book, coll for colloquium proceedings, proc for any other type of proceedings). 
 * M: Qualifier for publication:
    * E: Electronic Abstract (usually a counter, not a page number)
    * L: Letter
    * P: Pink page
   * Q-Z: Unduplicating character for identical codes 
 * PPPP: Page number. Note that for page numbers greater than 9999, the page number is continued in the m column. 
 * A: The first letter of the last name of the first author. 

The fields are padded with periods (.) so that the code is always 19 characters long. The journal is left-justified within its 5 characters, and the volume and page are right-justified. New journal abbreviations should be unique, and follow existing naming conventions. As an example, the bibliographic code: 
1992ApJ...400L...1W corresponds to the article: Astrophysical Journal Letters volume 400, page L1. 

##**Limit your search**##

Once you have a results list from an initial query you can use our filters to further refine your search.  Please note that your results list will change each time you apply a limit.  Each limit appears above the top of the results list and can be undone simply by clicking on the *x* in each box (or clearing all filters but chosing "Clear all."  Currently we have the following options available:

Clicking on a **>** will detail your results for that filter.

Clicking on any of the listed terms within a filter will automatically apply that result as a filter; if you want to choose more than one term within a specific filter you must first check the boxes next to the terms you want to choose and then choose the desired application ( **and**, **or** or **exclude**) from the **apply** box in that section.
[**EXAMPLE**](examples#filtering-within-facet)

  * *Top papers*--here you can chose to limit your search to the first xxx results (where you chose the number xxx either by typing in the number or using the scroll bar.)  Hitting apply activates this option.  You may return to the original results by using the reset button.
  * *Authors*--here you may chose to limit your search to include or exclude individual authors.  To do this choose one or more authors and the *apply* function will activate.  Here you can choose to "and", "or" or "exclude" authors from your resulting list. 
  * *Database*--here you may chose to add results from the database(s) that were not selected in your original query.  You may also chose to exclude a database that was initially chosen.  
  * *Keywords*--here you may chose to narrow your results by including or excluding keywords that were found in the results of your original query.  
  * *Publications*--here you may chose to narrow your results by including or excluding journals that were found in the results of your original query. 
  * *Refereed status*--here you may chose to include or exclude refereed or non-refereed publications
  * *Bib Groups*--here you may chose to include or exclude results from different Bib Groups within the ADS
  * *Grants*--here you may chose to include or exclude results that reference grant numbers that were recognized in the original search
  * *Data*--here you may chose to include or exclude results that contain data in various archives (e.g. CDS, HEASARC, CXO, NED)
  * *Vizier Tables*--here you may chose to include or exclude articles that have Vizier Tables
  * *Publication Year*--here you may chose to limit your results to a specified time period by typing in the year range or using the provided slide bar

##**Understanding the Results**##

Your results are ranked according to your query and filtering options that you have applied.

**export** Working with the list you can select articles and export the resulting lists in various formats (e.g. to ADS Classic, Endnote, Bibtex or AAStex)

**sort**  You can also sort your results by relevance, by date, by citation number or by popularity (all of these can be returned in ascending or descending order)

##**Analyze the results**##

   * **Citation Helper** Clicking on this option gives a list of 10 results which consists of publications that cite and/or are cited by papers in the list you just submitted, but they were not in this list. The process closely resembles the network approach of establishing "friends of friends". Assuming that the bibcodes provided are all valid, it is still possible that no results will be returned. If results are returned, they have a score associated with them. This score essentially reflects how many "friends" know these other "friends".
   * **Metrics**

Currently the following metrics are provided for a list of publications.  If you select records from your search results, the metrics will be displayed for the selected articles.  If you do not select any records a dialog box will appear and you may select all of your results (to a maximum of 3000) or adjust the number of papers to be analyzed by using the slide bar (choosing a number (n) on the slide bar will return the metrics for the first n papers in your current result list.)  

   * Number of papers 
   * [Normalized paper count](metricsdefs#Normalized paper count)
   * Number of citing papers 
   * Total citations 
   * [Normalized citations](metricsdefs#Normalized citations) 
   * Average of citations 
   * Median of citations 
   * [h-index](metricsdefs#h-index) 
   * [g-index](metricsdefs#g-index) 
   * [i10-index](metricsdefs#i10-index) 
   * [e-index](metricsdefs#e-index) 
   * [m-index](metricsdefs#m-index) 
   * [tori-index](metricsdefs#tori-index)
   * [riq-index](metricsdefs#riq-index)

Note that we do not remove self-citations based on author name, because of obvious author disambiguation problems. We apply a list-based removal of self-citations.

##**Visualizing the Results**##

The *View* button allows you to visualize your results in various ways.

   * **Author Network** allows you to illustrate author networks within ADS search results.  More information about how to use the Author Network is available with the tool.   You can zoom, filter and search author info in this mode and then apply these restrictions to your results list.
   * **Objects skymap** allows you to select objects or areas on a Skymap and to then use this information to filter your results list.  More information about how to use the Object Skymap is available with the tool.  You can choose a coordinate system (J2000 or Galactic), which layer(s) you would like to see and which object(s) or area you would like to include in your results.  
   * **Word Cloud** shows you a diagram which includes interesting terms from your ADS search results.  You can use these words to filter your results.  More information about how to use the word cloud is available with the tool.  

##**Export**##
Use this button to export your search results in different formats.  Currently available options are ADS Classic, BibTeX, AASTeX and Endnote.

##**Sort**##
Use this button to resort your query results.  You can sort by date, by citations and by popularity and each of these can be sorted in ascending or descending order.  When a sorting option is selected, a button which allows you to undo the sort is visible.  

##**Available links**##

Following each bibcode is a list of letters which indicate what data are available for the article.  

 * C   (Citations)   A list of articles that cite the current article. (This list is not necessarily complete)
 * D   (On-line Data)  Links to on-line data at other data centers.
 * E   (Electronic Article)  Links to the on-line version of the article. These on-line versions are in HTML format for viewing on-screen, not for printing.
 * F   (Printable Article)   Links to on-line articles in PDF or Postscript format for printing.
 * G   (Gif Images)  Links to the images of scanned articles in the ADS Article Service.
 * L   (Library Entries)   Links to entries in the Library of Congress and other on-line library system.
 * N   (NED Objects)   Access to the lists of objects for the current article in the NED database.
 * R   (References)  A list of articles referred to in the current article. For older articles these lists are not necessarily complete, they contain only references to articles that are in the ADS database. For some articles that are on-line in electronic form, the "R" link points to the on-line reference list, and therefore the complete list of references in that article.
 * S   (SIMBAD Objects)  Access to the lists of objects for the current article in the SIMBAD database.
 * T   (Table of Contents)   Links to the list of all articles in a books or proceedings volume.
 * X   (arXiv e-print)   Links to on-line articles in the arXiv database.


##**Individual article view**##

Clicking on the bibcode of an individual article will bring you to a page showing the abstract view for the chosen article including a DOI link, keywords and arXiv identifier. On this page you will find tab links to lists of:
   
   * References in the article
   * Citations to the article
   * Co-Reads of the article (papers that have been read by people who read this article)
   * Similar articles
   * Table of contents (if the article is part of a collection (e.g. a book or conference proceeding), you can see the entire table of contents for the collection.)  

You can also generate the metrics for the individual article by selecting metrics from the Analyze list.

 In addition you will find links to Full Text Sources (Open Access resources are indicated by an open lock) and Data Products.   Also shown will be a list of Suggested Articles which are suggested based upon the information for the chosen article.  We also provide links to ADS private libraries, Twitter, Facebook, LinkedIn and Mendeley.
