import os
import frontmatter

def clean_dirpath(dirpath):
    # remove './' prefix
    if len(dirpath) > 1 and dirpath[:2] == './':
        dirpath = dirpath[2:]
    return dirpath

def check_dirpath(dirpath):
    # make sure dirpath doesn't start with '.'
    return len(dirpath) == 1 or dirpath[0] != '.'

def check_filename(filename, ext='.md'):
    # ignore dotfiles, README, check for extension
    return len(filename) > 3 and filename[-3:] == ext \
    and filename[0] != '.'

def clean_filename(filename, date_format='YYYY-MM-DD-'):
    # remove date prefix and extension
    return os.path.splitext(filename[len(date_format):])[0]

def map(root='.', cat_prefix=''):
    # path is relative to execution directory, not to location of script
    os.chdir(root)

    directories = []
    num_files = 0
    for (dirpath, dirnames, filenames) in os.walk('.'):
        dirpath = clean_dirpath(dirpath)
        if not check_dirpath(dirpath):
            continue

        files = []
        for filename in filenames:
            if not check_filename(filename):
                continue
            num_files += 1
            # extract title from frontmatter
            with open('{}/{}'.format(dirpath, filename), 'r') as f:
                title = frontmatter.loads(f.read())['title']
                files.append({'file':clean_filename(filename), 'title':title})

        directories.append({'dir':dirpath, 'files':files})

    # generate markdown from directories list
    cats, links = [], [] # lists that will later be joined into strings
    indent, h, h_sub = '    ', '##', '####'

    for directory in directories:
        d, files = directory['dir'], directory['files']
        d_segments = d.split('/')
        level = len(d_segments)-1

        if d != '.':
            # for github in-page header anchors, '/' -> '' and ' ' -> '-'
            count = '<sup>({})</sup>'.format(len(files)) if len(files) else ''
            cats.append('{}* [{}{}](#{}) {}\n'
                .format( indent*level, cat_prefix, d_segments[-1],
                d.lower().replace(' ', '-').replace('/', '--'), count ))
            header = h_sub if level > 0 else h
            # with directory headers, pad '/' with spaces for readability
            links.append('\n{} {}\n'.format( header, d.replace('/', ' / ')) )

        for f in reversed(files): # display newest posts first
            links.append('* [{}]({}/{})\n'
                .format(f['title'], d.lower(), f['file']))

    cats.append('\n---\n')
    return({
        'count': '\n__{}__ and counting...\n\n---'.format(num_files),
        'cats': '\n\n## Categories\n\n' + ''.join(cats),
        'links': ''.join(links)
    })
