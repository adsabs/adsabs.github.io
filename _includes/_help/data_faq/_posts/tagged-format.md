# The {{ include.site }} Tagged Format

We welcome the submission of Bibliographic Records from librarians and researchers willing to provide this information to the {{ include.site }}. To facilitate the insertion of this data into our databases, we request that the records be submitted in electronic form and adhere to the following format:

    %R Bibliographic Code (required)
    %A Author List
    %a Review Authors
    %b Book Authors
    %F Author Affiliation
    %J Journal Name
    %D Publication Date
    %P First Page of Article
    %L Last Page of Article
    %T Title (required)
    %t Original Language Title
    %C Abstract Copyright
    %O Object Name
    %G Origin
    %I Links to other information
    %U Unified Astronomy Thesaurus (UAT) keywords
    %K Keywords
    %M Language (if not English)
    %X Comment
    %W Collection (if submitting for more than one)
    %B Abstract Text
    %Z References

A long entry should continue on the next line(s) with no repetition of the percent sign and keying letter. All entries should be in ascii and there should be no tabs or control characters. Blank lines can delimit paragraphs in the abstract, but should not otherwise be present within a record. The bibliographic code is the only field which is required for all records, but author list, journal name, publication date, and title are strongly recommended as well. Additional records should be separated by a blank line.

## Fields in the Tagged Format

Detailed descriptions of each field follow.

### Bibliographic Code

The bibliographic code is a 19 digit code (see [Bibcodes]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/help/actions/bibcode))

### Author List

The author list should contain semi-colon separated authors listed with last name first, followed by first name or initials. A paper with one author would be listed as Minkowski, R. A paper with multiple authors would be listed as

    Neubauer, F. J.; Burwell, C. G.; Miller, W. C.

Authors whose names contain "Jr" or "III" should be entered as

    Roberts, L. C., Jr.


### Review Authors

This contains the review authors in the same format as the regular authors.

### Book Authors

This contains the book authors in the same format as the regular authors.

### Author Affiliation

The institution with which the author is affiliated. If more than one author affiliation is to be listed, here is the suggested format:

    AA(first author's institution) AB(second author's institution) ...

Email addresses can be specified in the author affiliations. Please mark them as follows:

    <EMAIL>email address</EMAIL>


### Journal Name

This entry contains the reference information, including the journal name, volume, and page range. Also include here any editors of books or conference proceedings.

### Publication Date

This contains the publication month and year of the article in the format MM/YYYY (i.e. 02/1995). If no publication month is known, please use a month of 00.

### First Page of Article

This contains the first page number of the article.

### Last Page of Article

This contains the last page number of the article.

### Title

%T contains the title of the article. If there is also an original language title, it can be submitted with a %t and the language included in the %M tag.

### Object Name

This contains the name of Objects described in the paper. These are normally handled through SIMBAD and are therefore not part of the user input except in special circumstances.

### Origin of the Article in {{ include.site }}

This contains the source of the record in {{ include.site }}.
### Abstract Copyright

This contains a copyright statement of the abstract, such as
    (C) 1990: American Astromomical Society

### Unified Astronomy Thesaurus keywords

