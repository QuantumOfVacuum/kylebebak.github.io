---
layout: post
title: "My Short-Lived Plan to Write a Grammar-Checking Plugin for Sublime Text"
categories: code random
tags: [sublime-text, grammar, linting]
---

Now that I do all my writing with my text editor, I decided to write an ST plugin to check English grammar. I figured it would be fairly straightforward:

- find a good open source command line __grammar checker__
- if grammar checking is `on` for the current view, on each modification of the view queue up a debounced `grammar-check` request and delegate it to the __grammar checker__
- retrieve the results and display them in the view

This is basically how SublimeLinter works. I figured it would be a good learning experience that would involve a few hundred lines of code. Unfortunately, I got stuck at the first step.


## What's Currently Available

A short but sadly thorough investigation left me incredulous &mdash; it turns out there is just ___one___ open source grammar checker, [LanguageTool](https://languagetool.org/), which announces on its front page that English support is incomplete, and v3.2 is an 88MB `.jar` that requires Java 8 to run!

I realized grammar checking is more complicated than I thought. LanguageTool is built to support 20 languages, which is nice, but because English online beats its closest competitors for prevalence [by an order of magnitude](https://en.wikipedia.org/wiki/Languages_used_on_the_Internet#Content_languages_for_websites), building a lightweight English grammar checker should be a top priority. If I wasn't working I'd learn how to do it and start one myself...


## On Building a Minimalist Grammar Checker

For those that would undertake this endeavor, I think that [minimalism](./thoreau-original-minimalist) should be the guiding principle, with flexibility a distant second.

I want a grammar checker that looks for basic errors and makes no assumptions about "style". If you want your computer telling you ___how___ to write you're a terrible writer, and a grammar checker isn't going to help. UPenn's entertaining Language Log goes into this idea [more in depth](http://itre.cis.upenn.edu/~myl/languagelog/archives/005061.html):

>[Grammar checkers] can't really even help with standard nonsense like discouraging the use of passives (see this page for a listing of Language Log posts on the passive), because they are basically hopeless at identifying passive clauses — even more hopeless than college-educated American adults, which is not setting the bar very high. They mostly can't help with subject-verb agreement errors because they are unable to spot which noun the verb should be agreeing with. And they cannot warn you off singular antecedents for they, because they can't figure out which antecedent a given pronoun has. __The things they are good at, like spotting the occasional the the typing error, are very easy [and] there are very few of them.__ For the most part, accepting the advice of a computer grammar checker on your prose will make it much worse, sometimes hilariously incoherent. If you want an amusing way to whil[e] away a rainy afternoon, take a piece of literary prose you consider sublimely masterful and run the Microsoft Word™ grammar checker on it, accepting all the suggested changes.


Apparently, grammar checking is still a job left best to humans. This post is pretty negative, but these guys are linguists, and dismissing what they say out of hand probably isn't a good idea. I can only imagine the thousands, or millions of man hours that went into writing Word's grammar checker, a tool that mutilates sentences much more often than not.

So, what should a grammar checker be concerned with? Precisely those __obvious errors__ it can diagnose easily, but that nonetheless slip past human editing. Competent writers publish work with basic grammatical errors all the time, not because they're stupid, but because catching all the errors all the time is impossible. __The paragraph I quoted above has two of them.__ This, as I see it, is where grammar checkers come in.

A grammar checker limiting itself to this class of mistakes would be lightweight and easy to write, and would be just as valuable, and much less annoying, than a more complex beast with notions of "style". A more ambitious project might involve writing a configurable grammar checker, a la [ESLint](./eslint), that could enforce additional user-defined rules read from a config file.
