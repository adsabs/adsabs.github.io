
On average, articles get cited in a pretty predictable pattern. An article gets published, it takes a little while to get "absorbed" by the scientific community, and then, if it resonates, it starts getting citations. Something along the lines of figure 4 in my paper <a href="https://ui.adsabs.harvard.edu/#abs/2006JEPub...9....2H/abstract" target="_blank">"Effect of E-printing on Citation Rates in Astronomy and Physics", Journal of Electronic Publishing, vol. 9, p. 2</a>:

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2015-11-17_image01.gif" />
</div>

In the pre-Internet days, this meant that people had to work their way through abstract books and reading the tables of contents from volumes on the shelves of their local library. The principle, nevertheless, is the same, just with a different time scale. When you have to physically work your way through shelves and volumes, it obviously takes more time to gather your bibliography, when writing a paper in this pre-Internet era. Even when you allow for these longer time scales, there are still papers that take longer, way longer, to be cited than others. <a href="https://twitter.com/TodLauer/status/665283076835033088" target="_blank">Todd Lauer coined the phrase "long-fuse" papers on Twitter</a> (in a discussion with <a href="https://twitter.com/JossBlandHawtho/status/647199763851448321" target="_blank">Joss Bland-Hawthorn</a>) and wondered about how to detect these. That is what this blog is about. One attempt at finding them. The figure below shows one fine example of such a "long-fuse" publication: <a href="https://ui.adsabs.harvard.edu/#abs/1937ApJ....86..217Z/abstract" target="_blank">"On the Masses of Nebulae and of Clusters of Nebulae", by F. Zwicky (1937), Astrophysical Journal, vol. 86, p.217</a>

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2015-11-17_image05.png" alt="citations for 1937ApJ....86..217Z"/>
</div>

Before starting this little journey, first a caveat: when you go back into the pre-Internet era, especially decades before its inception, it is much harder to compile citation data. Some journals had references in footnotes, rather than in designated bibliographies, and in all cases references need to be manually typed in or extracted from the OCR of digitized material. In short, there are bound to be significant gaps in older citation data. But, even with this taken into account, there are still publications that can be described as "long-fuse" publications: there is something discussed in a publication that becomes (highly) relevant well after (which can be well up to a decade, or decades, later) its appearance. The Zwicky paper is a prime example.

So, how do you go about finding these publications? The key ingredient here is the fact that pubications really are nodes in a directed graph, specifically a directed graph with a very distinct "flow" publications cite material that has already been published, i.e. back in time. What makes "long-fuse" papers different within the context of the citation graph? Temporally speaking, the "distance" to the bulk of their citations is relative large. The next step is to turn this observation into a quantitative statement. Since we are looking at publications spread out over decades, it seems logical to apply some sort of normalization or scaling. Let's rescale all data in terms of "age" rather than absolute years. Within this context, it seems to make sense to compare the age of a publication to the average age of its associated citation distribution. Just to state the obvious: the "paper age" of a publication from, say, 1937, is 79 years (taking the current year as reference point, and starting with an age of 1). The "citation age" for a citation from a 2012 publication is 76 years (because if was published 76 years after the publication of the cited paper, taking citations from the same year as the cited paper as having an age of 1 year).

Let's explore the quanity <em>F</em> defined as the average citation age, divided by the paper age. What is its distribution like? To explore this, I took the following set of journals: <em>The Astrophysical Journal</em> (including <em>Letters</em> and <em>Supplement Series</em>), <em>The Astronomical Journal</em>, <em>Monthly Notices of the R.A.S.</em>, <em>Astronomy &amp; Astrophysics</em>, <em>Physical Review D</em>,<em> Physical Review E</em>, <em>Reviews of Modern Physics</em>, <em>Nuclear Physics A</em> and <em>Nuclear Physics B</em>. All the publications in this set were filtered on the following two, rather arbitrary, criteria: the minimal paper age is 20 years and the minimal amount of citations is 300. These filters were chosen for no particular reason, just to turn a set of about half a million publications into a much smaller set for this initial exploration. The resulting filtered publication set consists of 2750 publications. For this set, the quantity <em>F</em> turns out to have the frequency distribution shown in the figure below.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2015-11-17_image03.png" alt="frequency distribution of average citation age over paper age"/>
</div>

