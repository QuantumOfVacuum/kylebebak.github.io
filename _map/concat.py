import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
site_map = build.map(root)

print('---\n\
layout: page\n\
permalink: /site-map\n\
---\n\
' + site_map['count'] + site_map['cats'] + site_map['links'])
