---
layout: post
comments: true
title: "Getting GitGutter to Play Nice with SublimeLinter"
categories: code sublime-text
tags: [sublime-text, git, git-gutter, sublime-linter]
---

[GitGutter](https://github.com/jisaacks/GitGutter) lets you see in real time what's changed since a past commit. After each edit of the current view, it invokes `git diff` against a commit of your choosing and displays an icon in the gutter for each line that was __inserted__, __modified__, or __deleted__.

Calls to `git diff` are debounced in the same way that [SublimeLinter](./sublime-linter) debounces calls to linting executables.

The only thing that bothered me is that __GitGutter__ icons and __SublimeLinter__ icons compete for that primo gutter real estate. It's a race condition: whichever plugin renders its icons first gets overwritten moments later by the other. I'd rather know that my code will blow up at runtime than know if it's been modified, so I wanted SublimeLinter to take precedence.

Luckily, GitGutter's API allows you to specify __"protected_regions"__ of the gutter that are off limits to the plugin, and [buried in here](https://github.com/jisaacks/GitGutter/issues/113) are the regions corresponding to SublimeLinter.

Simply make or copy your own `GitGutter.sublime-settings` in `Packages/User`, and edit the `protected_regions` as follows:

~~~json
// ...
"protected_regions": [
  "sublimelinter-warning-marks",
  "sublimelinter-error-marks",
  "sublimelinter-warning-gutter-marks",
  "sublimelinter-error-gutter-marks",
  "lint-underline-illegal",
  "lint-underline-violation",
  "lint-underline-warning",
  "lint-outlines-illegal",
  "lint-outlines-violation",
  "lint-outlines-warning",
  "lint-annotations",
]
// ...
~~~

Voilà! GitGutter gets out of SublimeLinter's way, and everyone's happy. If this fix stops working, restarting Sublime Text will usually make it work again.

![](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/git_gutter_sublime_linter.png)
