import sys, os

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
tags = build.tags(root)

fm ='---\n\
layout: tag\n\
tag: {}\n\
permalink: /tag/{}/\n\
custom_css: tag\n\
---'


tags_dir = '{}/../tags'.format(path)
for tag, items in tags.items():
    with open('{}/{}.md'.format(tags_dir, tag), 'w') as f:
        f.write(fm.format(tag, tag))
