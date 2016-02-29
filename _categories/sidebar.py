import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
categories = build.build(root, sidebar=True)

print(categories['categories'])

