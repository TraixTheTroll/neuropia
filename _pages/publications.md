---
layout: page
permalink: /publications/
title: Publications
description: Selected publications by Neuropia members
nav: true
nav_order: 3
---

This selection covers mesenchymal stem cells, extracellular vesicles, multiple sclerosis, and neural regeneration. It includes clinical, laboratory, and review publications by current members, including collaborative work.

{% capture group_publications %}{% bibliography %}{% endcapture %}
{% assign publication_markup = group_publications | strip %}
{% if publication_markup contains '<li' %}
{% include bib_search.liquid %}
  <div class="publications">{{ group_publications }}</div>
{% else %}
  <p>We are preparing the group's publication list. Please check back for updates.</p>
{% endif %}
