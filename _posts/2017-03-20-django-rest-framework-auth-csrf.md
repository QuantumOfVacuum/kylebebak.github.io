---
layout: post
comments: true
title: "Authentication and CSRF Protection in Django Rest Framework"
categories: code security
tags: [security, web, csrf, django, django-rest-framework]
---

This is a brief explanation of how authentication is handled in DRF, and how it incorporates CSRF protection.


## Default Behavior

If `authentication_classes` isn't defined for a view, or it's an empty list, `SessionAuthentication` is run by default. `SessionAuthentication` is Django's default auth backend -- it's the one that checks the __session_id__ cookie.

If the user isn't logged in, no CSRF token is needed, because the auth method returns before enforcing the CSRF check. However, if the client __is logged in with a session cookie__, the rest of the auth method runs and raises a `PermissionDenied` exception if the CSRF check fails.


## Why CSRF Protection?

This can come as a surprise (it certainly did for me). Why does this make sense as default behavior, i.e. why is it a good idea to perform a CSRF check for requests that authenticate via a session cookie, but not for requests made by unauthenticated users?

CSRF is also known as __session-riding__, and is specifically caused by storing the __session_id__ in a cookie, which is automatically sent if the __cookie's URL__ matches the __origin__ of the __request URL__. Because of this, any service that authenticates users with a session cookie [must protect against CSRF](/post/csrf-protection).

Now it's true that unauthenticated requests are also vulnerable to CSRF, but usually your API doesn't expose unsecured endpoints that respond to "unsafe" methods (`POST`, `PUT`, `PATCH`, `DELETE`). So, DRF doesn't prevent CSRF for unauthenticated requests.


## How does SessionAuthentication work?

Clients will interact with your API via AJAX requests. For AJAX requests, in DRF as in Django, the CSRF cookie is compared with the value of the token passed in the custom `X-CSRFToken` request header. In other words, if you want to hit your API with a web client that authenticates with a session cookie, you'll always need to read the value of the CSRF cookie and add it as a request header.


## Alternatives to SessionAuthentication

[TokenAuthentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication). This requires clients to pass a token in the `Authorization` header of each request. __This is the kind of authentication you should use for most client-server setups__, like a mobile app or desktop app consuming your API.

This kind of auth doesn't require CSRF protection. The token isn't stored in a cookie, so it doesn't get sent automatically by your browser, which means it can't cause CSRF vulnerabilities.


## When should I use SessionAuthentication?

The only circumstance where using `SessionAuthentication` in DRF makes sense is for _"AJAX requests that are made within the same context as the API they are interacting with"_, i.e. if you've got a web app with endpoints that live in the same domain as your API endpoints. In this case, a user logs in, the web app tells their browser to set a session cookie and a CSRF cookie, and these get passed along every time your web app makes a request against your API.

Even in this special case, compared with `TokenAuthentication`, this doesn't really save you any work. The client has to add a header to every request it makes...

- `SessionAuthentication`: CSRF token in `X-CSRFToken` header
- `TokenAuthentication`: auth token in `Authorization` header
