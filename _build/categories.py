import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
categories = build.categories(root)

fm ='---\n\
layout: page\n\
permalink: /categories\n\
custom_css: categories\n\
---'

print(
'{}\n\
<h1>Categories</h1>\n\n\
{}\n\
__{}__ and counting...\n\n---\n\
{}'
.format(fm, categories['categories'], categories['count'], categories['links']))
