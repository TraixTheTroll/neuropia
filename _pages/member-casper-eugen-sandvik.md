---
layout: neuropia
permalink: /people/casper-eugen-sandvik/
title: Casper Eugen Sandvik
description: Neuropia research group
member_slug: casper-eugen-sandvik
nav: false
---

{% assign member = site.data.members | where: 'slug', page.member_slug | first %}

<p><a href="{{ '/#people' | relative_url }}">← All people</a></p>

<div class="neuropia-member-profile">
  <figure class="neuropia-profile-figure">
    <img class="neuropia-profile-photo" src="{{ member.image | prepend: '/assets/img/' | relative_url }}"
      alt="Profile image for {{ member.name | escape }}" width="{{ member.image_width }}" height="{{ member.image_height }}"
      loading="eager" decoding="async">
  </figure>
  <div class="neuropia-profile-copy" markdown="1">
<p class="neuropia-profile-role">{{ member.role | escape }}</p>

## About

Casper Eugen Sandvik holds a Master’s degree in Biomedicine from the University of Bergen. His Master’s thesis investigated the transdifferentiation of mesenchymal stem cells (MSCs) and the characterisation of the extracellular vesicles (EVs) they release.

Casper is currently pursuing a PhD at Neuro-SysMed, Haukeland University Hospital and the University of Bergen, where his research centres on MSC-derived small extracellular vesicles (sEVs) as potential therapeutics for multiple sclerosis and other neurodegenerative disorders.

He brings a multidisciplinary background, with hands-on experience in cell culture and cell-based assays, immunostaining, and animal studies. His EV expertise covers isolation and characterisation (ultracentrifugation, EXODUS, nanoparticle tracking analysis, transmission electron microscopy) and multi-omics (DIA LC-MS/MS proteomics, miRNA sequencing). He complements this with data analysis and bioinformatics skills in Python, R, and bash.

Currently, Casper is expanding into lipid nanoparticle (LNP) and EV-based delivery strategies targeting immune and neural cells.

## Research interests

- Small extracellular vesicles (sEVs)
- Mesenchymal stem cells (MSCs)
- Bioinformatics
- Omics
- Lipid nanoparticles (LNPs)

{% if member.email or member.linkedin or member.orcid or member.website %}
<h2>Links</h2>
{% if member.linkedin or member.orcid or member.website %}
<ul class="neuropia-member-links" aria-label="Links for {{ member.name | escape }}">
  {% if member.linkedin %}<li><a href="{{ member.linkedin | escape }}">LinkedIn</a></li>{% endif %}
  {% if member.orcid %}<li><a href="https://orcid.org/{{ member.orcid | escape }}">ORCID</a></li>{% endif %}
  {% if member.website %}<li><a href="{{ member.website | escape }}">Institutional profile</a></li>{% endif %}
</ul>
{% endif %}
{% if member.email %}<p class="neuropia-profile-email"><strong>Email:</strong> <a href="mailto:{{ member.email | escape }}">{{ member.email | escape }}</a></p>{% endif %}
{% endif %}

  </div>
</div>
