---
layout: neuropia
permalink: /people/christian-gronas/
title: Christian Grønås
description: Neuropia research group
member_slug: christian-gronas
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

Christian Grønås holds a bachelor's degree in Biomedicine from UiT – The Arctic University of Norway and a master's degree in Molecular Biology from the University of Bergen (UiB). His master's research focused on tissue-specific lipid alterations in Parkinson's disease, using lipidomics to investigate changes in the brain. He has also worked as a research assistant at Eterna Health, where he contributed to research on cell-based therapies for autoimmune diseases.

Christian is currently a researcher at Neuro-SysMed, Haukeland University Hospital, where his work focuses on Multilineage-differentiating Stress-Enduring (Muse) cells and their potential applications in multiple sclerosis (MS). His project investigates the regenerative and immunomodulatory properties of Muse cells, comparing their therapeutic potential with conventional and hypoxia-conditioned mesenchymal stromal cells and their extracellular vesicles. The research aims to explore novel cell-based approaches to neuroregeneration, remyelination, and the regulation of neuroinflammation.

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
