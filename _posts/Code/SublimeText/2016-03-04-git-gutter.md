---
layout: post
title: "Getting GitGutter to play nice with SublimeLinter"
categories: code sublime-text
tags: [sublime-text, git, git-gutter, sublime-linter]
---

[GitGutter](https://github.com/jisaacks/GitGutter) lets you see in real time what's changed since a past commit. After each edit of the current view, it invokes `git diff` against a commit of your choosing and displays an icon in the gutter for each line that was __inserted__, __modified__, or __deleted__.

Calls to `git diff` are debounced in the same way that [SublimeLinter](./sublime-linter) debounces calls to linting executables.

The only thing that bothered me is that the GitGutter icons and SublimeLinter icons compete for that primo gutter real estate. It's a race condition: whichever plugin renders its icons first gets overwritten moments later by the other. I'd rather know that my code will blow up at runtime than know if it's been modified, so I wanted SublimeLinter to have precedence.

Luckily, GitGutter's API allows you to specified __"protected_regions"__ of the gutter that are off limits to the plugin, and [buried in here](https://github.com/jisaacks/GitGutter/issues/113) are the regions corresponding to SublimeLinter.

Simply make your own `GitGutter.sublime-settings` in `Packages/User`, and edit the `protected_regions` as follows:

~~~json
// ...
"protected_regions": [
  "sublimelinter-warning-marks",
  "sublimelinter-error-marks",
  "sublimelinter-warning-gutter-marks",
  "sublimelinter-error-gutter-marks",
]
// ...
~~~

Voilà! GitGutter gets out of SublimeLinter's way, and everyone's happy.

![](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/git_gutter_sublime_linter.png)
