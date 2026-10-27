---
layout: page
permalink: /contact/
title: Contact
description: Affiliations and location
nav: true
nav_order: 3
---

Neuropia is based in Bergen, Norway, with the following affiliations.

{% for affiliation in site.data.affiliations %}

## {{ affiliation.name }}

{{ affiliation.department }}<br>
{{ affiliation.institution }}<br>
{{ affiliation.address }}

{% endfor %}
