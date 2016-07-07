---
layout: post
title: "Writing and Distributing Sublime Text Packages"
categories: code sublime-text
tags: [sublime-text, package-control, sublime-plugins, python]
---

I wrote this post after finishing my first ST plugin, a simple chunk of code that [sorts comma-separted lists](https://github.com/kylebebak/sublime_sort_list).

## Writing the Plugin

A Sublime Text plugin consists of, at the very least, a Python module with a class that inherits from one of the `sublime_plugin` classes, like `TextCommand`. If you want to expose settings that the user can modify, you will need a `.sublime-settings` file. The convention is to name it `<package_name>.sublime-settings`. Users can override it by simply placing a file with the same name in their `Packages/User` directory.

~~~json
// SortList.sublime-settings
{
  "start_list_chars": "[{(<",
  "end_list_chars": "]})>"
}
~~~

If your plugin is interactive in any way, it's advisable to include a `Main.sublime-commands` file, so that users can discover how to use your plugin via the __Command Palette__. A common way to name captions for your commands is `<package_name>: <command_description>`.

~~~json
// Main.sublime-commands
[
  { "caption": "SortList: Sort List", "command": "sort_list" }
]
~~~

If you want to include default keyboard shortcuts to commands provided by your plugin, you need to include `Default (OSX|Linux|Windows).sublime-keymap`, depending on the platform.

Here's what the project directory for `SortList` looks like:

~~~
├── LICENSE
├── Main.sublime-commands
├── README.md
├── demo
│   └── sort.gif
├── sort_list.py
├── SortList.sublime-settings
├── sorted_string.py
└── tests
    ├── __init__.py
    └── test_sorted_string.py
~~~


## Distribution via Package Control

>Most of the info in this section comes from [the Package Control docs](https://packagecontrol.io/docs/submitting_a_package), which are excellent. This is less general and based on my experience.

To make your package downloadable via __Package Control__, fork [package_control_channel](https://github.com/wbond/package_control_channel), and add the following to `repository/<letter>.json`, where `<letter>` is the first letter in the `name` of your package:

~~~json
// repository/s.json
{
    "name": "SortList",
    "details": "https://github.com/kylebebak/sublime_sort_list",
    "releases": [
        {
            "sublime_text": "*",
            "tags": true
        }
    ]
},
// ...
~~~

The above config would indicate that your plugin works for all platforms and all versions of Sublime Text. The `details` field must point to your plugin's GitHub repo. The `name` field will be the name of your plugin on Package Control, regardless of the name of your GitHub repo or the top-level module that runs your plugin.

### Naming your Package
Package Control recommends you use camel case or underscores in your package name. Because you can name your package's GitHub repo anything, give it a name that alludes to the fact it's a Sublime Text package, like `sublime-<package_name>`, __but don't include any variation of "sublime" in your actual package name__. All Sublime Text packages are obviously, well, Sublime Text packages. Including "sublime" in the package name adds noise and makes it less likely that people will think you are a h4x0r.

### Final Steps
Before you submit your pull request to `package_control_channel`, __make sure you have pushed at least one [semver](http://semver.org/) compliant tag to your plugin's repo__. When someone searches for your package by invoking `Package Control: Install Package`, the description will be pulled from your repo, so make sure to give your repo a sensible, succinct description.

Now, submit your pull request. The Package Control maintainers will vet your package and give you feedback. Once you've worked through any issues your package may have, and everything looks good to the maintainers, they will merge your pull request, and your package will be available on Package Control.

If you need to update your plugin, push another tag to your plugin's repo to create a new [release](https://github.com/kylebebak/sublime_sort_list/releases). People searching for your package will see the latest release. 
