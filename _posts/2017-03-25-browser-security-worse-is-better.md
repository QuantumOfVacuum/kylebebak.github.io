---
layout: post
comments: true
title: "Web Browsers Take the Worse is Better Approach to Security"
categories: code security
tags: [security, web, sop, cors, cookies, csrf, xss]
---

## Worse Is Better
Check out [this essay](https://www.dreamsongs.com/RiseOfWorseIsBetter.html). What Jeff Atwood calls the money shot:

>However, I believe that worse-is-better, even in its strawman form, has better survival characteristics than the-right-thing, and that the New Jersey approach when used for software is a better approach than the MIT approach.

What exactly is meant by __worse-is-better__ and __the-right-thing__ is [open to discussion](http://yosefk.com/blog/what-worse-is-better-vs-the-right-thing-is-really-about.html), but the essence is that reproductive fitness is a good criteria for selecting a design philosophy.

I think the people who implemented security in web browsers knew about this criteria, and they decided __worse-is-better__ was indeed better.


## JS and SOP
The web wasn't envisioned as a platform for applications. But when graphical web browsers appeared, people realized that the web could offer immersive, dynamic experiences. Netscape founder Marc Andreesen proposed a "glue language" that could be written into HTML and interpreted by the browser as necessary to realizing this vision. The result was JavaScript.

"Magic" cookies were introduced a year before JavaScript, to add state to the stateless HTTP protocol. In HTTP, each request-response cycle stands on its own. When the cycle finishes the connection is terminated, and neither the client nor the server is required to remember anything about it. 

So under HTTP as originally conceived, there's no way for a server to know if a string of requests are coming from the same client. In other words, no sessions. Cookies overcome this in a simple way. The server can tell the client to create a cookie with the `Set-Cookie` response header, and the browser complies. The cookie knows the `domain` for which it was set, and the browser sends it along with any request to that domain. The server can check the session cookie bundled with the request and associate the request with a user.

JS allows clients to manipulate cookies and read their values. But this raises an obvious security issue: what happens if you log in to `bank`, then you go to `A`, and JS running on `A` reads `bank`'s session cookie? Even without AJAX requests, it would be trivial for `A` to save your session cookie on its server, and boom, your session just got hijacked.

This sort of scenario motivated the __same-origin policy__. The SOP is implemented __by browsers__. It protects users by not allowing a script running on `A` to read content from any other domain, which includes cookies set by another domain.


### iframe
The SOP also ensures the `iframe` element can't be abused to read content from another domain. Without the SOP, if `A` has an iframe that embeds content from `bank`, and you're logged in to `bank`, JS running on `A` could just parse the DOM embedded in the iframe and read your account information.

The SOP means that the even though your browser renders `bank`'s content within `A`, the browser won't let JS see anything in the iframe. Even methods such as [getImageData](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData), which extracts the color of each pixel in a rectangular region of a canvas, have to be disabled if any images in the current window were loaded from a different domain.

Note: as a developer, you can control whether other sites can load your site in an iframe by using the [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) response header.


### AJAX
Eventually Microsoft gave JS the ability to perform asynchronous HTTP requests. The SOP comes into play here in much the same way it does with the iframe. Imagine you visit `A`. Unbeknownst to you, some JS running on `A` sends a GET request to `bank` and reads your account info in the response. Then it immediately POSTs your account info to some endpoint controlled by `A`.

Because JS APIs keep expanding to keep pace with demands for fancier web apps, enforcing the SOP requires constant vigilance. [There are lots of subtleties](https://blogs.msdn.microsoft.com/ieinternals/2009/08/28/same-origin-policy-part-1-no-peeking/).


## CORS
So, what happens if your API runs on `api.com` and your site is on `site.com`? You want users visiting your site to be able to consume your API, but the SOP prevents `site` from reading API responses.

You can use the [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin) response header to tell browsers that JS running on `site` has access to your API's resources, even though they come from a different domain. In other words, you can use this header to override the SOP if it's getting in your way.


## XSS
How can an attacker get around the SOP? Let's say he wants to read your account info from `bank`. Because of the SOP, using JS to do this won't work, __unless the JS is running on bank.com__.

If the attacker can get `bank` to run some malicious JS on its page, the SOP is bypassed. Getting `bank` to run this JS is what cross-site scripting is all about. This might be done, for example, by taking advantage of an insecure public comments section. Imagine comments are saved to a DB, and rendered in a list when the page is loaded.

If the comments aren't validated or encoded, they could contain <script>...</script> tags filled with malicious JS that gets executed by the browser for any visitor that loads the page. Maybe this JS reads the visitor's account info and POSTs it via AJAX to an endpoint the attacker controls.

[XSS vulnerabilities are very dangerous and very common](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)). Here's a [decidedly innovative example](/post/self-inflicted-xss).


## CSRF
One thing the SOP doesn't prevent is cross-site request forgery. This is because browsers don't stop JS running on one domain from making a request against another domain, they only prevent reading of the response.

It's perfectly kosher for JS running on `A` to hit `bank` with a POST request, even if this request might have unpleasant side effects for a user of `bank`. Because `bank`s cookies get sent along with the request, if a user is logged into `bank`, `bank` will treat the request as though it came from a logged in user.

Every site that uses session cookies is vulnerable to CSRF. This means the vast majority of web apps. [Preventing it](/post/csrf-protection) is not trivial, especially if you're not using a framework.

The obvious way to avoid this mess would have been "same-site" cookies, that only get sent to the same domain that set them. These wouldn't work as tracking cookies, but they would be just fine for most session cookies. Strangely, no such cookie existed until Google introduced the `SameSite` cookie in 2016, in Chrome 51. Few sites use `SameSite` cookies, even if "cross-domain" cookies are unnecessary, because the latter variety was the only option for more than 20 years. This gives you an idea of how browser vendors approach security.


## Insecure by Design
Your data would be safer if JS didn't have so many privileges, but web apps would be less interactive, ads would be less relevant, Facebook and Google wouldn't know every last thing about you...

In other words, [it works this way for a reason](https://www.owasp.org/images/9/90/Web_Security_Fundamentally_Broken.pdf).

>vulnerabilities are required by web standards... less secure and more adoption, or secure and obscure...

The market is right, evolution is right, worse-is-better is better.


## This a only problem in the browser
The browser is promiscuous, it visits lots of sites. Many of these sites are really applications, which means you have a bunch of __applications that share an environment (your browser)__. They're sandboxed from your OS, but not from each other.

With mobile apps this isn't an issue.

For example, [AsyncStorage](https://facebook.github.io/react-native/docs/asyncstorage.html) in React Native is global to the application, but it's not shared between applications. 


## Cookies illustrate the big difference between mobile apps and web apps
Without cookies, maintaining state across requests in web apps is difficult and prone to error.

With mobile apps, you have access to the OS APIs, as opposed to only those exposed by the browser. The OS lets you persist things, which means cookies are unnecessary -- you can persist a session token on the device and add it to request headers of every request.

Now that the [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) is implemented by most browsers, you might wonder if it could replace cookies. Imagine sessions. After login, the client could write the session id to local storage, then read it back and pass it to the server with every request.

But unless your site is an SPA, this is much easier said than done. What happens if a user clicks on a link to go to a different page? His browser doesn't know about your custom auth protocol, and it's not going to pass the session id with the request. You would need JS to run on every page in your site to do that for him.

In a mobile app, this is essentially what you do, but it's easy, because developers have control over everything that happens when a user navigates from one screen to another, including the requests that are made. In a web app, unless you use JS to hack the browser's behavior, clicking a link always has the same effect:
  - the browser issues a plain GET request to the URL in the href attribute
  - the browser renders a new page with the response content

Security is easier with mobile apps because each app is sandboxed, and developers have total control over the request-response cycle. This makes mobile apps easier to build than web apps, at least in my experience. But web offers a richness and ease of connectivity that mobile can only dream of, which is why it will continue to be the world's premier application platform for the foreseeable future.
