---
layout: post
title: "Blogging like a hacker with Jekyll"
categories: code jekyll
tags: [github, github-pages, jekyll]
---

Jekyll is awesome.

<https://gist.github.com/cobyism/4730490>

`_hooks/pre-commit`

~~~sh
#!/bin/bash -e

# build categories and sidebar before every commit
python _build/categories.py _posts > categories.md
python _build/sidebar.py _posts > _includes/sidebar.md
git add categories.md _includes/sidebar.md
~~~

The -e flag in the shebang line ensures that this hook exits if any of its commands exits with a non-zero exit status.
