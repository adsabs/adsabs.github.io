There are two ways to create an {{ include.site }} library:

  1. From the [search results page]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}{% if include.ads %}/#search/q={% else %}/search?q={% endif %}star), select your relevant papers, and {% if include.ads %}select the **Add papers to library** button. Fill in a library name and press submit.{% else %}select **Bulk Actions** and then **Add to library**. Fill in a library name and press submit.{% endif %}

  2. Go the **My Account** drop down and select **{{ include.site }} Libraries**. Press the {% if include.ads %}**Create a library**{% else %}**Add New Library**{% endif %} button.

{% if include.ads %}<img class="img-responsive" src="{{ site.baseurl }}/help/img/library_screenshot.png" alt="a screenshot of {{ include.site }} search results interface showing {{ include.site }} libraries button"/>{% endif %}

It is possible to modify the name and description of the library you have created. To do this, simply navigate to the {{ include.site }} Libraries page from the **My Account** drop down, at the top right of the web interface. Once there, you can select your library of interest, and {% if include.ads %}press **edit** on the attribute you would like to modify.{% else %}click the gear icon to modify the attributes you would like to change.{% endif %}

{% if include.ads %}To delete any of the records in your library, simply navigate to the library and press the red **x** next to the bibcode you do not want in the library.  To delete the entire library, navigate to the library page, click on the "View Editing Options" button and select the "Delete library" option.{% else %}To delete any of the records in your library, first select the record you want to remove, then click the **Delete** button.  To delete the entire library, click the gear icon, then select the "delete library" button.{% endif %}  Once deleted, a library is gone forever, so click with caution!
