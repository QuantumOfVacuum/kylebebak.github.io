---
layout: post
comments: true
title: "Writing and Distributing Sublime Text Packages"
categories: code sublime-text
tags: [sublime-text, package-control, sublime-packages, python]
---

I wrote this post after finishing my first ST package, a simple chunk of code that [sorts comma-separted lists](https://github.com/kylebebak/sublime_sort_list).


## Useful Links
- [ST3 API reference](https://www.sublimetext.com/docs/3/api_reference.html)
- [package_control_channel repo](https://github.com/wbond/package_control_channel)
- [How to submit a package](https://packagecontrol.io/docs/submitting_a_package)
- [package_reviewer wiki](https://github.com/packagecontrol/package_reviewer/wiki/Package-checks): avoid having your package rejected due to common errors


## Writing the Package
A Sublime Text package consists of, at the very least, a Python module with a class that inherits from one of the `sublime_plugin` classes, like `TextCommand`.


### Settings
If you want to expose settings that the user can modify, you will need a `.sublime-settings` file. The convention is to name it `<package_name>.sublime-settings`. Users can override it by simply placing a file with the same name in their `Packages/User` directory.

~~~json
// SortList.sublime-settings
{
  "start_list_chars": "[{(<",
  "end_list_chars": "]})>"
}
~~~


### Commands
If your package is interactive in any way, it's advisable to include a `Default.sublime-commands` file, so that users can discover how to use your package via the __Command Palette__. A common way to name captions for your commands is `<package_name>: <command_description>`.

~~~json
// Default.sublime-commands
[
  { "caption": "SortList: Sort List", "command": "sort_list" }
]
~~~

The value of the `command` key is derived from the name of one your package's commands, i.e. a class that inherits from `ApplicationCommand`, `WindowCommand` or `TextCommand`.


### Key Bindings
If you want to include default key bindings to commands provided by your package, you need to include `Default.sublime-keymap`.

~~~json
// Default.sublime-keymap
[
  { "keys": ["ctrl+alt+shift+s"], "command": "sort_list" },
]
~~~

If you want platform-specific key bindings, you can override `Default.sublime-keymap` with `Default (OSX|Linux|Windows).sublime-keymap`, for example to use the <kbd>super</kbd> key on OSX.

NOTE: Make sure your key bindings don't override any of the default key bindings on any platform. If they do your package will be rejected. On OSX, you can find these key bindings in the these files: `~/Library/Application Support/Sublime Text 3/Packages/Default/Default (OSX|Linux|Windows).sublime-keymap`.


### Overview
Here's what the project directory for `SortList` looks like. The class `SortListCommand`, which inherits from `sublime_plugin.TextCommand`, is defined in `sort_list.py`. It's picked up automatically by ST because it's in the root of the package.

~~~
├── Default.sublime-keymap
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

The above config indicates your package works for all platforms and all versions of Sublime Text. The `details` field must point to your package's GitHub repo. The `name` field will be the name of your package on Package Control, regardless of the name of your GitHub repo or the top-level module that runs your package.


### Naming your Package
Package Control recommends you use camel case or underscores in your package name. Because you can name your package's GitHub repo anything, you might choose to give it a name that alludes to the fact it's a Sublime Text package, like `sublime-<package_name>`, __but don't include any variation of "sublime" in your actual package name__. All Sublime Text packages are obviously, well, Sublime Text packages. Including "sublime" in the package name adds noise and makes it less likely that people will think you are a h4x0r.


### ChannelRepositoryTools and package_reviewer
To make sure you pull requests for `package_control_channel` is valid, install the `ChannelRepositoryTools` package. Open `package_control_channel` in Sublime Text and run __ChannelRepositoryTools: Test Default Channel__ from the command palette.

Also, be aware that a tool called [package_reviewer](https://github.com/packagecontrol/package_reviewer/blob/master/README.md) will be run against your package. If it raises any errors, your package will be rejected. You can download and run this tool yourself, or you see a list of such errors in the [package_reviewer wiki](https://github.com/packagecontrol/package_reviewer/wiki/Package-checks).


### Release a Version
Before you submit your pull request to `package_control_channel`, __make sure you have pushed at least one [semver](http://semver.org/) compliant tag to your package's repo__. When someone searches for your package by invoking `Package Control: Install Package`, the description will be pulled from your repo, so make sure to give your repo a sensible, succinct description.

Now, submit your pull request. The Package Control maintainers will vet your package and give you feedback. Once you've worked through any issues your package may have, and everything looks good to the maintainers, they will merge your pull request, and your package will be available on Package Control.

If you need to update your package, push another tag to your package's repo to create a new [release](https://github.com/kylebebak/sublime_sort_list/releases). People searching for your package will see the latest release. 


## Fancier Packages
Update: I recently wrote [Requester](https://github.com/kylebebak/Requester), an HTTP client built on top of [Requests](http://docs.python-requests.org/en/master/). Checking out this package is a good way to learn more about ST's developer API.

If you want to get really serious, check out [GitSavvy](https://github.com/divmain/GitSavvy), one of the best packages for ST3. It's a monument to engineering, and it incorporates almost everything in the API.
