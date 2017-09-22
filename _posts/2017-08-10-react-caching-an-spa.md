---
layout: post
comments: true
title: "Caching a React SPA"
categories: code react
tags: [software-design react spa caching]
---

React SPAs weigh a lot, because the JS weighs a lot. The initial request returns a minimal HTML skeleton that points to the JS bundle with the actual application. If you don't tell the client to cache this it has to pull in megabytes of JS every time it loads your app.

The hard problem with caching is cache invalidation. When you ship out a new version of your JS, how do you make sure clients get it right away?

__Tell the client not to cache the HTML skeleton at all__. This thing weighs a few kB, so it costs nothing to send it to the client. This means every time the HTML changes, the client gets the changes right away.

__Tell the client to cache the JS forever.__ Every time you deploy your app, change the name of the JS bundle, and have your HTML skeleton point to the new name.

Voilà! Clients get up-to-date JS for your app every time you ship, but never download any version more than once.

I thought this was a clever way to take advantage of disparity in size between HTML and JS code in modern SPAs.


