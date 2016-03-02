import click
import build

@click.command()
@click.option('--posts_dir', default='.', help='Path to posts directory')
@click.option('--categories_file', default='.', help='Output categories file')
def categories(posts_dir, categories_file):
    cats_dict = build.categories(posts_dir)
    # generate markdown from categories dict
    categories, links = [], [] # lists that will later be joined into strings
    indent, h, h_sub = ' '*4, '###', '####'

    for cat, files in cats_dict.items():
        cats = cat.split('/')
        level = len(cats)-1

        # for github in-page header anchors, '/' -> '' and ' ' -> '-'
        count = '<sup>({})</sup>'.format(len(files)) if len(files) else ''
        category = '{}* [{}](#{}) {}\n'.format(
            indent*level, cats[-1], cat.replace('/', '--'), count)

        categories.append(category)
        header = h_sub if level > 0 else h
        # with sub-directory headers, pad '/' with spaces for readability
        links.append('\n{} {}\n'.format( header, cat.replace('/', ' / ')) )

        files.sort(key=lambda x:x['date'])
        for f in reversed(files):  # files in each cat in reverse date order
            links.append('* [{}](../post/{}) <sup>{}</sup>\n'
                .format(f['title'], f['file'], f['date']))


    categories_template = \
    '<section id="categories" markdown="1">\n{}\n</section>' + \
    '\n---\n' + \
    '<section id="links" markdown="1">\n{}\n</section>'

    with open(categories_file, 'w') as f:
        f.write(categories_template.format(
            ''.join(categories), ''.join(links)) )


if __name__ == '__main__':
    categories()
