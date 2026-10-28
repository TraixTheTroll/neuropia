---
layout: page
permalink: /contact/
title: Contact
description: Enquiries, affiliations, and location
nav: true
nav_order: 4
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

For enquiries about Neuropia, please contact **Christopher Elnan Kvistad** at [christopher.elnan.kvistad@helse-bergen.no](mailto:christopher.elnan.kvistad@helse-bergen.no).

Neuropia is based in Bergen, Norway, with the following affiliations.

{% for affiliation in site.data.affiliations %}

## {{ affiliation.name }}

{{ affiliation.department }}<br>
{{ affiliation.institution }}<br>
{{ affiliation.address }}

{% endfor %}
