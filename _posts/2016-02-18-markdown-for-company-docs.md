---
layout: post
comments: true
title: "GitHub and Markdown for Company Documents"
categories: code git
tags: [github, markdown, ms-word]
---

Companies with any technical chops should use online code repositories filled with HTML or something that compiles to HTML for nearly all of their documents.

Most tech companies write their intra-company documents, such as code documentation, in Markdown, and store them on a cloud repo like GitHub. This provides a single point of access, versioning, and shared editing, and it's online by definition. More non-tech companies should do the same, because it's not difficult and the benefits are huge.

The first tech job I had was working at an IT consulting company in Mexico. They were addicted to MS Word and MS Outlook. When I arrived HR sent me a series of emails with URLs and usernames and passwords for Jira, Trello, Google Docs; attached documents with the company calendar, the sick leave and vacation policy; forms that I was to fill out with my contact info and personal bio and return to sender. There was plenty of info they forgot or didn't think to send that I obtained later by asking around. After all, the emails were coming from lots of different people, and coordinating to make sure they didn't miss anything can't have been easy.

Later, when I started using Git and then GitHub, I realized how clumsy the onboarding process had been. What if HR had just sent me a link to a private GitHub repo with stuff like this:

- all the WiFi networks and passwords
- instructions on how to use the printers
- names and contact info for everyone, including tech support (teach a man to fish...)
- information about company healthcare, benefits, stocks
- information about vacation policy, and a company calendar
- links to forms for inputting employee contact info
- links to forms for annual evaluations
- links to project logging tools, and instructions on how to use them

One email instead of 10, no missing or outdated information... This system would have have required no Herculean feats of coordination.


Likely they would still have preferred to stick with Word for inter-company documents, because, after all, Word is a standard in the corporate world. But using Word for this suffers from the same weaknesses as using it for docs within the company. Anyway, these days everyone accepts a business doc as a PDF. They may even prefer it this way, as it ensures it's going to look the same on their machine as it does on yours. Markdown trivially compiles to HTML, which can be trivially exported to PDF. I imagine company-wide HTML or Markdown templates and stylesheets in the central repo, and collaboratively edited docs in individual project repos. We would have been able to send our clients docs that actually looked consistent and professional...
