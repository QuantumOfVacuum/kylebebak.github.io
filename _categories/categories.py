import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
categories = build.build(root)

fm ='---\n\
layout: page\n\
permalink: /categories\n\
custom_css: categories\n\
---\n'

print('{}\n__{}__ and counting...\n\n---\n\n## Categories\n\n{}\n---\n{}'
    .format(fm, categories['count'], categories['categories'], categories['links']))

