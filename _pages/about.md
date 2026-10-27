---
layout: about
title: Home
permalink: /
description: Neuropia research group in Bergen, Norway
subtitle: Research group · Bergen, Norway
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

<div class="neuropia-home">
  <p class="neuropia-lead">
    Neuropia brings together researchers affiliated with Neuro-SysMed, Haukeland University Hospital,
    and the University of Bergen.
  </p>
  <p>Meet the people in our group and follow our research outputs.</p>

  <div class="neuropia-feature-grid">
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
