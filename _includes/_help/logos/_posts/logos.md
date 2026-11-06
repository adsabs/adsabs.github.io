# {{ include.site }} Logos

{% if include.ads %}Below is the collection of ADS logo svg files used within the front-end services.{% else %}Below is the collection of SciX logo files used within the SciX website and help pages.{% endif %} All logos are covered by the Creative Commons License with Attribution, but put simply, any user can copy, modify, or redistribute the images (even commercially) as long as the original author ({{ include.site }}) is attributed. For full details, <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">read the license.</a>

(To save an image, right click and select "save image as"{% unless include.ads %}, or use the download link below it{% endunless %}).

{% if include.ads %}
<hr>
<div class="row">

  <div class="col-sm-12 col-md-0 col-md-offset-1">

  <div>
    <img src="/help/img/bbb_assets/ads_partial_logo_dark_background.svg" alt="" class="img-responsive" style="max-width:200px;margin:auto;">
  </div>
  <br>
  <div>
    <img src="/help/img/bbb_assets/ads_logo_full_light_background.svg" alt="" class="img-responsive">
  </div>
  <br>
  <div>
    <img src="/help/img/bbb_assets/ads_logo_full_dark_background.svg" alt="" class="img-responsive">
  </div>


  </div>
</div>
<hr>
{% else %}
Higher-resolution versions of these logos will be added to this page later.

<hr>
<div class="row">

  <div class="col-sm-12 col-md-0 col-md-offset-1">

  <div>
    <img src="{{ site.baseurl }}/help/common/images/scix/FULL%20COLOR-ScixHorizontalBlackBackground.svg" alt="SciX horizontal logo, full color on a black background" class="img-responsive" style="max-width:400px;margin:auto;">
    <p class="text-center"><strong>Horizontal logo</strong> (icon and wordmark), full color on a black background. SVG. <a href="{{ site.baseurl }}/help/common/images/scix/FULL%20COLOR-ScixHorizontalBlackBackground.svg" download>Download</a></p>
  </div>
  <br>
  <div>
    <img src="{{ site.baseurl }}/help/common/images/scix/FULLCOLORDARK-IsotypeNoBackground.svg" alt="SciX icon, full color with a dark outline, transparent background" class="img-responsive" style="max-width:200px;margin:auto;">
    <p class="text-center"><strong>Icon</strong>, full color with a dark outline, transparent background (for use on light backgrounds). SVG. <a href="{{ site.baseurl }}/help/common/images/scix/FULLCOLORDARK-IsotypeNoBackground.svg" download>Download</a></p>
  </div>
  <br>
  <div>
    <div style="background-color:#222;padding:15px;max-width:230px;margin:auto;">
      <img src="{{ site.baseurl }}/help/common/images/scix/FULLCOLORLIGHT-IsotypeNoBackground.svg" alt="SciX icon, full color with a white outline, transparent background" class="img-responsive" style="max-width:200px;margin:auto;">
    </div>
    <p class="text-center"><strong>Icon</strong>, full color with a white outline, transparent background (for use on dark backgrounds; shown here on a dark background). SVG. <a href="{{ site.baseurl }}/help/common/images/scix/FULLCOLORLIGHT-IsotypeNoBackground.svg" download>Download</a></p>
  </div>
  <br>
  <div>
    <img src="{{ site.baseurl }}/about/img/SciX-logo.png" alt="SciX icon, white outline on a dark square background" class="img-responsive" style="max-width:150px;margin:auto;">
    <p class="text-center"><strong>Icon</strong>, full color with a white outline on a dark square background. PNG, 150 x 150 pixels. <a href="{{ site.baseurl }}/about/img/SciX-logo.png" download>Download</a></p>
  </div>
  <br>
  <div class="text-center">
    <img src="{{ site.baseurl }}/help/common/images/scix/FAVICON-black-frame-32X32.png" alt="SciX favicon, dark outline">
    &nbsp;
    <span style="display:inline-block;background-color:#222;padding:4px;"><img src="{{ site.baseurl }}/help/common/images/scix/FAVICON-white-frame-32X32.png" alt="SciX favicon, white outline"></span>
    <p><strong>Favicons</strong>, dark outline (for light backgrounds) and white outline (for dark backgrounds), transparent background. PNG. Dark outline:
    <a href="{{ site.baseurl }}/help/common/images/scix/FAVICON-black-frame-16X16.png" download>16 x 16</a>,
    <a href="{{ site.baseurl }}/help/common/images/scix/FAVICON-black-frame-32X32.png" download>32 x 32</a>.
    White outline:
    <a href="{{ site.baseurl }}/help/common/images/scix/FAVICON-white-frame-16X16.png" download>16 x 16</a>,
    <a href="{{ site.baseurl }}/help/common/images/scix/FAVICON-white-frame-32X32.png" download>32 x 32</a>.</p>
  </div>


  </div>
</div>
<hr>
{% endif %}
