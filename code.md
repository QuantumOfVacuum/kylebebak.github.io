---
layout: page
title: Code
permalink: /code
custom_css: page
---

## Python

- __py-geohash-any__ &mdash; A minimal Python geohash package designed to use any url-safe encoding. [Here on GitHub](https://github.com/kylebebak/py-geohash-any).

- __questionnaire__ &mdash; a Python package that prompts users to answer a series of questions using a terminal GUI, and returns the answers. questionnaire makes it trivial to ask different questions based on previous answers, and it allows users to go back and answer questions again. It works with Python 2 and 3.

  The package currently has 3 core prompters that can ask __multiple choice/single option__, __multiple choice/multiple option__, and __raw input__ questions. Extending the package is as simple as writing new prompters. [Check it out here](https://github.com/kylebebak/questionnaire).


## Sublime Text

- __Requester__ &mdash; [A simple, powerful HTTP client](https://github.com/kylebebak/Requester) built on top of [Requests](http://docs.python-requests.org/en/master/). Like having Postman in your text editor.

- __SortList__ &mdash; [A cross-language plugin](https://github.com/kylebebak/sublime_sort_list) for sorting items in comma-separated lists. Handles lists without opening and closing list delimiters, and lists with trailing commas. Preserves lists' quote style (single vs. double).

- __auto-save__ &mdash; [A plugin](https://github.com/jamesfzhang/auto-save) that automatically saves the current file after every modification. Not mine, but I wrote decent chunk of the API.


## Ansible

- __kylebebak.tmux__ &mdash; An Ansible role for a badass `tmux` installation on Ubuntu. Installable via Ansible Galaxy. [Check it out here](https://github.com/kylebebak/ansible-tmux).


## Other

- __Notes__ &mdash; Notes for hackers. Notes provides a minimal syntax for quick access, editing capability, and search functionality to all notes under a directory of your choosing. Under your notes directory, you can organize notes into any folder structure you like.
  
  The default extension for notes is [`.md`](http://daringfireball.net/projects/markdown/). The extension is not part of notes' syntax. Notes supports tab completion and wildcard matching, which makes finding notes a cinch. Combined with a text editor and a Markdown plugin, Notes gives you the best of various worlds:

  - the __speed__ and __efficiency__ of a real text editor
  - the __semantics__ and __portability__ of a markup language
  - a __stylized editor__ with __file organization__, a la Evernotes
  
  Place your notes directory in your Dropbox or an online Git repo to get syncing, versioning, and access from everywhere. [Check it out here](https://github.com/kylebebak/notes).

- __Location History__ &mdash; Unless you've disabled location services on your phone, Google (or Apple or Microsoft) is probably [tracking your location](http://www.howtogeek.com/195647/googles-location-history-is-still-recording-your-every-move/), in Google's case once a minute and accurate to 5 or 10 meters. There used to be an API for accessing this data, but now the best you can do is download your raw location history for a range of dates as KML or JSON via Google Takeout. I did this, ran a clustering algorithm on the data to create visit, location and trip instances, and put them in a database.

  When run on about 18 months of my location data, this process turned up 4400 visits (clusters of points where I'd been stationary somewhere for more than 6 minutes) that correspond to 750 unique locations. Trips are the sequences of moving points that occur between visits. The data was a lot of fun to explore. Probed with simple queries it can answer interesting aggregate questions, like where are the top five places I spend time on Saturdays, or, over a period of 6 months, at what time on average did I leave work on each of the different weekdays.

  I built a front end for this data using the Google Maps API and some JS plugins. The data doesn't reveal anything that makes me uncomfortable, [so I made it available here](http://www.dronfelipe.com/location_history).

- __Match It__ &mdash; An Android clone of the [Spot it!](http://www.blueorangegames.com/index.php/games/spotit) card game, on Google Play Store [here](https://play.google.com/store/apps/details?id=bebak.kyle.tap_it).

- __Tortas__ &mdash; Pon tu propio changarro de tortas. Genera un [menú](http://www.dronfelipe.com/tortas) digno de los mejores puestos: sumamente variado, internacional y sin sentido alguno.
