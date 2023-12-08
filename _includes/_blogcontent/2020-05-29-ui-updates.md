
A number of changes have come to ADS over the past few months, some of which you may have missed. Read on for an overview of some of the bigger updates to the site. If you want to stay up to date on changes with ADS, [sign up](http://eepurl.com/ggoxhn) for our monthly newsletter or check in occasionally with our [What’s New page]({{ site.baseurl }}/help/whats_new/).

## myADS: Personal Email Notifications
The myADS service, which notifies subscribers via email about new papers relevant to their interests, has continued to operate out of the Classic system for the past few months while the replacement system was in development. We’re happy to announce that the new replacement myADS system is now ready!

The [setup page](https://ui.adsabs.harvard.edu/user/settings/myads) can be found within your account settings. Here, you can either set up new notifications, or if you were a subscriber of the Classic myADS notifications, you can import your existing settings from Classic.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-05-01_myads.png" />
<em>myADS setup</em>
</div>
<br>

A quick overview: emails are generated daily (on weekdays) and/or weekly (over the weekend). Daily emails let you know about new arXiv papers, while the weekly emails are geared towards notifications of newly published articles. If you used the Classic myADS, all of the notifications you had set up there have their counterparts in the new myADS, though there are some small differences. We’ve also added one additional notification type, designed to allow for more general notifications. Full documentation for the new myADS is available [here](../help/userpreferences/myads).

## Library Collaborators
One of the most-requested features for ADS libraries has now arrived: the ability to share library editing privileges with collaborators. There are 4 privilege levels available:
* Owner: A library can only have one owner and you are automatically the owner for any library you’ve created. Library owners can add and delete papers from libraries, edit the library name and description, add and manage collaborators, and delete the library.
* Admin: A library can have multiple admin-level users. Library admins can do everything library owners can do, except delete the library. Note that admin users can add and manage any collaborators, except for the library owner.
* Read & write: A user with read & write privileges can add and remove papers from libraries. 
* Read: A user with read privileges can view a private library.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-05-01_library_collaborators.png" />
<em>Manage Library Collaborators screen</em>
</div>
<br>

To add a collaborator, go to the library and click the Manage Access tab. Either click the button to “Add Collaborator” and fill out the form, or edit the permission levels of existing collaborators directly. Note that collaborators will need to already have an ADS account in order for you to add them, and that collaborators will be emailed when their permissions are added or edited.

As noted above, libraries can only have one owner, so owner-level permissions cannot be assigned here. To transfer library ownership to another user, click the Transfer Ownership button, also on the Manage Collaborators tab, and fill out the email address of the new owner. As with collaborators, the new owner must already have an ADS account, and they will be emailed when ownership is transferred to them.

## Sort by Score

By default, most searches in ADS return results sorted in reverse chronological order. (Though some special searches, such as those using a [second-order operator]({{ site.baseurl }}/help/search/second-order), sort results according to their own internal algorithms.) This is useful if you’re searching for recent papers, but may be less useful if you’re looking for a popular older paper that would otherwise be swamped by more recent articles. This is especially true if you’re not using search tags, such as *year:*, but are simply entering your search terms in the search bar to search all metadata at once.

The new score sort is ideal for these types of searches. The score sort is similar to a relevancy sort: it combines the search engine’s rating of how well a given paper matches the search terms along with a measure of a paper’s popularity (a date-weighted combination of citation and download statistics). So, papers that are a good match to the given search terms *and* are more popular will rank more highly than similar less-popular papers. 

A search for Nobel Prize-winning astronomer Adam Riess shows the difference. Searching by his last name and sorting by date ([Riess](https://ui.adsabs.harvard.edu/search/q=Riess&sort=date%20desc%2C%20bibcode%20desc&p_=0)) returns the most recent papers first; some of these likely cite him in the abstract, include him or someone with the same name as *Nth* author, or otherwise mention his name in passing. Changing the sort to score order ([Riess](https://ui.adsabs.harvard.edu/search/p_=0&q=Riess&sort=score%20desc%2C%20bibcode%20desc)), however, returns his Nobel Prize-winning papers, and other highly cited works, at the top of the list.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2020-05-01_score_sort.png" />
<em>Example of sorting by score</em>
</div>
<br>

## BibTeX Custom Citation Keys
BibTeX citation keys, used in the LaTeX citation commands such as ``\citep{cite_key}``, have long been auto-generated and set to the bibcode in ADS exports. This had the benefit of ensuring unique citation keys for each paper in a bibliography but were generally fairly opaque and hard to remember---especially troublesome if you were trying to type the LaTeX citation command, including the cite key, from memory. 

The export service now allows you to generate custom-formatted citation keys when exporting to the BibTeX or BibTeX ABS format. This can be set in your [search settings](https://ui.adsabs.harvard.edu/user/settings/application) under “BibTeX [ABS] Default Export Key Format.” Citation key custom formats can include any combination of the bibcode, *N* number of authors, the publication, and the year. In addition, you can choose to add auto-generated sequential lettering (a, b, c, …) to the generated cite keys if duplicates appear in the exported set. More information on the custom format setup is available on the search settings page.

## Exclude Selected Results
On the search results page, the ability to manually select a number of papers and limit the results to just those papers has been available for some time. We’ve recently added the inverse ability: to manually select a number of papers and exclude them from the results set. To try this, select one or more papers in the search results set, then click the Exclude button in the right sidebar. The selected set of articles, whether “limit to” or “exclude” has been selected, will appear in the search bar using the *docs( )* syntax.

## Export via the API

### Sort order
Users of our API who export citation data in BibTeX and other formats (including those building bibliography management tools) were previously required to pass in a sort order, such as sorting by date. Otherwise, the returned export data was automatically sorted in reverse chronological order. We’ve recently tweaked the export service to allow the exported citation data to be returned in the same order as the input bibcodes are provided to the service. This makes it easier for our API users to match the input bibcodes and exported citation data. To activate this mode, set the sort parameter equal to “no sort” in your API call.

### Journal format
By default, journal names in the BibTeX, BibTeX ABS, and AASTeX export formats are formatted using the AASTeX macros if one exists for the journal (e.g. the Astrophysical Journal is formatted as ``\apj``). API users can now control this behavior using the “journalformat” parameter. Setting this parameter equal to 1 returns the default, the AASTeX macros. Setting it to 2 returns the journal abbreviations (e.g. ApJ for the Astrophysical Journal), while setting it to 3 returns the full journal name.

<br>
The above are just some of the new and improved features we’ve added to ADS over the past few months. For the full list, check out our [What’s New page]({{ site.baseurl }}/help/whats_new/) and consider subscribing to our What’s New [email newsletter](http://eepurl.com/ggoxhn). And if you have a feature suggestion for us, [send us an email](mailto:adshelp@cfa.harvard.edu) and let us know.

