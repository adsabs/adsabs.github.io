---
title: ADS Bibliographic Libraries | ADS API
---


# Bibliographic Libraries API

{:toc}

ADS allows researchers to create and curate their own collections of papers (bibliographic libraries). If you use these endpoints
you are accessing the `resources` that belong to a particular user (the permission is granted through the OAuth token).



## Work with Libraries

	GET /libraries/

Obtains all the libraries that belong to the requesting user, along with some additional metadata.


<%= headers 200 %>
```json
{}
```


### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library



### Return data

Name | Type | Description
-----|------|-----------------------
`name` | `string` | Name of the library
`id` |`string`| ID of the library
`description`| `string`| Description of the library
`num_documents`| `int` | Number of documents in the library
`date_created`| `string`| ISO date library was created
`date_last_modified`| `string`| ISO date library was last modified
`permission`| `string`| Permission type, can be: 'read', 'write', 'admin', or 'owner'
`public`| `boolean`| True means it is a public library
`num_users` | `int`| Number of users with permissions to this library
`owner`| `string` | `Identifier of the user who created the library


	POST /libraries/

Creates a library for the requesting user. Returns metadata on the library created.

<%= headers 200 %>
```json
{}
```

### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library


### Parameters

Name | Type | Description
-----|------|-----------------------
`name` | `string` | Name of the library (must be unique for that user)
`description`| `string`| Description of the library
`public`| `boolean`| Whether the library is public to view
`bibcode`|`list` | Optional. List of bibcodes to add

### Return data

Name | Type | Description
-----|------|-----------------------
`name` | `string` | Name of the library
`id` |`string`| ID of the library
`description`| `string`| Description of the library


## Work with a Library

	GET /libraries/:library_id

End point to interact with a specific library. Obtains all the documents of a given library. 
**library_id** [**string**] is the unique identifier of the library, as specified in the `/libraries` GET response.


Only returns library content if the user has the correct privileges. See the document end point for deleting a library. 

<%= headers 200 %>
```json
{}
```

### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library. Additionally, the user has to have one of: `admin`, `owner` roles.


### Return data

Name | Type | Description
-----|------|-----------------------
`documents` | `list` | Currently, a list of bibcodes.
`solr` |`dict`| The response from the search API [BigQuery endpoint](../search#bigquery)
`metadata`| `dict`| Metadata of the library, see description above
`updates` | `dict` | `num_updated` - (int) number of documents modified based on the response from the search<br/> `duplicates_removed` - (int) Number of files removed because they are duplication<br/> `update_list` - List of dictionaries such that a single element described the original bibcode (key) and the updated bibcode now being stored (item)





	POST /documents/:library_id


End point to interact with a specific library, by adding documents and removing documents. You also use this endpoint to delete the entire library. **library_id** (`string`) is the unique identifier of the library, as specified in the `/libraries` GET response.

Adds a document to a library for a given user.

### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library. Additionally, the user has to have one of: `admin`, `owner` roles.
`write` | Gives the user permission to edit the library. Additionally, the user has to have one of: `admin`, `owner` roles.


### Parameters

Name | Type | Description
-----|------|-----------------------
`bibcode` | `list` | List of bibcodes to be added.
`action`| `string`| 'add' or 'remove' a bibcode


### Return data

Name | Type | Description
-----|------|-----------------------
`number_added` | `int` | number of documents added (if 'add' is used) 
`number_removed`| `int`| number of documents removed (if 'remove' is used)







	PUT /documents/:library_id


### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library. Additionally, the user has to have one of: `admin`, `owner` roles.


### Parameters

Name | Type | Description
-----|------|-----------------------
`name` | `string` | Name of the library (must be unique for that user)
`description`| `string`| Description of the library
`public`| `boolean`| Whether the library is public to view


*Note: The above are optional. Leave fields out if they do not need to be updated.*

### Return data

Name | Type | Description
-----|------|-----------------------
`name` | `string` | Name of the library
`description`| `string`| Description of the library
`public`| `boolean`| If the library should be publicly viewable


*Note: returns the key/value that was requested to be updated*





	 DELETE /documents/:library_id


Request that deletes a library.


### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library. The user has to have `owner` role.


## Update Access Rights


End point to manipulate the permissions between a user and a library.


	GET /permissions/:library_id

Request that returns the permissions for a given library.

<%= headers 200 %>
```json
{}
```

### Scopes

Name | Description
-----|-------------
`user` | Gives the user permission to view the library. Additionally, the user has to have one of: `admin`, `owner` roles.


### Return data

List of dictionaries, where each dictionary is for a specific user.


Name | Type | Description
-----|------|-----------------------
`user_dictionary` | `dict` | `key` contains the user's email, the `item` will have a list of permissions (ie: 'read', 'write', 'admin', 'owner')



	POST /permissions/:library_id

Request that modifies the permissions of a library

### Scopes

Name | Description
-----|-------------
`user` |  Additionally, the user has to have one of: `admin`, `owner` roles.


### Parameters

Name | Type | Description
-----|------|------------
`username`|`string`| Identification of the user (typically email)
`permission`|`string`| 'read', 'write', 'admin' or 'owner'
`value` | `boolean`| Whether the user has this permission (True=yes, False=no)



## Transfer a Library

	POST  /transfer/library_id

Transfer the ownership of a library to another ADS user.


### Scopes

Name | Description
-----|-------------
`user` |  The user has to have the role of `owner`.


### Parameters

Name | Type | Description
-----|------|------------
`transfer_user`|`string`| Username of the user the account should be transfered to


## Explanation of Permissions

  * **owner**: Owns the library. Can read libraries, add/remove bibcodes, delete the library, add/remove permissions, transfer ownership of the library.
  * **admin**: Can read libraries, add/remove bibcodes, add/remove permissions.
  * **write**: Can read libraries, add/remove bibcdes.
  * **read**: Can read libraries.

Any other user that does not have a permission to the library they try to visit, can only see it if it is public. If the user has no permissions, they cannot view this library.

## Source code

The source code of the microservice can be viewed at https://github.com/adsabs/biblib-service.

