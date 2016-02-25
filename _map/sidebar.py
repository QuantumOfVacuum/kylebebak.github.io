import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
site_map = build.map(root, sidebar=True)

print(site_map['categories'])
