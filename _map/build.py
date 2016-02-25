import os
import frontmatter
from collections import OrderedDict
import datetime

def parse_filename(filename, ext='.md'):
    """
    Remove and validate date prefix and extension,
    return list with [date, file].
    """
    filename, extension = os.path.splitext(filename)
    date, file = filename[:10], filename[11:]

    if extension == ext:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date prefix, format is YYYY-MM-DD")
        return [date, file]
    return [None, None]


def parse_base_cats(cat, sep='/'):
    cats = cat.split(sep)
    return [sep.join(cats[:i]) for i in range(1, len(cats))]


def map(root='.'):
    # path is relative to execution directory, not to location of script
    os.chdir(root)

    site_map = OrderedDict() # cat -> [files]
    num_files = 0
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for filename in filenames:
            date, file = parse_filename(filename)
            if not date or not file:
                continue
            num_files += 1
            # extract title and categories from frontmatter
            with open('{}/{}'.format(dirpath, filename), 'r') as f:
                fm = frontmatter.loads(f.read())
                title, cat = fm['title'], fm['categories'].replace(' ', '/')
                file = {'date': date, 'file': file, 'title': title}
                for base_cat in parse_base_cats(cat):
                    if not base_cat in site_map:
                        site_map[base_cat] = []
                if cat in site_map:
                    site_map[cat].append(file)
                else:
                    site_map[cat] = [file]

    # generate markdown from categories dict
    categories, links = [], [] # lists that will later be joined into strings
    indent, h, h_sub = ' '*4, '##', '####'

    for cat, files in site_map.items():
        cats = cat.split('/')
        level = len(cats)-1

        # for github in-page header anchors, '/' -> '' and ' ' -> '-'
        count = '<sup>({})</sup>'.format(len(files)) if len(files) else ''
        categories.append('{}* [{}](#{}) {}\n'
            .format( indent*level, cats[-1], cat.replace('/', '--'), count ))
        header = h_sub if level > 0 else h
        # with sub-directory headers, pad '/' with spaces for readability
        links.append('\n{} {}\n'.format( header, cat.replace('/', ' / ')) )

        files.sort(key=lambda x:x['date'])
        for f in reversed(files):  # files in each cat in reverse date order
            links.append('* [{}]({}/{}) <sup>{}</sup>\n'
                .format(f['title'], cat, f['file'], f['date']))

    return({
        'count': num_files,
        'categories': ''.join(categories),
        'links': ''.join(links)
    })
