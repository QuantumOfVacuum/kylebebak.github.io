---
layout: post
title: "How to quickly cycle between Sublime Text color schemes"
categories: code sublime-text
tags: [sublime-text, dev-hacks, color-schemes]
---

~~~json
{
    "keys": ["super+shift+c"], "command": "toggle_color_scheme",
    "args": { "color_schemes": [
        "Packages/User/SublimeLinter/Solarized (Light) (SL).tmTheme",
        "Packages/User/SublimeLinter/Solarized (Dark) (SL).tmTheme",
        "Packages/User/SublimeLinter/Monokai (SL).tmTheme"
      ]
    }
}
~~~

~~~python
import sublime, sublime_plugin

class ToggleColorSchemeCommand(sublime_plugin.TextCommand):
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



http://www.sublimelinter.com/en/latest/usage.html#choosing-color-schemes
`Packages/User/SublimeLinter`

improving solarized dark

~~~xml
...
<key>lineHighlight</key>
<string>#074652</string>
<key>selection</key>
<string>#074652</string>
...
~~~


`Packages/Seti_UI/Main/Widget - Seti.stTheme`

~~~xml
...
    <key>background</key>
    <string>#313131</string>
...
    <key>selection</key>
    <string>#00a3a3</string>
...
~~~

`Packages/Seti_UI/Seti.sublime-theme`

~~~json
...
{
    "class": "sidebar_tree",
    "settings": ["Seti_sb_small_padding"],
    "row_padding": [8,4]
},
...
~~~

and then insert `"Seti_sb_small_padding": true,` into your `Preferences.sublime-settings`
