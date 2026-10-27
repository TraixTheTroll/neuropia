---
layout: page
permalink: /people/
title: People
description: Current members of Neuropia
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/neuropia.css' | relative_url }}">

<ul class="neuropia-people-grid" aria-label="Current group members">
  {% for member in site.data.members %}
    <li class="neuropia-person">
      {% assign profile_path = '/people/' | append: member.slug | append: '/' %}
      <a class="neuropia-person-link" href="{{ profile_path | relative_url }}" aria-label="View profile of {{ member.name | escape }}">
        {% if member.image %}
          <img class="neuropia-avatar" src="{{ member.image | prepend: '/assets/img/' | relative_url }}" alt=""
            width="{{ member.image_width }}" height="{{ member.image_height }}" loading="lazy" decoding="async">
        {% else %}
          <span class="neuropia-avatar neuropia-initials" aria-hidden="true">{{ member.initials | escape }}</span>
        {% endif %}
        <h2>{{ member.name | escape }}</h2>
        {% if member.role %}<p class="neuropia-role">{{ member.role | escape }}</p>{% endif %}
        <span class="neuropia-link-label">View profile <span aria-hidden="true">↗</span></span>
      </a>
      {% if member.bio %}<p>{{ member.bio | escape }}</p>{% endif %}
      {% if member.email or member.orcid or member.website %}
        <ul class="neuropia-member-links" aria-label="Links for {{ member.name | escape }}">
          {% if member.email %}<li><a href="mailto:{{ member.email | escape }}">Email</a></li>{% endif %}
          {% if member.orcid %}<li><a href="https://orcid.org/{{ member.orcid | escape }}">ORCID</a></li>{% endif %}
          {% if member.website %}<li><a href="{{ member.website | escape }}">Profile</a></li>{% endif %}
        </ul>
      {% endif %}
    </li>
  {% endfor %}
</ul>
