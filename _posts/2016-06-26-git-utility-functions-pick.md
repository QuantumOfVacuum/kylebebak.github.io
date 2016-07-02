---
layout: post
title: "Git Helpers and Other Utility Functions Using pick"
categories: code git
tags: [git, shell, dev-hacks, pick, thoughtbot]
---

## Git and pick

`git` can be a bit of a pain, especially when passing branches or commit hashes as args. Big projects have lots of branches and tons of commits. Finding and copying commit hashes to compare commits, for example, is awkward and slow. In my case, the awkwardness meant I wasn't getting nearly as much mileage out of Git as I should have been.

Then I read about [pick](https://github.com/thoughtbot/pick) from [thoughtbot](https://thoughtbot.com/). It's a command line tool you can use to "fuzzy select anything". Pipe it a list of options and an `ncurses` interface will open, allowing you to fuzzy search the options and send the one you pick to `stdout`.

Looking at the gif on pick's README, I realized selecting branches and commit hashes would be a __lot__ faster with fuzzy search, so I wrote [some utility functions](https://github.com/kylebebak/dotfiles/blob/master/dotfiles/.helpers/pick.sh) that invoke pick to do exactly that. Since then my usage of and satisfaction with Git have gone up drastically. Here are descriptions of the helper functions.

- `gbp [command]`: Pick a branch and pass it to __command__ (__gbp git checkout__, __gbp git merge__, etc). If __command__ is not passed, pick and copy branch name.
- `gbpf`: Pick a branch, pick a modified file from this branch, and diff it.
- `ghp [command]`: Pick a past commit and pass it to __command__. If __command__ is not passed, pick and copy commit hash.
- `ghpf`: Pick a past commit, pick a modified file from this commit, and diff it.
- `gbc [arg]`: Pick a branch and find out how far ahead or behind (number of commits) it is compared with current branch. If any __arg__ is passed, pick both branches.
- `gbca [arg]`: Like __gbc__, but shows names and hashes of commits.
- `gdp`: Pick a file that has been modified since the last commit, and diff it.

The gif below gives an idea of just how effective `pick` can be for these tasks, using `ghpf`. Remember, this function is for first picking a commit, then picking one of the files that has changed since that commit, and diffing the file. At the end, `ghpf` echoes the command it executed.

![pick ghpf](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/pick_ghpf.gif)

Think of how long it would take to run `git log` and `git diff` and build up that command in your text editor. Using `pick` it takes a few seconds.


## Other Helpers

Here's an alias I use that I named `psp`. Read it and see if you can guess what it does.

~~~sh
ps -ef | pick | awk '{print \$2}' | xargs echo -n | pbcopy
~~~

That's right... Pick any process on your machine, parse and clean the `PID`, and copy it to the clipboard.

![pick psp](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/pick_psp.gif)

Basically, `pick` is your friend whenever you need to search a list of anything. For commands that generate big lists, `pick` can be so effective that it changes how you think of and use these commands, which is what happened to me with `git`.
