---
layout: page
permalink: /publications/
title: Publications
description: Research publications from Neuropia
nav: true
nav_order: 2
---

{% capture group_publications %}{% bibliography %}{% endcapture %}
{% assign publication_markup = group_publications | strip %}
{% if publication_markup contains '<li' %}
{% include bib_search.liquid %}
  <div class="publications">{{ group_publications }}</div>
{% else %}
  <p>We are preparing the group's publication list. Please check back for updates.</p>
{% endif %}