This contains keywords from the [Unified Astronomy Thesaurus](http://astrothesaurus.org/) (UAT), separated by a comma.

### Links to Other Information

Links should be preceded by their link type and semi-colon separated, e.g.

	%I DOI: 10.1234/article_doi; PDF: https://article_pdf

Available links include arxiv, data, doi, electr, pdf and other.

### Keywords

This contains keywords related to the article, separated by a comma.

### Language

This contains the original language of the article.

### Comment

This contains author comments.

### Collection

This contains the database key if you are submitting abstracts for multiple databases (astronomy: AST, physics: PHY, general: GEN).

### Abstract

This contains the abstract text. Any line beginning with at least one blank space will be assumed to be a new paragraph. New paragraphs may also be delimited with blank lines. Abstracts should not contain tables, and will appear best in the system if they contain only ascii characters.

### References

This field should contain the list of references cited by the current paper. They should be formatted so that there is just one reference per line, e.g.:

    %Z Bechtold,~J., \etal 1994, \aj, 108, 374
       Massa, D. L., & Savage, B. D. 1984, ApJ, 279, 310
       Savage, B. D., & Mathis, J. S. 1979, ARA&A, 17, 73

Please note that references containing TeX/LaTeX formatting, AASTeX macros and HTML entities are acceptable.

## Examples of Records in Tagged Format

This section shows a few examples of our tagged format.

Example 1:

	%R 1993ApJ...415...50C
	%A Cavaliere, A.; Colafrancesco, S.; Menci, N.
	%J Astrophysical Journal, Part 1, vol.415, no. 1, p. 50-57.
	%D 09/1993
	%L 57
	%T Distant clusters of galaxies detected by X-rays
	%K Cosmic Plasma, Dark Matter, Galactic Clusters, X-ray Astronomy, Baryons, Luminosity, Redshift
	%B The dynamical masses of groups and clusters of galaxies decrease on average with increasing redshift, after the hierarchical cosmogonies dominated by direct collapses of dark matter overdensities. We show that the masses of intracluster plasma emitting in the X-ray band are to decrease more rapidly. We also show that consideration of the intrinsic spread in the dynamical formation times leads us to predict more numerous faint sources at given dynamical mass. The model we compute yields steeper luminosity functions in the X-ray band with a specific change in lookback time: the bright end shifts back. Such negative evolution is fast even at modest redshifts z less than about 0.5 if the external gas infalling into groups of clusters was preheated and has cooled down after z of about 1.5-2. If so, the evolution is considerably faster in the X-ray than in the optical band, comparing interestingly with data from the existing surveys.
	%Z Abell, Ci. 0. 1958, ApJS, 3, 211
	Barcons, X., Fabian, A. C., & Rees, M. J. 1991, Nature, 350, 685
	Bardeen, J. M., Bond, J. R., Kaiser, N., & Szalay, A. 5. 1986, ApJ, 403, 15
	Blumenthal, Ci., Faber, S. M., Primack, J. R., & Rees, M. J. 1984, Nature, 311, 517
	Bohringer, H., et al. 1991, in Proc. NATO ASI "Clusters and Superclusters of Galaxies," ed. A. C. Fabian (Dordrecht: Kluwer), 71 
	Burg, R., Cavaliere, A., & Menci, N. 1993, ApJ, 404, L55
	Cavaliere, A., Gursky, H., & Tucker, W. H. 1971, Nature, 231, 437
	Cavaliere, A., & Colafrancesco, 5. 1988, ApJ, 331, 660
	---. 1990, in Clusters of Galaxies (Cambridge: Cambridge Univ. Press), 43
	Cavaliere, A., Burg, R., & Giacconi, R. 1991, ApJ, 366, L61

Example 2:

	%T Adsorption behavior of a textile dye of Reactive Blue 19 from aqueous solutions onto modified bentonite   
	%A Gök, Özer; Safa Özcan, A.;Özcan, Adnan
	%P 5439

Example 3:

	%T Seeing Red: Extremely Red Objects from the Cadis K' Survey
	%A Thompson, D.; Beckwith, S. V. W.
	%F AA(Max-Planck-Institut fuer Astronomie, Koenigstuhl 17, D-69117 Heidelberg, Germany)
	%P 13
	%B We discuss various interpretations of the nature of extremely red objects (EROs), discovered in the first of 7 deep, wide-field K' images in the CADIS survey. Point sources with K' = 20.5 mag are detected at the 5 sigma level over an area of 125 arcmin^2. A total of 20 EROs meeting the selection criteria (R-K') >= 6^{m} and K' <= 19.75 mag were selected from the data, giving a surface density of 0.16 +/- 0.04 arcmin^{-2} for all EROs and 0.016 +/- 0.011 arcmin^{-2} for bright (K' < 19^{m}) EROs.} 

Example 4:

	%T Chandra observations of M31 and their implications for its ISM
	%A Primini, F., Garcia, M., Murray, S., Forman, W., Jones, C., and McClintock, J.
	%F AA(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA), AB(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA), AC(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA), AD(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA), AE(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA), AF(Harvard-Smithsonian Center for Astrophysics, Cambridge, USA) 
	%B We have been regularly observing the bulge and inner disk of M31 for nearly one year, using both the HRC-I and ACIS-I instruments on the Chandra X-Ray Observatory. We present results from our program that are of interest to the study of the ISM in M31. In particular, we find that the unresolved emission within 3' of the center of M31 has a distinctly softer spectrum than that of most of the resolved X-ray sources in the region. Preliminary spectral analysis of bright point sources in the bulge shows no evidence (within the poor statistics) for soft spectral components, but does reveal significant extra-galactic X-ray extinction (NH ~ 1021 cm-2). We find no new X-ray counterparts to supernova remnants to date. 

Example 5:

	%T We Do Not Forget Johannes Kepler
	%A Wszołek, B
	%B Year 2009 was announced as the International Year of Astronomy. This was to mark 400th anniversary of the first astronomical observation through a telescope by Galileo. From the other hand, this year marks 400th anniversary of Astronomia Nova, the famous work of Kepler published in Prague in 1609. Two laws of planetary motions opened human efforts to understand gravitational force; so the overall cosmic space conquest, with its great importance not only for astronomy, was developed thankful to Kepler's work. This contribution is thought to show the most inspiring ideas of Johannes Kepler, published in Astronomia Nova and in other his books. 
	%I PDF: FILE:proc16_02.pdf

