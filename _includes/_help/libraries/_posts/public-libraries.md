You can make your library publicly viewable to non-{{ include.site }} users {% if include.ads %}by going to the **Manage Access** tab within your {{ include.site }} Libraries section under **My Account**. Press the **Make this library public** button to make it public.{% else %}First navigate to the {{ include.site }} Libraries page from the My Account drop down, then click on the library you'd like to make public. Click on the gear icon to access the library settings, then toggle Make library public? and click Save to make it public.{% endif %} This button generates a unique URL that you can give to people to view your library. You have the option to make your library private again in the future, in the same part of the interface. By default, all libraries are private.

You can also add collaborators to a library to allow other users to view, edit, and/or administrate your library. Available permissions:
* *Read Only*: Can view the contents of a private library
* *Read & Write*: Can view a library and add/remove records to it
* *Admin*: Can view a library, add/remove records, edit the library name and description, and add/remove other collaborators

To add a collaborator:
{% if include.ads %}1. Go to the **Manage Access** tab and scroll to the **Collaborators** section.
2. Click the **Add Collaborator** button.{% else %}1. Click the check mark button and scroll to the Collaborators section.{% endif %}
3. Fill out the email address of the user you'd like to add as a collaborator (they must have an {{ include.site }} user account under this email address) and choose their permission level.
4. Click **Add Collaborator** to finish adding the user. The user will be emailed to notify them of their updated permissions.

Editing collaborators' permissions or revoking their access can be done directly from the **Manage Access** tab.

*Note that you must be the library owner or have admin permissions to add, edit, or remove collaborators.*
