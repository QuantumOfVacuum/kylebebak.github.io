---
layout: post
comments: true
title: "Building Your GitHub Pages Site Alongside Your Code"
categories: code jekyll
tags: [github, github-pages, jekyll]
---

If you have a project on GitHub, and you host the project site with [GitHub Pages](https://pages.github.com/), you might well have a `_site` or `dist` directory or something similar living alongside your application code.

In Jekyll's case, your site is built from the files in `_site` every time you push them to the `gh-pages` branch. Wouldn't it be nice if every time you pushed your code to `master`, you could push just the `_site` directory to `gh-pages`, and thus ensure that your documentation was always up to date with your application code?

It turns out [some smart GitHub users](https://gist.github.com/cobyism/4730490) have suggested using `git subtree push` to push a subdirectory in your repo to `gh-pages`. My addition to the recipe is putting this code in a `pre-push` hook that runs only when you push to `master`.

If you'd like to do the same, put this code into `.git/hooks/pre-push`.

~~~sh
#!/bin/bash

# push _site directory to gh-pages
while read oldrev newrev refname
do
  branch=$(git rev-parse --symbolic --abbrev-ref $refname)
  if [ "$branch" == "master" ]; then
    git subtree push --prefix _site origin gh-pages
  fi
done

printf "\n"
~~~

Enjoy =)
