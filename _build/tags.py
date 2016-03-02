import sys, os, random

import build

path = os.path.dirname(os.path.abspath(__file__))

root = sys.argv[1] if len(sys.argv) > 1 else '.'
tags_dict = build.tags(root)



r_weak = lambda: random.randint(0, 95)
r_strong = lambda: random.randint(64, 191)
r = [r_strong, r_weak, r_weak]

tags = []
for tag, items in tags_dict.items():
    colors = [c() for c in sorted(r, key=lambda k: random.random())]
    color = '#%02X%02X%02X' % tuple(colors)
    size = pow(len(items), .4)
    style = 'style="background-color:{};font-size:{}em;"'.format(color, size)

    tags.append('<a href="/tag/{}">'.format(tag))
    tags.append('<span class="resizing-tag" {}>{}</span>'.format(style, tag))
    tags.append('</a>')

with open('{}/../_includes/tags.html'.format(path), 'w') as f:
    f.write(''.join(tags))



# front matter for all files in tags/
fm ='---\n\
layout: tag\n\
tag: {}\n\
permalink: /tag/{}/\n\
custom_css: tag\n\
---'

tags_dir = '{}/../tags'.format(path)
for tag, items in tags_dict.items():
    with open('{}/{}.md'.format(tags_dir, tag), 'w') as f:
        f.write(fm.format(tag, tag))

