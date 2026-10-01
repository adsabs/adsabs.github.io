<section class="about-band about-band--wash" id="ai">
  <div class="about-band-inner">
    <p class="about-eyebrow">Machine learning at SciX</p>
    <h2>We build the models, and we share them openly</h2>
    <p class="about-lead">A team of twenty cannot read 36 million records. Machine learning is how a group this size keeps a collection this large accurate, and every model and dataset we train for the job is released publicly.</p>

    <div class="about-split about-split--wide">
      <div>
        <h3>What we have released</h3>
        <ul class="about-releases">
          <li>
            <span class="about-release-year">2021</span>
            <span class="about-release-body"><strong>astroBERT</strong>, a language model trained on the astronomy literature.</span>
          </li>
          <li>
            <span class="about-release-year">2024</span>
            <span class="about-release-body"><strong>INDUS</strong>, a cross-disciplinary model built with NASA and IBM. It won a <a href="https://science.nasa.gov/open-science/ai-language-model-science-research/">NASA Agency Group Achievement Award</a> in 2025.</span>
          </li>
          <li>
            <span class="about-release-year">2024</span>
            <span class="about-release-body"><strong>NER-DEAL</strong>, an open dataset for tagging papers by topic.</span>
          </li>
          <li>
            <span class="about-release-year">2025</span>
            <span class="about-release-body"><strong>TRACS</strong>, which links papers to the telescopes that produced the observations.</span>
          </li>
        </ul>
        <p>The models live on <a href="https://huggingface.co/adsabs">Hugging Face</a> and the code on <a href="https://github.com/adsabs">GitHub</a>. Anyone can use them. <a href="{{ site.baseurl }}/scixblog/ads-models-and-datasets">Read about the models</a>.</p>
      </div>

      <div>
        <h3>How we use it</h3>
        <p>Machine learning routes records into the right disciplines and finds the mentions of data and software buried in a paper's text. Curators wrote the rules it learned from, and curators check what comes back. The classification that sorts the collection started as a set of ground rules written by subject specialists, and the model refines that work rather than replacing it.</p>

        <h3>Why a curated corpus matters now</h3>
        <p>Generative models invent citations. An answer about science can only be trusted if it can be traced to a real paper, a real dataset and a real grant. SciX holds exactly that: curated records, rich metadata, and a graph of the links between them, maintained by scientists.</p>
        <p>Through the <a href="{{ site.baseurl }}/scixhelp/api-scix/">open API</a>, a research assistant can walk that graph and come back with work it can attribute, including connections across fields that a general search engine will not surface. A climate model written for Earth turning up in a study of an exoplanet atmosphere is the kind of link the graph can make.</p>
        <p>This work follows the Smithsonian's principles for AI: accuracy, privacy, respect for copyright, and use that can be accounted for.</p>
      </div>
    </div>
  </div>
</section>
