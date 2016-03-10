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
        except Exception:
            raise ValueError("The date prefix for {} is INVALID".format(filename)) from None

        return [date, file]
    return [None, None]


def parse_base_cats(cat, sep='/'):
    """Helper function to ensure empty parent categories are
    included, and in correct hierarchical order."""
    cats = cat.split(sep)
    return [sep.join(cats[:i]) for i in range(1, len(cats))]


def traverse_posts(root):
    """
    Returns generator that returns all posts within root and
    its subdirectories. Root is relative to directory from
    which build.py is executed.
    """
    for (dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            date, file = parse_filename(filename)
            if not date or not file:
                continue
            yield tuple([dirpath, filename, file, date])


def tags(root='.'):
    """Build and return tag -> [files] dict."""
    tags_dict = dict()
    for dirpath, filename, file, date in traverse_posts(root):
        # extract tags from frontmatter
        with open('{}/{}'.format(dirpath, filename), 'r') as f:
            fm = frontmatter.loads(f.read())
            for tag in fm['tags']:
                if tag in tags_dict:
                    tags_dict[tag].append(file)
                else:
                    tags_dict[tag] = [file]

    return OrderedDict(reversed(sorted(tags_dict.items(), key=lambda x: len(x[1]))))


def categories(root='.'):
    """Build and return cat -> [files] dict."""
    cats_dict = dict()
    for dirpath, filename, file, date in traverse_posts(root):
        # extract title and categories from frontmatter
        with open('{}/{}'.format(dirpath, filename), 'r') as f:
            fm = frontmatter.loads(f.read())
            title, cat = fm['title'], fm['categories'].replace(' ', '/')
            file = {'date': date, 'file': file, 'title': title}
            for base_cat in parse_base_cats(cat):
                if not base_cat in cats_dict:
                    cats_dict[base_cat] = []
            if cat in cats_dict:
                cats_dict[cat].append(file)
            else:
                cats_dict[cat] = [file]

    return OrderedDict(sorted(cats_dict.items(), key=lambda x: x[0]))