The phenomenon of "long-fuse" papers is not very likely to be the result of some sort of "phase transition&#8221; in the citation graph evolution; there probably is a smooth transition from the realm "long-fuse" papers to "regularly cited&#8221; papers. We can't point to a region in the figure above and say: <em>this region represents the component of "long-fuse" papers</em>.  Nevertheless, it seems plausible that the "long-fuse" papers live in the right tail of this distribution. Since this is just a first exploration, I&#8217;ll just pick a threshold and see what follows.

How many papers remain from the 2750 papers if I add the addition requirement that <em>F &gt; 0.75</em>? A total of 60 papers remain, 32 of which are from the set of core astronomy journals. Let&#8217;s explore a couple of them! The following plot shows the normalized number of citations (normalized by the number of citations on November 16, 2015) as a function of year for 5 papers on astronomy-related subjects.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2015-11-17_image02.png" alt="frequency distribution of average citation age over paper age"/>
</div>

These 5 papers are:

<ol>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1911MNRAS..71..460P/abstract" target="_blank">Plummer, H. C. (1911), "On the problem of distribution in globular star clusters&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 71, p.460</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1947MNRAS.107..410B/abstract" target="_blank">Bondi, H. (1947), "Spherically symmetrical models in general relativity&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 107, p.410</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1949RvMP...21..447G/abstract" target="_blank">Gödel, Kurt (1949), "An Example of a New Type of Cosmological Solutions of Einstein&#8217;s Field Equations of Gravitation&#8221;, Reviews of Modern Physics, vol. 21, Issue 3, pp. 447</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1972PhRvD...6.3368B/abstract" target="_blank">Boulware, David G. &amp; Deser, S. (1972), "Can Gravitation Have a Finite Range?&#8221;, Physical Review D, vol. 6, Issue 12, p. 3368</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1988NuPhB.302..668W/abstract" target="_blank">Wetterich, C. (1988), "Cosmology and the fate of dilatation symmetry&#8221;, Nuclear Physics B, Volume 302, Issue 4, p. 668</a></li>
</ol>

Below is a similar plot for 5 physics papers.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2015-11-17_image04.png" alt="Normalized citations for 5 long-fuse physics papers"/>
</div>


<p>The 5 papers are:</p>
<ol>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1957RvMP...29..454E/abstract" target="_blank">Everett, Hugh (1957), "&#8216;Relative State&#8217; Formulation of Quantum Mechanics&#8221;, Reviews of Modern Physics, vol. 29, Issue 3, pp. 454</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1966RvMP...38..447B/abstract" target="_blank">Bell, John S. (1966), "On the Problem of Hidden Variables in Quantum Mechanics&#8221;, Reviews of Modern Physics, vol. 38, Issue 3, pp. 447</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1970NuPhB..22..397V/abstract" target="_blank">van Dam, H. &amp; Veltman, M. (1970), "Massive and mass-less Yang-Mills and gravitational fields&#8221;, Nuclear Physics B, Volume 22, Issue 2, p. 397</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1973PhRvD...7.2405N/abstract" target="_blank">Nambu, Yoichiro (1973), "Generalized Hamiltonian Dynamics&#8221;, Physical Review D, vol. 7, Issue 8, pp. 2405</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1978PhRvD..18.2574D/abstract" target="_blank">Deshpande, Nilendra G. &amp; Ma, Ernest (1978), "Pattern of symmetry breaking with two Higgs doublets&#8221;, Physical Review D, Volume 18, Issue 7, pp.2574</a></li>
</ol>

So, this initial exploration looks promising! Next, I should attempt to look in more detail at the various assumptions and seemingly arbitrary choices of variables. The choices for minimal paper age and number of citations are probably arbitrary by nature, but it seems the selected cut-off frequency of 0.75 can definitely be explored a bit further.

