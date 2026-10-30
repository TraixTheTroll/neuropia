---
layout: neuropia
permalink: /people/torbjorn-krakenes/
title: Torbjørn Kråkenes
description: Neuropia research group
member_slug: torbjorn-krakenes
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

Torbjørn Kråkenes holds a BSc in Nanotechnology and an MSc in Medical Cell Biology from the University of Bergen. He completed his PhD there in 2021, investigating the proteins recognised by Yo autoantibodies in paraneoplastic cerebellar degeneration.

He is a senior researcher at Neuro-SysMed, Haukeland University Hospital, and co-leads Neuropia with Christopher Elnan Kvistad. As the principal investigator for the group’s laboratory-based basic research, he leads its experimental work on potential approaches to neural repair and regeneration.

His research focuses on neuronal injury, neuroprotection, and the therapeutic potential of mesenchymal stem cells (MSCs) and their extracellular vesicles (EVs) in multiple sclerosis. His work spans neuronal cell culture, protein localisation, and preclinical animal studies, including investigations of MSCs in models of demyelination.

He has also contributed to the SMART-MS clinical trial of mesenchymal stem cells in progressive multiple sclerosis. This work connects his background in experimental neurobiology with the clinical evaluation of potential regenerative therapies.

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
