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
    # TODO gen.lib.rus.ec support
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

FILEHOST_URLS = {
    'libgen.pw':    'https://libgen.pw/item/detail/id/{id}',
    'libgen.io':    'http://libgen.io/ads.php?md5={md5}',
    'library1.org': 'http://library1.org/_ads/{md5}',
    'b-ok.org':     'http://b-ok.org/md5/{md5}',
    'bookfi.net':   'http://bookfi.net/md5/{md5}',
}

DEFAULT_FILEHOST = 'libgen.pw'
