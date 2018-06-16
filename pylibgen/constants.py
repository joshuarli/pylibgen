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

FILEHOST_URLS = {
    'libgen.pw':    'https://libgen.pw/item/detail/id/{id}',
    'libgen.io':    'http://libgen.io/ads.php?md5={md5}',
    'library1.org': 'http://library1.org/_ads/{md5}',
    'b-ok.org':     'http://b-ok.org/md5/{md5}',
    'bookfi.net':   'http://bookfi.net/md5/{md5}',
}

DEFAULT_FILEHOST = 'libgen.pw'

DEFAULT_BOOK_FIELDS = (
    'title',
    'author',
    'year',
    'edition',
    'pages',
    'identifier',
    'extension',
    'filesize',
    'md5',
)

ALL_BOOK_FIELDS = (
    'aich',
    'asin',
    'author',
    'bookmarked',
    'btih',
    'city',
    'cleaned',
    'color',
    'commentary',
    'coverurl',
    'crc32',
    'ddc',
    'descr',
    'doi',
    'dpi',
    'edition',
    'extension',
    'filesize',
    'generic',
    'get_url',
    'googlebookid',
    'id',
    'identifier',
    'identifierwodash',
    'issn',
    'issue',
    'language',
    'lbc',
    'lcc',
    'library',
    'local',
    'locator',
    'md5',
    'openlibraryid',
    'orientation',
    'pages',
    'pagesinfile',
    'paginated',
    'periodical',
    'publisher',
    'scanned',
    'searchable',
    'series',
    'sha1',
    'sha256',
    'tags',
    'timeadded',
    'timelastmodified',
    'title',
    'toc',
    'topic',
    'torrent',
    'tth',
    'udc',
    'visible',
    'volumeinfo',
    'year',
)
