---
layout: neuropia
title: Home
permalink: /
description: Mesenchymal stromal cells, extracellular vesicles, and neurological disease
homepage: true
nav: false
---

<header class="hero">
  <img src="{{ '/assets/img/neuropia-logo.png' | relative_url }}" width="3000" height="3000" alt="Neuropia logo" class="logo">
  <h1>NEUROPIA</h1>
  <div class="subtitle">Research group · Bergen, Norway</div>
  <p class="tagline">Exploring the therapeutic potential of mesenchymal stromal cells, extracellular vesicles and lipid nanoparticles in neurological disease — from cellular cultures to clinical translation.</p>
  <a href="#about" class="cta">Explore the cosmos of repair</a>
</header>
<div class="hero-spacer" aria-hidden="true"></div>

<section id="about">
  <div class="section-label">About</div>
  <h2>Cellular messengers, neurological frontiers</h2>
  <div class="section-content">
    <p>Neuropia investigates the therapeutic potential of mesenchymal stromal cells and their extracellular vesicles, with multiple sclerosis as our primary disease focus. Our broader interests extend to other neurodegenerative disorders, including Parkinson’s disease.</p>
    <p>We work at the intersection of advanced cell culture (mesenchymal stromal and neuronal), vesicle biology, and delivery systems such as lipid nanoparticles. The goal is to understand how these vesicles can modulate inflammation, support neuronal survival, and open new paths from laboratory insight to patient care.</p>
    <p>Based at <a href="{{ site.data.affiliations.first.url | escape }}">Neuro-SysMed</a>, Haukeland University Hospital, and the University of Bergen.</p>
  </div>
</section>

<section id="research">
  <div class="section-label">Our focus</div>
  <h2>From vesicle to patient</h2>
  <div class="section-content">
    <p>Neuropia investigates mesenchymal stromal cells (MSCs) and extracellular vesicles (EVs) as potential therapeutic approaches for neurological disease. Multiple sclerosis is our main disease focus, with broader interests in other neurodegenerative disorders, including Parkinson’s disease.</p>
    <p><strong>Mesenchymal stromal cells.</strong> We study the biological properties of MSCs and how they may be modified to support neural protection and repair. Our work includes laboratory studies of neural and glial differentiation, protein expression, and MSC effects in experimental demyelination models.</p>
    <p>Recent studies examine <a href="https://pubmed.ncbi.nlm.nih.gov/42008439/">neural and glial differentiation of bone marrow MSCs</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/37943848/">MSCs in a mouse model of demyelination</a>. These laboratory findings inform further research; they do not establish clinical benefit.</p>
    <p><strong>Extracellular vesicles.</strong> EVs are membrane-enclosed particles released by cells that carry proteins, nucleic acids, and other molecules. We are interested in how MSC-derived EVs influence inflammation and tissue repair, and whether they could support future cell-free therapeutic approaches in MS.</p>
    <p>Group members have reviewed <a href="https://pubmed.ncbi.nlm.nih.gov/39408622/">MSC-derived vesicles as potential treatments for MS</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/40589765/">brain-derived blood biomarkers, including EVs</a>. The therapeutic review discusses preclinical evidence and the challenges of moving toward clinical trials. Its published title uses the term “exosomes”; we use EVs as the broader term here.</p>
    <p><strong>From mechanisms to clinical research.</strong> Understanding therapeutic potential also requires testing safety and efficacy in people. Members contributed to <a href="https://pubmed.ncbi.nlm.nih.gov/42081777/">SMART-MS, a randomized, double-blind, placebo-controlled trial of intrathecal MSCs in progressive MS</a>. The trial did not detect a neuroregenerative effect on its primary outcome and reported safety concerns. It underlines the need to evaluate cell-based approaches carefully, alongside continued research into mechanisms and alternatives such as MSC-derived EVs.</p>
    <div class="focus-grid">
      <div class="card">
        <h3>Mesenchymal stromal cells & EVs</h3>
        <p>Harnessing the immunomodulatory and regenerative properties of mesenchymal stromal cell-derived extracellular vesicles for neurological repair.</p>
      </div>
      <div class="card">
        <h3>Lipid nanoparticles</h3>
        <p>Engineering and studying lipid-based delivery systems to enhance the targeting and cargo of therapeutic vesicles and nanoparticles.</p>
      </div>
      <div class="card">
        <h3>Neuronal & mesenchymal cultures</h3>
        <p>Advanced in vitro models of neuronal and mesenchymal stromal cells to dissect mechanisms of disease and therapeutic response.</p>
      </div>
      <div class="card">
        <h3>Clinical translation</h3>
        <p>Bridging laboratory findings toward clinical research, including work on multiple sclerosis and Parkinson’s disease.</p>
      </div>
    </div>
  </div>
</section>

<section id="people">
  <div class="section-label">Our group</div>
  <h2>People</h2>
  <div class="section-content">
    <p>Current members of Neuropia</p>
    {% include neuropia-people.liquid %}
  </div>
</section>

<section id="publications">
  <div class="section-label">Our work</div>
  <h2>Publications</h2>
  <div class="section-content">
    <p>Selected publications by Neuropia members. This selection covers mesenchymal stromal cells, extracellular vesicles, multiple sclerosis, and neural regeneration. It includes clinical, laboratory, and review publications by current members, including collaborative work.</p>
    {% include neuropia-publications.liquid %}
  </div>
</section>

<section id="contact">
  <div class="section-label">Affiliations & Contact</div>
  <h2>Contact</h2>
  <div class="section-content">
    {% include neuropia-contact.liquid %}
  </div>
</section>
