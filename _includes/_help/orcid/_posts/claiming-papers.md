{% if include.ads %}<figure>
   <img src="/help/img/orcid-add.gif"  class="img-responsive" alt="a short animated image showing the orcid claiming process">
</figure>{% else %}<figure>
   <img src="/scixhelp/sciximg/scix-orcid-add.gif"  class="img-responsive" alt="a short animated image showing the orcid claiming process">
</figure>{% endif %}


### Recommended Method
If you care about having your ORCID claims searchable in {{ include.site }}.

1. **Make sure you're signed in to {{ include.site }}.** If you are not signed in already, [sign in here]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/user/account/login) or [create an account]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/user/account/register).

2. **Authenticate with ORCID.** Click on the ORCID button in the top navigation bar and follow the instructions.

3. **Enter a bit of extra information in your {{ include.site }} User Profile.** If you haven't done this already, [go to the ORCID settings page in your {{ include.site }} account]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/user/settings/orcid). Enter in 1) your current affiliation, and 2) any name variations under which you might have published. Submitting the form will grant {{ include.site }} permission to track your claims, allowing us to put your data in our system and marking it as trusted so that others can find it.

4. **Claim papers.** Search for your name variations in the search interface.
  Make sure ORCID mode is "on" (click on the ORCID button in the navigation bar to toggle the setting). Claim papers individually by clicking the Claim in ORCID button under a relevant search result. You can also claim multiple papers at once by selecting the check boxes next to the relevant search results{% if include.ads %} and clicking the Claim button in the ORCID Bulk Actions box in the right column.{% else %} and clicking the Claim from Scix option in the Bulk Actions dropdown menu.{% endif %}

5. **Check your claims in {{ include.site }}!** Your ORCID claims take up to **24 hours** to be indexed in {{ include.site }}. After that, you should be able to search for your ORCID papers in {{ include.site }} by using the search term: *orcid:[orcid id]*.

### Alternate Method
If you just want to use {{ include.site }} to send claims to your ORCID profile. (Most of your papers will likely still be eventually findable in {{ include.site }}, but they will be marked as less trusted than papers claimed using Method #1)

1. **Authenticate with ORCID.** Click on the ORCID button in the top navigation bar and follow the instructions.

2. **Claim papers.** Search for your name variations in the search interface. Make sure ORCID mode is "on" (click on the ORCID button in the navigation bar to toggle the setting). Claim papers individually by clicking the Claim in ORCID button under a relevant search result. You can also claim multiple papers at once by selecting the check boxes next to the relevant search results{% if include.ads %} and clicking the Claim button in the ORCID Bulk Actions box in the right column.{% else %} and clicking the Claim from Scix option in the Bulk Actions dropdown menu.{% endif %}

3. **It's not too late to change your mind!** You can always sign into your {{ include.site }} account (or create a new one) and submit the user profile information described above to facilitate indexing your claims in {{ include.site }}. Without performing this final step, some of your claims may not be properly indexed in {{ include.site }} due to our inability to match your name variations against the published records.
