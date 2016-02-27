---
layout: post
title: "Screencasts and GIFs with free OSX software"
categories: code mac
---

## OSX for screencasts
The easiest, freest way is to use QuickTime Player, which comes pre-installed. Go to __File > New Screen Recording__ or press <kbd>ctrl</kbd>+<kbd>⌘</kbd>+<kbd>N</kbd>. The __Screen Recording__ window pops up. There are options to choose your microphone, and "Show Mouse Clicks in Recording", which is useful if you're doing a tutorial.

You can select a region of the screen or record all of it. To stop recording, you click on the recording icon that appears in the OSX menu bar. QuickTime will open the video you just recorded, which you can either discard or save as a `.mov`. If you want to trim junk off the beginning or end of the recording, hit <kbd>⌘</kbd>+<kbd>T</kbd>.

## Screencasts to GIFs
For converting your `.mov` to a GIF, e.g. for displaying it in a Github repo, you can follow [this tutorial](https://gist.github.com/dergachev/4627207), written by Alex Dergachev. It will advise you to `brew install ffmpeg` and `brew install gifsicle`, and run something like the following command: `ffmpeg -i <in>.mov -pix_fmt rgb24 -r 10 -f gif - | gifsicle --optimize=3 --delay=3 > out.gif`. The `-r` flag is for the frame rate.

Alternatively, you can download a [Ruby CL tool](https://github.com/dergachev/screengif) also written by Alex, with `gem install screengif`, and then run `screengif --input <in>.mov -r 10 --output out.gif`. The syntax for __screengif__ is simpler. According to Alex it's a wrapper for the piped commands above, but for some reason it runs a lot slower on my machine.

