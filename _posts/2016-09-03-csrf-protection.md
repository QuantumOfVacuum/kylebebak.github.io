---
layout: post
comments: true
title: "How CSRF protection works"
categories: code security
tags: [security, web, csrf, django]
---

## What is CSRF?

Cross-site request forgery is when malicious `siteB.com` tricks a user into making a request against `siteA.com`. Also known as __session riding__, it takes advantage of the fact that the user's browser passes along siteA's cookies in the request to `siteA.com`, regardless of where the request originated. If siteA is just looking at the session cookie to see if the user is logged, it will treat the request as valid.

The danger is when siteB executes an "unsafe" (not idempotent) request against siteA, for example to post something to the user's profile, or send a message to another user, or whatever. CSRF protection is a reliable method to ensure the request __really__ did originate with `siteA.com`, preventing siteB from getting the user to make requests against siteA.


## How to protect against CSRF?

There are explanations of varying quality out there. Many gloss over the details and seem to imply that setting a secret cookie on the browser and having the browser submit the cookie with requests is sufficient. But this is exactly how sessions work, [and sessions do nothing to prevent CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)#Prevention_measures_that_do_NOT_work).

The posts that finally helped me "get it" were [this](http://security.stackexchange.com/questions/47198/is-djangos-built-in-csrf-protection-enough) and [this](https://cloudunder.io/blog/csrf-token/).


### Double-Submit Cookie

Basically, there are are two patterns for stopping CSRF attacks: __Double-Submit Cookie__ and __Synchronizer Token__. Since I'm a Python fan, I'll start with the one used by Django, __Double-Submit Cookie__.

It works like this. If a view is protected against CSRF, when the view responds to any petition whose request method is "unsafe", e.g. `POST`, `PUT`, and `DELETE`, it requires a `csrfmiddlewaretoken` to be passed in the request payload. It checks the value of this token against the `csrftoken`, a cookie which is also passed along with the request. If they don't have the same value, the request is rejected.

The key thing to understand here is that the client is passing two tokens in the request __which must have the same value__. The `csrfmiddlewaretoken`, in the request body, and the `csrftoken` in the cookie. Imagine Django serves a page with a form for posting a tweet. To ensure the `csrfmiddlewaretoken` is passed along in the POST request when the form is submitted, Django serves the page with the token embedded in the form as a hidden input.

~~~html
<form action="https://tweeter.com/tweet" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="nc98P987bcpncYhoadjoiydc9ajDlcn">
  <input type="text" name="tweet">
  <input type="submit">
</form>
~~~

When the user logs in, Django resets the `csrftoken` cookie on his browser to some big unguessable string, and for the remainder of the user's session it serves all forms that are protected against CSRF with this token as a hidden form input. The token is unique per user and per session.

A malicious site wanting to POST some tweet on behalf of the user can include any `csrfmiddlewaretoken` in the request payload, but it has no way of making this match with the `csrftoken` cookie that will also be passed along with the request. Django will compare the two and reject the request.


### Synchronizer Token

This pattern is like the first one, except that no cookie is used. Instead, the server checks the __hidden_input_csrftoken__ passed in the request payload against a __session_csrftoken__ that it stores along with the user's session_id when the user logs in.

The only difference is that the __session_csrftoken__ is stored in a database record, by the server, instead of in a cookie, by the browser. It is no more difficult to implement. But it is a little more secure.

Because it relies on a DB record instead of a cookie, it's not vulnerable to cookie forcing. While it shouldn't be possible for one site to edit cookies set by another site, there are attacks, like XSS, that break this assumption. That said, as mentioned in one of the posts I link to, if your site is vulnerable to XSS then CSRF is probably the least of your worries.
