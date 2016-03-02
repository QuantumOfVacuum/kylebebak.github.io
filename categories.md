---
layout: page
title: Categories
permalink: /categories
custom_css: categories
---

{% capture categories %}{% include categories.md %}{% endcapture %}
{{ categories | markdownify }}