Finally, here is the full set of 32 papers from the astronomy data set (note that the Zwicky paper was reproduced in this analysis):

<ol>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1911MNRAS..71..460P/abstract" target="_blank">Plummer, H. C. (1911), "On the problem of distribution in globular star clusters&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 71, p.460-470</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1924MNRAS..84..665V/abstract" target="_blank">von Zeipel, H. (1924), "The radiative equilibrium of a rotating system of gaseous masses&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 84, p.665-683</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1926ApJ....64..321H/abstract" target="_blank">Hubble, E. P. (1926), "Extragalactic nebulae.&#8221;, Astrophysical Journal, 64, 321-369 (1926)</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1937ApJ....86..217Z/abstract" target="_blank">Zwicky, F. (1937), "On the Masses of Nebulae and of Clusters of Nebulae&#8221;, Astrophysical Journal, vol. 86, p.217</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1941ApJ....93...70H/abstract" target="_blank">Henyey, L. G.; Greenstein, J. L. (1941), "Diffuse radiation in the Galaxy&#8221;, Astrophysical Journal, vol. 93, p. 70-83 (1941).</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1943ApJ....97..255C/abstract" target="_blank">Chandrasekhar, S. (1943), "Dynamical Friction. I. General Considerations: the Coefficient of Dynamical Friction.&#8221;, Astrophysical Journal, vol. 97, p.255</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1944MNRAS.104..273B/abstract" target="_blank">Bondi, H.; Hoyle, F. (1944), "On the mechanism of accretion by stars&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 104, p.273</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1947MNRAS.107..410B/abstract" target="_blank">Bondi, H. (1947), "Spherically symmetrical models in general relativity&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 107, p.410</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1952MNRAS.112..195B/abstract" target="_blank">Bondi, H. (1952), "On spherically symmetrical accretion&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 112, p.195</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1955ApJ...121..161S/abstract" target="_blank">Salpeter, Edwin E. (1955), "The Luminosity Function and Stellar Evolution.&#8221;, Astrophysical Journal, vol. 121, p.161</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1956MNRAS.116..351B/abstract" target="_blank">Bonnor, W. B. (1956), "Boyle&#8217;s Law and gravitational instability&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 116, p.351</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1959ApJ...129..243S/abstract" target="_blank">Schmidt, Maarten (1959), "The Rate of Star Formation.&#8221;, Astrophysical Journal, vol. 129, p.243</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1962AJ.....67..591K/abstract" target="_blank">Kozai, Yoshihide (1962), "Secular perturbations of asteroids with high inclination and eccentricity&#8221;, Astronomical Journal, Vol. 67, p. 591</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1964MNRAS.128..307R/abstract" target="_blank">Refsdal, S. (1964), "On the possibility of determining Hubble&#8217;s parameter and the masses of galaxies from the gravitational lens effect&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 128, p.307</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1968ApJ...153L..59N/abstract" target="_blank">Neupert, Werner M. (1968), "Comparison of Solar X-Ray Line Emission with Microwave Emission during Flares&#8221;, Astrophysical Journal, vol. 153, p.L59</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1972ApJ...178..347B/abstract" target="_blank">Bardeen, James M.; Press, William H.; Teukolsky, Saul A. (1972), "Rotating Black Holes: Locally Nonrotating Frames, Energy Extraction, and Scalar Synchrotron Radiation&#8221;, Astrophysical Journal, Vol. 178, pp. 347-370 (1972)</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1973ApJ...184..839S/abstract" target="_blank">Sneden, C. (1973), "The nitrogen abundance of the very metal-poor star HD 122563.&#8221;, Astrophysical Journal, Vol. 184, p. 839 &#8211; 849</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1973ApJ...186..705P/abstract" target="_blank">Purcell, Edward M.; Pennypacker, Carlton R. (1973), "Scattering and Absorption of Light by Nonspherical Dielectric Grains&#8221;, Astrophysical Journal, Vol. 186, pp. 705-714 (1973)</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1973ApJ...186.1007W/abstract" target="_blank">Whelan, John; Iben, Icko, Jr. (1973), "Binaries and Supernovae of Type I&#8221;, Astrophysical Journal, Vol. 186, pp. 1007-1014 (1973)</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1973MNRAS.161..365T/abstract" target="_blank">Tayler, R. J. (1973), "The adiabatic stability of stars containing magnetic fields-I.Toroidal fields&#8221;, Monthly Notices of the Royal Astronomical Society, Vol. 161, p. 365 (1973)</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1976ApJ...209L...1P/abstract" target="_blank">Petrosian, V. (1976), "Surface brightness and evolution of galaxies&#8221;, Astrophysical Journal, vol. 209, Oct. 1, 1976, pt. 2, p. L1-L5.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1977MNRAS.179..433B/abstract" target="_blank">Blandford, R. D.; Znajek, R. L. (1977), "Electromagnetic extraction of energy from Kerr black holes&#8221;, Monthly Notices of the Royal Astronomical Society, vol. 179, May 1977, p. 433-456.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1977MNRAS.180...57W/abstract" target="_blank">Weidenschilling, S. J. (1977), "Aerodynamics of solid bodies in the solar nebula&#8221;, Monthly Notices of the Royal Astronomical Society, vol. 180, July 1977, p. 57-70. Research supported by the Carnegie Corp.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1977MNRAS.181..375G/abstract" target="_blank">Gingold, R. A.; Monaghan, J. J. (1977), "Smoothed particle hydrodynamics &#8211; Theory and application to non-spherical stars&#8221;, Monthly Notices of the Royal Astronomical Society, vol. 181, Nov. 1977, p. 375-389.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1979ApJ...228..939C/abstract" target="_blank">Cash, W. (1979), "Parameter estimation in astronomy through application of the likelihood ratio&#8221;, Astrophysical Journal, Part 1, vol. 228, Mar. 15, 1979, p. 939-947.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1981A&amp;A....99..126H/abstract" target="_blank">Hut, P. (1981), "Tidal evolution in close binary systems&#8221;, Astronomy and Astrophysics, vol. 99, no. 1, June 1981, p. 126-140.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1982ApJ...253..785A/abstract" target="_blank">Arnett, W. D. (1982), "Type I supernovae. I &#8211; Analytic solutions for the early part of the light curve&#8221;, Astrophysical Journal, Part 1, vol. 253, Feb. 15, 1982, p. 785-797.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1982MNRAS.200..115S/abstract" target="_blank">Soltan, A. (1982), "Masses of quasars&#8221;, Monthly Notices of the Royal Astronomical Society, vol. 200, July 1982, p. 115-122.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1983ApJ...270..365M/abstract" target="_blank">Milgrom, M. (1983), "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis&#8221;, Astrophysical Journal, Part 1 (ISSN 0004-637X), vol. 270, July 15, 1983, p. 365-370. Research supported by the U.S.-Israel Binational Science Foundation.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1983ApJ...272..317L/abstract" target="_blank">Li, T.-P.; Ma, Y.-Q. (1983), "Analysis methods for results in gamma-ray astronomy&#8221;, Astrophysical Journal, Part 1 (ISSN 0004-637X), vol. 272, Sept. 1, 1983, p. 317-324.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1986ApJ...309..846L/abstract" target="_blank">Lin, D. N. C.; Papaloizou, John (1986), "On the tidal interaction between protoplanets and the protoplanetary disk. III &#8211; Orbital migration of protoplanets&#8221;, Astrophysical Journal, Part 1 (ISSN 0004-637X), vol. 309, Oct. 15, 1986, p. 846-857.</a></li>
<li><a href="https://ui.adsabs.harvard.edu/#abs/1994ApJ...422..158O/abstract" target="_blank">O&#8217;Donnell, James E. (1994), "R<sub>nu</sub>-dependent optical and near-ultraviolet extinction&#8221;, Astrophysical Journal, Part 1 (ISSN 0004-637X), vol. 422, no. 1, p. 158-163</a></li>
</ol>
