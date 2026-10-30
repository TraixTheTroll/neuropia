---
layout: neuropia
permalink: /people/andrea-gremes/
title: Andrea Gremes
description: Neuropia research group
member_slug: andrea-gremes
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

Andrea Gremes holds a Master’s degree in Pharmacy from the University of Innsbruck, Austria. For his Master’s thesis, he conducted preclinical studies investigating a gene therapy approach for mesial temporal lobe epilepsy.

Over the past two years, Andrea has further expanded his expertise through his research on Parkinson’s disease at Neurosymed, gaining valuable insights into disease-related mechanisms and neuronal dysregulation pathways implicated in neurodegenerative disorders.

He brings a multidisciplinary background, complemented by hands-on experience in animal experimentation, cell culture, and transcriptomics techniques, including spatial transcriptomics and single-nucleus RNA sequencing.

Currently, Andrea is undertaking a one-year research internship focused on the production and evaluation of lipid nanoparticles (LNPs) encapsulating therapeutic payloads as potential disease-modifying strategies for neurodegenerative disorders.

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
