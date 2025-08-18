#### Linking accounts

If you have an account in our legacy system, {{ include.site }} Classic, it is possible to import libraries from your old account into the new {{ include.site }} interface. 

First login with your normal credentials on the new {{ include.site }}, and then navigate to the *Customize Settings* page:

<img class="img-responsive" src="{{ site.baseurl }}/help/img/import_help_01.png" alt="a screenshot of the location of the Customize Settings button"/>

Once there, select **Import Libraries** in the left panel:

<img class="img-responsive" src="{{ site.baseurl }}/help/img/import_help_02.png" alt="a screenshot of {{ include.site }} Classic library import with the form filled in"/>

If you are linking a {{ include.site }} Classic account, you will need to specify your email, your password used for your {{ include.site }} Classic account, and the mirror at which you have an account.

If you need to link a different account, then simply press **Sign into a new Classic account**

<br>

#### Importing libraries

Once you have successfully connected your {{ include.site }} Classic account with the new {{ include.site }}, you now have the option to import your {{ include.site }} Classic libraries into the new {{ include.site }}.

<img class="img-responsive" src="{{ site.baseurl }}/help/img/import_help_03.png" alt="a screenshot after the Import all Classic libraries button has been pressed"/>

You can see my original {{ include.site }} Classic library now exists in the new {{ include.site }}:

**{{ include.site }} Classic**
<img class="img-responsive" src="{{ site.baseurl }}/help/img/import_help_04.png" alt="a screenshot of the library in {{ include.site }} Classic"/>

**The new {{ include.site }}**
<img class="img-responsive" src="{{ site.baseurl }}/help/img/import_help_05.png" alt="a screenshot of the library in the new {{ include.site }}"/>



<u><b>ATTENTION</b>: the following rules are used to import your libraries into the new interface</u>

  1. **All the libraries you own** will be imported, and created with their 'Name' and 'Description' from {{ include.site }} Classic. Entries for all bibcodes for each library will be created also. However, notes attached to individual entries within a library will not be imported and are not supported in the new {{ include.site }}.
  2. If you have a library in the new {{ include.site }} with the same name, it will **merge** the documents from your {{ include.site }} Classic library into the new {{ include.site }}; **the new {{ include.site }} takes precedent**.
  3. You can repeat this process as many times as you wish, but must keep in mind the actions of 2. and 3.
  4. You **cannot undo** your import, you must delete a library and re-import if you make a mistake.

<br>

## FAQ

 * "*I can't seem to authenticate my {{ include.site }} Classic account*"

   Make sure you i) actually have a {{ include.site }} Classic account, and ii) that you selected the correct mirror - otherwise it won't work. If you are still running into trouble, then contact us at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}</a>.

 * "*I can't seem to import my libraries*"

   You should make sure you actually have any libraries to import from your {{ include.site }} Classic library. It is more than likely you are trying to import from an account that does not have any. However, if you do have libraries and keep running into this problem then contact us at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}.

 * "*I can't find the export format for the software I'm trying to use*"

   If you think we should supply a format for another third-party software that is used then let us know at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}</a>.

<br>
