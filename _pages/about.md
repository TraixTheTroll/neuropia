---
layout: about
title: Home
permalink: /
description: Mesenchymal stem cells and extracellular vesicles in neurological disease
subtitle: Research group · Bergen, Norway
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

<div class="neuropia-home">
  <p class="neuropia-lead">
    Mesenchymal stem cells and extracellular vesicles in neurological disease.
  </p>
  <p>
    Neuropia investigates the therapeutic potential of mesenchymal stem cells and extracellular vesicles,
    with multiple sclerosis as our main disease focus. Our broader research interests include other
    neurodegenerative disorders, such as Parkinson’s disease.
  </p>
  <p>We are based at Neuro-SysMed, Haukeland University Hospital, and the University of Bergen, Norway.</p>

  <div class="neuropia-feature-grid">
    <a class="neuropia-feature" href="{{ '/research/' | relative_url }}">
      <span class="neuropia-eyebrow">Our focus</span>
      <h2>Research</h2>
      <p>Cells, vesicles, and the path from laboratory studies to clinical research.</p>
      <span class="neuropia-link-label">Explore our research <span aria-hidden="true">↗</span></span>
    </a>
    <a class="neuropia-feature" href="{{ '/people/' | relative_url }}">
      <span class="neuropia-eyebrow">Our group</span>
      <h2>People</h2>
      <p>Meet our {{ site.data.members | size }} current members.</p>
      <span class="neuropia-link-label">View the group <span aria-hidden="true">↗</span></span>
    </a>
    <a class="neuropia-feature" href="{{ '/publications/' | relative_url }}">
      <span class="neuropia-eyebrow">Our work</span>
      <h2>Publications</h2>
      <p>Research publications from Neuropia.</p>
      <span class="neuropia-link-label">View publications <span aria-hidden="true">↗</span></span>
    </a>
  </div>

  <section class="neuropia-affiliations" aria-labelledby="affiliations-heading">
    <h2 id="affiliations-heading">Affiliations</h2>
    <div class="neuropia-affiliation-grid">
      {% for affiliation in site.data.affiliations %}
        <div>
          <h3>{{ affiliation.name | escape }}</h3>
          <p>{{ affiliation.department | escape }}<br>{{ affiliation.institution | escape }}<br>{{ affiliation.address | escape }}</p>
        </div>
      {% endfor %}
    </div>
  </section>
</div>
