---
layout: post
title: "Good enough security, backup, encryption"
categories: code random
---

My security and backup, for anyone that wants to hack me, consists of the following:

- After 5 minutes, my computer is locked and requires a ~10 char password to open. Not uncrackable, but it doesn't have to be, because there's nothing sensitive and unencrypted inside.
- My bank numbers and government ID numbers are all in an encrypted [Vecacrypt](https://veracrypt.codeplex.com/) file. This file is encrypted with a ~30 char password and is currently uncrackable in theory.
- This encrypted file is under my Dropbox.
- All of my online logins are stored in [LastPass](https://lastpass.com/), with the same password as the one I use to encrypt the Veracrypt file. LastPass logs me out automatically if I'm idle for 10 minutes, of if I close the browser.

The most plausible attack vector is probably snooping on my connection to steal my password when I send it to LastPass to authenticate. But LastPass uses https. Either that or putting a gun to my head and asking me for the password.

I think of online security as sort of analogous to home security: a breakin is always possible, but if you're better protected than your neighbor it's a lot less likely.
