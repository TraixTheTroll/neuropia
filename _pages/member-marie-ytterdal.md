---
layout: page
permalink: /people/marie-ytterdal/
title: Marie Ytterdal
description: Neuropia research group
member_slug: marie-ytterdal
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

{% assign member = site.data.members | where: 'slug', page.member_slug | first %}

<p><a href="{{ '/people/' | relative_url }}">← All people</a></p>

<div class="neuropia-member-profile">
  <figure class="neuropia-profile-figure">
    <a href="{{ member.image | prepend: '/assets/img/' | relative_url }}" aria-label="Open full-size profile image for {{ member.name | escape }}">
      <img class="neuropia-profile-photo" src="{{ member.image | prepend: '/assets/img/' | relative_url }}"
        alt="Profile image for {{ member.name | escape }}" width="{{ member.image_width }}" height="{{ member.image_height }}"
        loading="eager" decoding="async">
    </a>
    <figcaption><a href="{{ member.image | prepend: '/assets/img/' | relative_url }}">View full-size image</a></figcaption>
  </figure>
  <div class="neuropia-profile-copy" markdown="1">
<p class="neuropia-profile-role">{{ member.role | escape }}</p>

## About

A short biography and research interests will be added here.

  </div>
</div>
