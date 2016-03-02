import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
categories = build.categories(root)


categories_template = \
'{}\n\
__{}__ and counting...\n\n---\n\
{}'

with open('{}/../_includes/categories.md'.format(path), 'w') as f:
    f.write(categories_template.format(
        categories['categories'], categories['count'], categories['links']) )
