---
layout: page
permalink: /people/christopher-elnan-kvistad/
title: Christopher Elnan Kvistad
description: Neuropia research group
member_slug: christopher-elnan-kvistad
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

{% assign member = site.data.members | where: 'slug', page.member_slug | first %}

<p><a href="{{ '/people/' | relative_url }}">← All people</a></p>

<div class="neuropia-member-profile">
  <figure class="neuropia-profile-figure">
    <img class="neuropia-profile-photo" src="{{ member.image | prepend: '/assets/img/' | relative_url }}"
      alt="Profile image for {{ member.name | escape }}" width="{{ member.image_width }}" height="{{ member.image_height }}"
      loading="eager" decoding="async">
  </figure>
  <div class="neuropia-profile-copy" markdown="1">
<p class="neuropia-profile-role">{{ member.role | escape }}</p>

**MD, PhD · Consultant neurologist · Associate professor**

## About

Christopher Elnan Kvistad is a consultant neurologist at Haukeland University Hospital and an associate professor at the University of Bergen, Norway. He co-leads Neuropia with Torbjørn Kråkenes. The group is dedicated to developing novel therapeutic strategies for neural repair and regeneration.

His research focuses on translating experimental discoveries into clinical treatments for neurological diseases, particularly multiple sclerosis and Parkinson’s disease. His work includes clinical trials of regenerative therapies, as well as preclinical research involving mesenchymal stromal cells, extracellular vesicles, and emerging RNA-based technologies.

He is the principal investigator of several investigator-initiated clinical studies, including SMART-MS and NORSEMAN-MS, and leads the development of novel extracellular vesicle-based treatment strategies.

His overarching research goal is to develop therapies that promote repair of the damaged central nervous system and improve neurological function.

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
