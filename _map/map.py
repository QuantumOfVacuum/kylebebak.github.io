import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
site_map = build.map(root)

fm ='---\n\
layout: page\n\
permalink: /cats\n\
custom_css: cats\n\
---\n'

print('{}\n__{}__ and counting...\n\n---\n\n## Categories\n\n{}\n---\n{}'
    .format(fm, site_map['count'], site_map['categories'], site_map['links']))

