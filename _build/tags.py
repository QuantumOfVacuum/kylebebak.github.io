import random
import click
import build

@click.command()
@click.option('--posts_dir', default='.', help='Path to posts directory')
@click.option('--tags_dir', default='.', help='Path to output tags directory')
@click.option('--tags_file', default='.', help='Output tags file')
def tags(posts_dir, tags_dir, tags_file):
    tags_dict = build.tags(posts_dir)
    r_weak = lambda: random.randint(0, 95)
    r_strong = lambda: random.randint(128, 191)
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

    with open(tags_file, 'w') as f:
        f.write(''.join(tags))


    # front matter for all files in tags/
    fm ='---\nlayout: tag\ntag: {}\npermalink: /tag/{}/\ncustom_css: tag\n---'

    for tag, items in tags_dict.items():
        with open('{}/{}.md'.format(tags_dir, tag), 'w') as f:
            f.write(fm.format(tag, tag))


if __name__ == '__main__':
    tags()
