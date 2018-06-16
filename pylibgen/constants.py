from collections import namedtuple

__Mirror = namedtuple('Mirror', ('name', 'search', 'lookup'))

MIRRORS = {
    'libgen.io': __Mirror(
        'libgen.io',
        'http://libgen.io/search.php'
        '?req={req}&res=100&column={column}',
        'http://libgen.io/json.php'
        '?ids={ids}&fields={fields}',
    )
    # gen.lib.rus.ec support is pending.
}

DEFAULT_MIRROR = 'libgen.io'

DEFAULT_SEARCH_FIELDS = [
    'title',
    'author',
    'year',
    'edition',
    'pages',
    'identifier',
    'extension',
    'filesize',
    'md5',
]
