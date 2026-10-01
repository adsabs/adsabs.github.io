<section class="about-band">
  <div class="about-band-inner about-split">
    <div>
      <h2>A map of the literature, not a list</h2>
      <p>Each record is a node, and the paper is the hub. From a paper you can move to the papers it references and the papers that cite it, to the datasets and software it mentions, and to the grants tied to the work. In a single quarter researchers followed 1.72 million of those links from a publication out to the data behind it.</p>
      <p>The models that classify and link records, including astroBERT and INDUS, are published on <a href="https://huggingface.co/adsabs">Hugging Face</a>. <a href="{{ site.baseurl }}/scixblog/ads-models-and-datasets">Read about the models</a>.</p>
    </div>
    <div class="about-graph" role="img" aria-label="Knowledge graph with a paper at the center, linked to references, citations, data, software, and grants.">
      <svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id="kg-field" cx="50%" cy="48%" r="58%">
            <stop offset="0%" stop-color="#049dd9" stop-opacity="0.10" />
            <stop offset="100%" stop-color="#049dd9" stop-opacity="0" />
          </radialGradient>
          <filter id="kg-soft" x="-40%" y="-40%" width="180%" height="180%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
          <pattern id="kg-dots" width="18" height="18" patternUnits="userSpaceOnUse">
            <circle cx="1" cy="1" r="0.7" class="kg-dot" />
          </pattern>
        </defs>

        <rect class="kg-field" width="720" height="480" rx="16" />
        <rect width="720" height="480" rx="16" fill="url(#kg-field)" />
        <rect width="720" height="480" rx="16" fill="url(#kg-dots)" opacity="0.55" />

        <g class="kg-edges" fill="none">
          <path class="kg-edge kg-edge--primary kg-edge--navy" d="M360 210 C360 170 360 130 360 88" />
          <path class="kg-edge kg-edge--primary kg-edge--cyan" d="M392 218 C460 190 510 170 548 156" />
          <path class="kg-edge kg-edge--primary kg-edge--teal" d="M328 218 C250 190 200 170 172 156" />
          <path class="kg-edge kg-edge--primary kg-edge--green" d="M332 258 C280 300 240 340 208 362" />
          <path class="kg-edge kg-edge--primary kg-edge--orange" d="M388 258 C450 300 500 340 528 362" />

          <path class="kg-edge kg-edge--leaf kg-edge--navy" d="M360 72 C340 60 328 54 318 48" />
          <path class="kg-edge kg-edge--leaf kg-edge--navy" d="M360 72 C382 58 392 54 402 50" />
          <path class="kg-edge kg-edge--leaf kg-edge--navy" d="M360 72 C346 90 340 100 336 108" />
          <path class="kg-edge kg-edge--leaf kg-edge--navy" d="M360 72 C378 88 388 96 396 102" />

          <path class="kg-edge kg-edge--leaf kg-edge--cyan" d="M548 150 C568 130 580 122 592 118" />
          <path class="kg-edge kg-edge--leaf kg-edge--cyan" d="M548 150 C576 160 596 166 610 170" />
          <path class="kg-edge kg-edge--leaf kg-edge--cyan" d="M548 150 C540 172 534 184 528 190" />
          <path class="kg-edge kg-edge--leaf kg-edge--cyan" d="M548 150 C562 178 568 192 572 202" />

          <path class="kg-edge kg-edge--leaf kg-edge--teal" d="M172 150 C148 132 132 126 120 122" />
          <path class="kg-edge kg-edge--leaf kg-edge--teal" d="M172 150 C140 164 118 174 102 180" />
          <path class="kg-edge kg-edge--leaf kg-edge--teal" d="M172 150 C186 168 192 180 196 190" />

          <path class="kg-edge kg-edge--leaf kg-edge--green" d="M208 362 C178 348 162 344 150 340" />
          <path class="kg-edge kg-edge--leaf kg-edge--green" d="M208 362 C186 382 174 394 166 402" />
          <path class="kg-edge kg-edge--leaf kg-edge--green" d="M208 362 C226 384 234 394 240 400" />

          <path class="kg-edge kg-edge--leaf kg-edge--orange" d="M528 362 C556 346 570 342 582 338" />
          <path class="kg-edge kg-edge--leaf kg-edge--orange" d="M528 362 C550 384 562 394 570 402" />
          <path class="kg-edge kg-edge--leaf kg-edge--orange" d="M528 362 C508 382 498 392 492 400" />

          <path class="kg-edge kg-edge--cross" d="M196 190 C240 230 280 280 208 362" />
          <path class="kg-edge kg-edge--cross" d="M528 362 C480 280 420 160 396 102" />
          <path class="kg-edge kg-edge--cross" d="M528 190 C470 140 410 90 360 72" />
        </g>

        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(318 48)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(402 50)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(336 108)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(396 102)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>

        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(592 118)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(610 170)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(528 190)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>
        <g class="kg-node kg-node--paper kg-node--leaf" transform="translate(572 202)"><rect x="-9" y="-11" width="18" height="22" rx="2.5" /><path d="M-5-4h10M-5 1h10M-5 6h7" /></g>

        <g class="kg-node kg-node--data kg-node--leaf" transform="translate(120 122)"><circle r="8" /></g>
        <g class="kg-node kg-node--data kg-node--leaf" transform="translate(102 180)"><circle r="7" /></g>
        <g class="kg-node kg-node--data kg-node--leaf" transform="translate(196 190)"><circle r="8" /></g>

        <g class="kg-node kg-node--soft kg-node--leaf" transform="translate(150 340)"><rect x="-7" y="-7" width="14" height="14" rx="3" /></g>
        <g class="kg-node kg-node--soft kg-node--leaf" transform="translate(166 402)"><rect x="-6" y="-6" width="12" height="12" rx="3" /></g>
        <g class="kg-node kg-node--soft kg-node--leaf" transform="translate(240 400)"><rect x="-7" y="-7" width="14" height="14" rx="3" /></g>

        <g class="kg-node kg-node--grant kg-node--leaf" transform="translate(582 338)"><polygon points="0,-9 8,-4 8,4 0,9 -8,4 -8,-4" /></g>
        <g class="kg-node kg-node--grant kg-node--leaf" transform="translate(570 402)"><polygon points="0,-8 7,-3.5 7,3.5 0,8 -7,3.5 -7,-3.5" /></g>
        <g class="kg-node kg-node--grant kg-node--leaf" transform="translate(492 400)"><polygon points="0,-8 7,-3.5 7,3.5 0,8 -7,3.5 -7,-3.5" /></g>

        <g class="kg-node kg-node--paper kg-node--type" transform="translate(360 72)">
          <rect x="-16" y="-20" width="32" height="40" rx="4" />
          <path d="M-8-8h16M-8-1h16M-8 6h10" />
        </g>
        <text class="kg-label" x="360" y="28" text-anchor="middle">References</text>

        <g class="kg-node kg-node--paper kg-node--type" transform="translate(548 150)">
          <rect x="-16" y="-20" width="32" height="40" rx="4" />
          <path d="M-8-8h16M-8-1h16M-8 6h10" />
        </g>
        <text class="kg-label" x="548" y="112" text-anchor="middle">Citations</text>

        <g class="kg-node kg-node--data kg-node--type" transform="translate(172 150)">
          <circle r="16" />
        </g>
        <text class="kg-label" x="172" y="122" text-anchor="middle">Data</text>

        <g class="kg-node kg-node--soft kg-node--type" transform="translate(208 362)">
          <rect x="-14" y="-14" width="28" height="28" rx="6" />
        </g>
        <text class="kg-label" x="208" y="394" text-anchor="middle">Software</text>

        <g class="kg-node kg-node--grant kg-node--type" transform="translate(528 362)">
          <polygon points="0,-18 16,-9 16,9 0,18 -16,9 -16,-9" />
        </g>
        <text class="kg-label" x="528" y="394" text-anchor="middle">Grants</text>

        <g class="kg-hub" filter="url(#kg-soft)" transform="translate(360 230)">
          <rect class="kg-hub-card" x="-34" y="-42" width="68" height="84" rx="8" />
          <path class="kg-hub-lines" d="M-18-18h36M-18-8h36M-18 2h24" />
          <text class="kg-hub-text" y="28" text-anchor="middle">Paper</text>
        </g>
      </svg>
    </div>
  </div>
</section>
