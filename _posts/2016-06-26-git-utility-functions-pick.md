---
layout: post
title: "Git Helpers and Other Utility Functions Using pick"
categories: code git
tags: [git, shell, dev-hacks, pick, thoughtbot]
---

## Git and pick

`git` can be a bit of a pain, especially when passing branches or commit hashes as args. Big projects have lots of branches and have tons of commits. Finding and copying commit hashes to compare commits, for example, is awkward and slow. This made me reluctant to use Git, which meant I wasn't getting nearly as much mileage out of it as I should have been.

Then I read about [pick](https://github.com/thoughtbot/pick) from [thoughtbot](https://thoughtbot.com/). It's a command line tool you can use to "fuzzy select anything". Pipe it a list of options and an interface will open, allowing you to fuzzy search the options and send the one you pick to `stdout`.

I realized that selecting branches and commit hashes would be a __lot__ faster with fuzzy search. So, I wrote [some utility functions](https://github.com/kylebebak/dotfiles/blob/master/dotfiles/.helpers/pick.sh) that invoke pick to do exactly that, and needless to say my usage of and satisfaction with Git have gone up by an order of magnitude =). Here are descriptions of what they do:

- `gbp [command]`: Pick a branch and pass it to `command` (`gbp git checkout`, `gbp git merge`, etc). If `command` is not passed, pick and copy branch name.
- `gbpf`: Pick a branch, pick a modified file from this branch, and diff it.
- `ghp [command]`: Pick a past commit and pass it to `command`. If command is not passed, pick and copy commit hash.
- `ghpf`: Pick a past commit, pick a modified file from this commit, and diff it.
- `gbc [arg]`: Pick a branch and find out how far ahead or behind (number of commits) it is compared with current branch. If __any__ `arg` is passed, pick both branches.
- `gbca [arg]`: Like `gbc`, but shows names and hashes of commits.
- `gdp`: Pick a file that has been modified since the last commit, and diff it.

Here are a couple of gifs to show how this works, first with `ghp` and then with `gbca`.

![pick ghp](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/pick_ghp.gif)

---

![pick gbca](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/pick_gbca.gif)


## Other Helpers

Here's an alias I use that I named `psp`. Read it and see if you can guess what it does.

~~~sh
ps -ef | pick | awk '{print \$2}' | xargs echo -n | pbcopy
~~~

That's right... Pick any process on your machine, parse and clean the `PID`, and copy it to the clipboard.

![pick pid](https://raw.githubusercontent.com/kylebebak/kylebebak.github.io/master/_assets/img/pick_pid.gif)

Basically, `pick` is your friend whenever you need to search a list of anything. For commands that generate big lists, `pick` can be so effective that it changes how you think of and use these commands, which is what happened to me with `git`.
