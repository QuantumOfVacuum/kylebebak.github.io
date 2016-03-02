---
layout: post
title: 'Exponential navigation, and chaining Sublime Text API calls'
categories: code sublime-text
tags: [sublime-text, dev-hacks]
---

I've never been much of a Vim user, but people I respect swear by it. Among its "super powers" is lightning fast navigation in normal mode. I like being able to hit <kbd>5</kbd>,<kbd>j</kbd> and move up 5 lines, because often one line at a time is too slow, and ~40 lines with <kbd>Page Up</kbd> is too fast.

But using Vintage Mode for this alone seemed like overkill, so I decided I would find a Sublime Text plugin that could chain multiple calls to __"move cursor up a line"__, and so forth, and put these in my keymap. I stumbled upon [this one](https://github.com/kylebebak/sublime_text_config/blob/master/run_multiple_commands.py) in the ST forums, which does the job nicely. To enable it, simply put this file, `run_multiple_commands.py`, into the `User` directory under your Sublime Text packages.

If you want to chain calls to the ST API in your __keymap__, it helps to know what those calls look like. Fortunately, there's an easy way to find out. Bring up the __console__ with <kbd>ctrl</kbd>+<kbd>`</kbd>, and enter `sublime.log_commands(True)`. Now, every call you make to the API by pressing key(s) or clicking your mouse will get logged to the console, and you can copy it almost as is into your keymap. [Here's my keymap](https://github.com/kylebebak/sublime_text_config/blob/master/Default%20(OSX).sublime-keymap), and here's an excerpt with some entries that __run multiple commands__.

~~~json
{ "keys": ["alt+up"],
"command": "run_multiple_commands",
"args": {
  "commands": [
  {"command": "move", "args": {"by": "lines", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "lines", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "lines", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "lines", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "lines", "forward": false}, "context": "window" }
  ]
}
},

...

{ "keys": ["ctrl+alt+left"],
"command": "run_multiple_commands",
"args": {
  "commands": [
  {"command": "move", "args": {"by": "wordends", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "wordends", "forward": false}, "context": "window" },
  {"command": "move", "args": {"by": "wordends", "forward": false}, "context": "window" },
  ]
}
},
~~~

## Exponential navigation
I can hit <kbd>alt</kbd>+<kbd>up/down</kbd> to move 5 lines up or down, adding <kbd>shift</kbd> to highlight these lines, and I can do the same with <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>left/right</kbd> to move 3 words left or right.

I've been using this system for over a year. Arriving at 5 lines for vertical movement and 3 words for lateral movement was part intuition and part trial and error. The intuition behind it was enabling navigation whose sensitivity struck a __exponential middle ground__ between:

- <kbd>up/down</kbd> &#8594; <kbd>?</kbd> &#8594; <kbd>Page Up/Page Down</kbd>
    - 1 line &#8594; 5 lines &#8594; ~40 lines
- <kbd>alt</kbd>+<kbd>left/right</kbd> &#8594; <kbd>?</kbd> &#8594; <kbd>super</kbd>+<kbd>left/right</kbd>
    - 1 word &#8594; 3 words &#8594; ~15 words

In practice, the system is natural and smooth. After a while, choosing which of the 3 "levels" of sensitivity is most appropriate requires almost no cognitive effort, but at the same time it doesn't feel imprecise. If you're moving down to something 19 lines away, you hit <kbd>alt</kbd>+<kbd>down</kbd> a few times, watching the cursor as you go, hit up, and you're there. It turns out a few times was 4, ___but you didn't have to think about it___, because you had visual feedback the whole way.

If your file is 250 lines long, 10 movements will get you to any line in the file. Typically, this will be more like 4. It's fast and relatively mindless, which is what I want in navigation. I'd rather focus on the code.
