---
layout: post
comments: true
title: "Mixing Markdown with HTML, Using kramdown"
categories: code jekyll
tags: [markdown, jekyll, kramdown, parsers]
---

The first Markdown converter was written so that HTML tags in a Markdown file are left alone by the parser. The content [inside of block-level elements](http://daringfireball.net/projects/markdown/syntax#html) is also ignored by the parser. This means that `<p>**Hello**</p>` is converted to exactly that, paragraph tags with "Hello" and some asterisks inside, not paragraph tags wrapping bold tags wrapping __Hello__.

Using [kramdown](https://github.com/gettalong/kramdown), Jekyll's default Markdown converter, you can mix HTML and Markdown. How does this work?

If you want Markdown content inside block level elements to be converted to HTML, simply add the `markdown="1"` attribute to the opening tag of the block-level element.

~~~html
<section id="categories" markdown="1">

__Markdown__ getting converted to __HTML__ inside a ___block-level element___.

A list of categories:

- foo
- bar

</section>
~~~

Here's what __kramdown__ does with this section element and its content:

---

<section id="categories" markdown="1">

__Markdown__ getting converted to __HTML__ inside a ___block-level element___.

A list of categories:

- foo
- bar

</section>
