---
layout: post
comments: true
title: "How CSRF Protection Works"
categories: code security
tags: [security, web, csrf, django]
---

## What is CSRF?

Cross-site request forgery is when you visit `evil.com`, and `evil.com` makes a request against `A.com` without your knowledge. It's trivial for `evil.com` to do this: it just includes some JS in the page that makes a request against `A.com`. If you're logged in to `A.com` when the request gets made, bad things can happen if `A.com` doesn't have CSRF protection.

Also known as __session riding__, CSRF takes advantage of the fact that your browser passes along __A__'s cookies in the request to `A.com`, regardless of where the request originated. If __A__'s request validation consists only of checking the session cookie to see if you're logged in, it will treat the request from __evil__ as valid!

So if __evil__ executes an "unsafe" request against __A__, for example to post something to your profile, or send a message to your friend, __A__ will oblige. CSRF protection is a reliable method to ensure the request __really__ did originate with `A.com`, preventing any evil site from making unsafe requests against __A__.


## How to protect against CSRF?

There are explanations of varying quality out there. Many gloss over the details and seem to imply that setting a special cookie on the browser and having the browser submit the cookie with requests is sufficient. But this is exactly how sessions work, [and sessions don't prevent CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)#Prevention_measures_that_do_NOT_work); they enable it!

The posts that finally helped me get it were [this](http://security.stackexchange.com/questions/47198/is-djangos-built-in-csrf-protection-enough) and [this](https://cloudunder.io/blog/csrf-token/).


### Double-Submit Cookie

Basically, there are are two patterns for stopping CSRF attacks: __Double-Submit Cookie__ and __Synchronizer Token__. Since I'm a Python fan, I'll start with the one used by Django, __Double-Submit Cookie__.

It works like this. If a view is protected against CSRF, when the view responds to any petition whose request method is "unsafe", e.g. `POST`, `PUT`, and `DELETE`, it requires a `csrfmiddlewaretoken` to be passed in the request payload. It checks the value of this token against the `csrftoken`, a cookie which is also passed along with the request. If they don't have the same value, the request is rejected.

The key here is that the browser passes two tokens in the request __which must have the same value__. The `csrfmiddlewaretoken`, in the request body, and the `csrftoken` in the cookie. Imagine Django renders a page with a form for posting a tweet. To ensure the `csrfmiddlewaretoken` is included in the POST request when the form is submitted, Django renders the page with the token embedded in the form as a hidden input.

~~~html
<form action="https://tweeter.com/tweet" method="POST">
  <input type="hidden" name="csrfmiddlewaretoken" value="nc98P987bcpncYhoadjoiydc9ajDlcn">
  <input type="text" name="tweet">
  <input type="submit">
</form>
~~~

When you log in, Django resets the `csrftoken` cookie on your browser to some big unguessable string, and for the remainder of your session it renders forms with this token in a hidden input. The token is unique per user and per session.

An evil site using JS to POST some tweet on your behalf can set any `csrfmiddlewaretoken` in the request payload, but it has no way of making this match with the `csrftoken` cookie that is also passed along with the request. Django compares the two and rejects the request.


### Synchronizer Token

This pattern is like the first one, except that no cookie is used. Instead, the server checks the __hidden_input_csrftoken__ passed in the request payload against a __session_csrftoken__ that it stores along with your session_id when you log in.

The only difference is that the __session_csrftoken__ is stored in a database record, by the server, instead of in a cookie, by the browser. It's no more difficult to implement. But it is a little more secure.

Because it relies on a DB record instead of a cookie, it's not vulnerable to cookie forcing. While it shouldn't be possible for one site to edit cookies set by another site, there are attacks, like XSS, that break this assumption. That said, as mentioned in one of the posts I link to, if a site is vulnerable to XSS then CSRF is probably the least of its worries.
