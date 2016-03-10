---
layout: post
title: "How to quickly cycle between Sublime Text color schemes"
categories: code sublime-text
tags: [sublime-text, sublime-linter, dev-hacks, color-schemes]
---

If you use more than one color scheme in Sublime Text, for example `Solarized (Light)` during the day and `Solarized (Dark)` at night, here's a simple plugin to make switching between them as painless as possible. Instead of having to click and hover through __Sublime Text > Preferences > Color Scheme > Color Scheme - Default > {your_color_scheme}__, you can simply bind some keys to cycle through a series of color schemes of your choice.

First, create a file called `cycle_color_scheme.py`, and put it in `Packages/User`. Here's mine:

~~~python
import sublime, sublime_plugin

class CycleColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):

        preferences = sublime.load_settings('Preferences.sublime-settings')
        scheme = self.view.settings().get("color_scheme")

        try:
            schemes = kwargs.get("color_schemes")
            i = schemes.index(scheme)
            preferences.set(
                'color_scheme', schemes[ (i+1) % len(schemes) ])
        except ValueError:
            print("Your current color scheme doesn't match any of your args.")
        except Exception:
            print("Something went wrong.")
~~~

Then, add the following to your `Default (OSX).sublime-keymap`, also in the `Packages/User` directory. Put your favorite color schemes in the `color_schmes` list. These need to be entered as relative paths to color scheme files: `{color_scheme}.tmTheme`.

~~~json
{
    // ...
    
    "keys": ["super+shift+c"], "command": "cycle_color_scheme",
    "args": { "color_schemes": [
        "Packages/User/SublimeLinter/Solarized (Light) (SL).tmTheme",
        "Packages/User/SublimeLinter/Solarized (Dark) (SL).tmTheme",
        "Packages/User/SublimeLinter/Monokai (SL).tmTheme"
      ]
    }

    // ...
}
~~~

If you use [SublimeLinter](./sublime-linter), any color scheme you use will get copied into `Packages/User/SublimeLinter`, and you're set. If not, you can use something like [Colorsublime](http://colorsublime.com/) to download themes, and put them somewhere in `Packages/User`. 
