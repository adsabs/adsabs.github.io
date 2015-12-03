---
title: Export Service | ADS API
---

# Export service API


	POST /export/:format

### parameters

name | type | description
-----|------|--------------
`bibcode`  |`list` | list of bibcodes

<%= headers 200 %>
```json
{
  "msg": "Retrieved 1 abstracts, starting with number 1.  Total number selected: 1.", 
  "export": "@ARTICLE{2015ApJS..219...21Z,\n   author = {{Zhang}, M. and {Fang}, M. and {Wang}, H. and {Sun}, J. and \n\t{Wang}, M. and {Jiang}, Z. and {Anathipindika}, S.},\n    title = \"{A Deep Near-infrared Survey toward the Aquila Molecular Cloud. I. Molecular Hydrogen Outflows}\",\n  journal = {\\apjs},\narchivePrefix = \"arXiv\",\n   eprint = {1506.08372},\n primaryClass = \"astro-ph.SR\",\n keywords = {infrared: ISM, ISM: jets and outflows, shock waves, stars: formation, stars: winds, outflows},\n     year = 2015,\n    month = aug,\n   volume = 219,\n      eid = {21},\n    pages = {21},\n      doi = {10.1088/0067-0049/219/2/21},\n   adsurl = {http://adsabs.harvard.edu/abs/2015ApJS..219...21Z},\n  adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}\n\n"
}
```

Available formats are: `aastex`, `bibtex`, `endnote`

Using `curl`, to get the BibTeX for e.g. the record with bibcode `2015ApJS..219...21Z`, you would do

``` command-line
$ curl -H "Authorization: Bearer <your API token>" -H "Content-Type: application/json" -X POST -d '{"bibcode":["2015ApJS..219...21Z"]}' https://api.adsabs.harvard.edu/v1/export/bibtex

{
>  "msg": "Retrieved 1 abstracts, starting with number 1.  Total number selected: 1.", 
>  "export": "@ARTICLE{2015ApJS..219...21Z,\n   author = {{Zhang}, M. and {Fang}, M. and {Wang}, H. and {Sun}, J. and \n\t{Wang}, M. and {Jiang}, Z. and {Anathipindika}, S.},\n    title = \"{A Deep Near-infrared Survey toward the Aquila Molecular Cloud. I. Molecular Hydrogen Outflows}\",\n  journal = {\\apjs},\narchivePrefix = \"arXiv\",\n   eprint = {1506.08372},\n primaryClass = \"astro-ph.SR\",\n keywords = {infrared: ISM, ISM: jets and outflows, shock waves, stars: formation, stars: winds, outflows},\n     year = 2015,\n    month = aug,\n   volume = 219,\n      eid = {21},\n    pages = {21},\n      doi = {10.1088/0067-0049/219/2/21},\n   adsurl = {http://adsabs.harvard.edu/abs/2015ApJS..219...21Z},\n  adsnote = {Provided by the SAO/NASA Astrophysics Data System}\n}\n\n"
}

```

## Source Code

The source of the microservice is at https://github.com/adsabs/export_service.


