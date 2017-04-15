---
layout: post
comments: true
title: "Cookies and CSRF: How Web Browsers Take the Worse is Better Approach to Security"
categories: code security
tags: [security, web, sop, cors, cookies, csrf]
---

## The Browser makes writing web apps easy

You have 

https://www.jwz.org/doc/worse-is-better.html

http://programmers.stackexchange.com/questions/216605/how-do-web-servers-enforce-the-same-origin-policy


>The same origin policy is a wholly client-based restriction, and is primarily engineered to protect users, not services.

>You're asking for a server-side mechanism to distinguish between requests made by my program (which can send anything) and requests made by a browser that has a page loaded from a permitted origin. It simply can't be done


>The same-origin policy was invented because it prevents code from one website from accessing credential-restricted content on another site.

vulnerabilities are required by web standards
less secure and more adoption, or secure and obscure


http://security.stackexchange.com/questions/97825/is-cors-helping-in-anyway-against-cross-site-forgery


>All the SOP does is prevent the response from being read by another domain (aka origin). This is irrelevant to whether a CSRF attack is successful or not.


>All CORS does is relax the SOP when it is active. It does not increase security, it simply allows some exceptions to take place.


>So if you have http://data.example.org you can set response headers to allow http://site.example.com to make AJAX requests and retrieve data from your API.


## What does it protect against?

### EVERYTHING
Without SOP, evil.com has JS that makes a GET request against `bank.com/account_info`. Cookies are sent automatically, including the auth cookie for `bank.com`. `bank.com` obliges, returns the contents of `bank.com/account_info`, evil.com reads the contents, game over

So, SOP will allow the browser to make the request, but it won't allow it to READ the response.

Relation to CSRF: without SOP, JS from siteB makes AJAX GET request against a page on siteA, which has form with embedded CSRF token in hidden form field. siteB can read response, parse DOM tree, find token, and then make a POST request against siteB with token inserted in body. Voila, CSRF protection implemented by siteA is broken.


## It's only necessary in the browser
The browser is promiscuous, it visits lots of sites. When people wanted to make sites more interesting, they introduced JS, and now many of these sites are really applications. Without SOP, all of these applications could read each other's data and modify each other's state!

In mobile, it's not necessary, because you don't run multiple applications that share the same context/environment.

For example, [AsyncStorage](https://facebook.github.io/react-native/docs/asyncstorage.html) in React Native is global to the application, but it's not shared between applications. Mobile apps are sandboxed, while web apps aren't, because they all run in the same context (your browser).


This is why cookies were implemented in browsers in 1995. Without cookies or other browser storage APIs, maintaining state across requests, for example to keep a user logged in, was difficult and prone to error. You might keep connections open for as long as you wanted sessions to be active, wasting a bunch of memory on your server, or you might try putting the session id in the query string, which is [insecure for many reasons](https://security.stackexchange.com/questions/14093/why-is-passing-the-session-id-as-url-parameter-insecure).

With mobile apps, you have access to all of the OS APIs, as opposed to only the APIs exposed by the browser. OS APIs include those for persisting things, which means cookies are uneccessary -- you can persist a session token on the device and add it to request headers of every request.



To see why cookies are useful, imagine a site that does sessions without cookies, now that the [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) is implemented by most browsers. The app could use JS to persist a session id to local storage, then read it back and pass it to the server with every request.

But unless your site is an SPA, this is much easier said than done. What happens if a user clicks on a link to go to a different page? His browser doesn't know about your custom auth protocol, and it's not going to pass the session id with the request. You would need JS to run on every page in your site to do that for him.



In a mobile app, this is essentially what you do, but it's easy, because developers have control over everything that happens when a user navigates from one screen to another, including the requests that are made. In a web app, unless you hack the browser's behavior with JS, clicking a link makes the browser issue a plain GET request to the URL.

So, to recap, cookies allow you to persist  this is why cookies exist.
