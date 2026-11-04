---
layout: neuropia
permalink: /people/anna-maria-rasmussen-eitrheim/
title: Anna-Maria Rasmussen Eitrheim
description: Neuropia research group
member_slug: anna-maria-rasmussen-eitrheim
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

Anna-Maria Rasmussen Eitrheim has a Bachelor's degree in Molecular Biology from the University of Bergen (UiB) and is now doing a Master's in Biomedicine at UiB, writing her thesis at Neuro-SysMed, Haukeland University Hospital.
Her project examines at whether small extracellular vesicles (sEVs) from bone marrow mesenchymal stem cells (MSCs) could help decrease inflammation and/or support ​repair in multiple sclerosis (MS). She compares sEVs from MSC’s of MS patients and of healthy donors, looking at their molecular content and their effect on nerve cells.
She has been trained in cell culture and EV isolation, and has some previous experience with western blotting and preparing protein samples for mass spectrometry."

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
