---
layout: post
title: "Add Bash and Zsh tab completion to your shell script"
categories: code shell
tags: [shell, ui, software-design]
---

Tab completion can be a big usability win for CL tools, but building it into your program isn't straightforward, and there aren't many how-to resources online. Luckily, I found [this excellent tutorial](https://blog.jcoglan.com/2013/02/12/tab-completion-for-your-command-line-apps/) written by James Coglan, and used it to build tab completion for my program [notes](https://github.com/kylebebak/notes).

He bases his tutorial on the tab completions offered by [rbenv](https://github.com/rbenv/rbenv), the Ruby environment and package manager. Incidentally, this is similar to how __rbenv__'s Python counterpart, __virtualenv__, deploys tab completions.

When I type in `notes` at the command line and hit tab, a function is invoked that builds and displays a list of notes.

![notes tab completion](https://raw.githubusercontent.com/kylebebak/posts/master/_assets/img/notes_tab_completion.gif)

The completions I wrote work for __Bash__ and __Zsh__. When the shell starts up, a shell-specific completion function is defined, and hooked into the shell with one of the following commands:

~~~sh
# Bash
complete -F <completion_function> notes
# Zsh
compctl -K <completion_function> notes
~~~

There are a few ways to make sure this happens. [One](http://www.debian-administration.org/article/317/An_introduction_to_bash_completion_part_2) is to put a script with the completion function and the command in a special, shell-specific directory, like `/etc/bash_completion.d`. The one I prefer, used by rbenv and virtualenv, is to require the user to source the completion script himself by adding a line to his shell startup file:

~~~sh
# rbenv
eval "$(rbenv init -)"
# virtualenv
source /usr/local/bin/virtualenvwrapper.sh
# notes
which notes >/dev/null && . "$( notes -i )"
~~~

I like this method because it doesn't depend on the special completion directories, and it doesn't deploy files to them. In the case of notes, if `notes -i` is invoked, it returns the absolute path of the completion "control" script. This script decides which shell-specific completion script to invoke, depending on the shell. The user simply sources this control script in his startup file, and boom, notes gets tab completions!
