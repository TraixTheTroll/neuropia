---
layout: neuropia
permalink: /people/lars-bo/
title: Lars Bø
description: Neuropia research group
member_slug: lars-bo
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

Lars Bø is a professor at the Department of Clinical Medicine, University of Bergen, and a consultant neurologist at Haukeland University Hospital. He trained in medicine at the University of Bergen and completed his doctorate there in 1998, studying the immunopathology of inflammation and demyelination in multiple sclerosis.

His research examines how inflammation, loss of myelin, and damage to nerve fibres contribute to multiple sclerosis. His neuropathological studies have helped characterise demyelination in the cerebral cortex and the involvement of grey matter in the disease.

At Neuro-SysMed, his work connects experimental studies of disease mechanisms with clinical treatment research. He is study director of RAM-MS, a trial comparing autologous haematopoietic stem cell transplantation with high-efficacy treatments for multiple sclerosis. He has also contributed to SMART-MS, which investigated mesenchymal stem cells in progressive multiple sclerosis.

He brings experience in neuropathology, preclinical disease models, and clinical trials to collaborative research on neuroprotection and repair. His work spans both the biological mechanisms underlying multiple sclerosis and the evaluation of potential treatment strategies.

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
