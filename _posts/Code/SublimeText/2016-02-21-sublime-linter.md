---
layout: post
title: "SublimeLinter for code linting in any language"
categories: code sublime-text
---

[SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) is a code linting framework for Sublime Text. Its design is straightforward and very effective, and I feel like writing about it.

>In [background mode](https://sublimelinter.readthedocs.org/en/latest/lint_modes.html#background), lint requests are generated for every modification of a view, as well as on file loading and saving... Remember that background lint requests only trigger a lint if the associated view has not been modified when the request is pulled off the queue...

On each modification of a view, a lint request is enqueued. After a delay, the request gets pulled off the queue. If no other requests were added to the queue during the delay, i.e. the current request is the only request on the queue when it gets pulled off, then it triggers a lint. This debounces linting requests, like in the [auto-save](https://github.com/jamesfzhang/auto-save) plugin I contribute to. The lint looks at the syntax of the file, and runs all of the SublimeLinter __linters__ assigned to the syntax of the view. Each __linter__, in turn, calls the command line executable it uses for linting (`eslint`, `javac -Xlint`, `pyflakes`, `ruby -wc`, ...), retrieves line-specific warnings and errors, and returns them to SublimeLinter. SublimeLinter finishes up by aggregating the errors and displaying them in the gutter. Here's a [detailed description](https://sublimelinter.readthedocs.org/en/latest/usage.html#usage-linting) from the excellent documentation.

The SublimeLinter __linters__ I mentioned above are separate packages that must be installed with Package Control. SublimeLinter manages delegation details, like displaying errors and managing the queue of lint requests, but does no linting on its own. If you were paying attention above, you noticed that __linters__ don't lint either; they delegate lint requests to their command line linter of choice.

This modular design makes SublimeLinter easy to extend. To add linting for a new syntax, e.g. [ES6 JS or JSX](../javascript/eslint), you don't even touch SublimeLinter. You create a package that calls a linting executable and passes the results to SublimeLinter, basing your code on the many existing linting packages.

SublimeLinter settings are specified in `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/SublimeLinter.sublime-settings`. Here you can change the "debounce" `delay`, the `lint_mode`, configure individual linters, and define a `syntax_map` to make sure your linters are called for files with specialized syntax.

~~~json
{
    "user": {
        ...
        "delay": 0.5,
        ...
        "lint_mode": "background",
        "linters": {
            "eslint": {
                "@disable": false,
                "args": [],
                "excludes": []
            }
        },
        ...
        "syntax_map": {
            "html (django)": "html",
            "html (rails)": "html",
            "html 5": "html",
            "javascript (babel)": "javascript",
            "php": "html",
            "python django": "python"
        },
        ...
    }
}
~~~

I find IDEs clunky and bloated; they're designed for many things, but not for editing text. Text is the raw material of all programs, __which for me is enough to make IDEs an anti-pattern__. Code linting, however, has always been one of their strong points. SublimeLinter gives you industrial strength code linting in a lean, mean text editor, which, if this applies to you, is one more reason to drop your IDE.
