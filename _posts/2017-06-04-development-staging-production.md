---
layout: post
comments: true
title: "3 Environments: Development, Staging, and Production"
categories: code random
tags: [software-design]
---

Why is this pattern so common? Why do new coders hear about it long before they know what it means? 

This is one of those beautiful questions of constraints and degrees of freedom. For example: __Why are the laws of electromagnetic and gravitational attraction inverse square laws?__

__Hint__: what would those laws be like if the universe had 2 or 4 spatial dimensions instead of 3?

If someone sees this question and knows the answer they're probably a good engineer.


## Constraints
At a high level, there are just two constraints with code.

### 1. People Create It
This requires an environment that's optimized for __developers__. Devs want an environment with a tight feedback loop, where the delay between changing code and seeing the effects is short; they want an environment that __exposes__ the code that powers it. They want an environment over which they have control, which means it runs on their machines, and as few other machines as possible. We'll call this environment __development__.

### 2. People Use It
This requires an environment that's optimized for __users__. It could be __development__, but optimizing for developers __and__ users doesn't work. Users want a robust environment backed by as many machines as needed to accommodate them and another million users, and that __hides__ the code that powers it. We'll call this environment __production__.

Finally, users want a production environment __that doesn't break__. But with only two environments this isn't possible. Because dev and prod are necessarily different, devs can't be sure code that works in dev will work in prod. It has to be tested first. This is done in an environment that's as similar as possible to production (but cheaper to maintain). This one is called __staging__.

---

Analysis of constraints gives insights into all kinds of questions. For example, in popular implementations of nearly all languages, why is source code compiled to bytecode before being interpreted by a VM? [Very good answer here](https://softwareengineering.stackexchange.com/questions/289429/why-does-python-need-both-a-compiler-and-an-interpreter?newreg=5d73d13956fa4b418c39362d1446e2af)...
