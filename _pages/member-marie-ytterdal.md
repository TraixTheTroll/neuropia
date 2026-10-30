---
layout: neuropia
permalink: /people/marie-ytterdal/
title: Marie Ytterdal
description: Neuropia research group
member_slug: marie-ytterdal
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

Marie Ytterdal holds a Bachelor’s degree in Biomedicine from the University of Tromsø and a Master’s degree in Biomedical Science from the University of Bergen, completed in 2024. She is currently a PhD candidate at Neuro-SysMed, Haukeland University Hospital and the University of Bergen.

Her research focuses on the anti-inflammatory potential of mesenchymal stem cell (MSC)-derived extracellular vesicles (EVs) in multiple sclerosis. Her doctoral project investigates how these vesicles may influence chronic inflammation, with particular attention to microglia and disease progression.

Her [first-author study](https://doi.org/10.1371/journal.pone.0347119) investigated the shift of bone marrow MSCs towards neural- and glial-like states. This work combines cell culture, proliferation and migration assays, immunofluorescence imaging, and mass-spectrometry-based protein profiling.

Her contributions span experimental methodology, quantitative analysis, data curation, and computational work. Within Neuropia, she connects studies of MSC biology with research on potential cell- and EV-based treatments for multiple sclerosis.

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
