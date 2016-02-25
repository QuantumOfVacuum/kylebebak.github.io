---
layout: post
title: "How to distribute your program via Homebrew"
categories: code homebrew
---

I recently packaged a program I wrote called [notes](https://github.com/kylebebak/notes) for distribution via `Homebrew`, following this [excellent tutorial](http://formalfriday.club/2015/01/05/creating-your-own-homebrew-tap-and-formula.html).

To make your package installable via Homebrew, you put it in a Github repo and create a release. Then you create a __tap__, a repo containing at least one __formula__. The formula is a Ruby file pointing to a downloadable tarball of the package, with instructions on how to build and install it.

When a user downloads your package, the tarball is saved to `/Library/Caches/Homebrew`. It gets unzipped and, depending on the formula, parts of the package are copied to `/usr/local/Cellar/<pkg>/<version>`. This directory, in the user's __cellar__, is called a __keg__.

To make writing formulae easier, you can use [variables for directory locations](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Formula-Cookbook.md#variables-for-directory-locations). For example, `bin.install foo` will create `/usr/local/Cellar/<pkg>/<version>/bin/foo`, use `chmod` to make sure foo is executable, and create a symlink from `/usr/local/bin/foo` to foo in the cellar.

They say [the right example is worth 1000 lines of documentation](https://news.ycombinator.com/item?id=7811482). Enough beating around the bush - here is notes' directory tree, courtesy of [tree](https://en.wikipedia.org/wiki/Tree_(Unix)):

~~~
.
├── LICENSE
├── README.md
├── _completions
│   ├── c.bash
│   ├── c.zsh
│   └── init.sh
├── _config
│   └── env.sh
├── _helpers
│   └── helpers.sh
└── bin
    └── notes
~~~

And here's the formula for installing notes, i.e. building the notes keg:

~~~ruby
class Notes < Formula
  desc "..."
  homepage "https://github.com/kylebebak/notes"
  url "https://github.com/kylebebak/notes/archive/1.0.0.tarball.gz"
  version "1.0.0"
  sha256 "e17405adc655824dec3ca6e2a9a4b199a715743ed5f0948df58f6bb369267aa3"

  def install
    bin.install "bin/notes"
    prefix.install Dir["_completions"]
    prefix.install Dir["_helpers"]
    prefix.install Dir["_config"]
  end
end

~~~

This `install` method creates a keg with the same directory tree as the one in source code, while ignoring metadata like `README.md` and `LICENSE`, and tests or CI scripts, if I had any. The `prefix.install` method copies the directories into the cellar without polluting the executable namespace under `/usr/local/bin`. The only symlink created by this formula is `/usr/local/bin/notes`.

Once you have your tarball release and your tap on Github, users can install your program with two shell commands:

~~~sh
brew tap kylebebak/notes
brew install notes
~~~

Tab completion is crucial to __notes__' usability. Enabling it was the trickiest part of writing notes; I explain how in [this post](../Shell/enabling-tab-completion).
