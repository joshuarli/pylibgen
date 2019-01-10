from collections import namedtuple

__Mirror = namedtuple("Mirror", ("name", "search", "lookup"))

MIRRORS = {
    "libgen.io": __Mirror(
        "libgen.io",
        "http://libgen.io/search.php"
        "?req={req}"
        "&page={page}"
        "&res={per_page}"
        "&column={mode}"
        "&lg_topic={lg_topic}"
        "&view={view}"
        "&open={open}"
        "&phrase={phrase}",
        "http://libgen.io/json.php" "?ids={ids}" "&fields={fields}",
    ),
    # TODO gen.lib.rus.ec support
}

DEFAULT_MIRROR = "libgen.io"

# these query parameters for mirror/search.php are pinned.
SEARCH_BASE_PARAMS = {
    # database to search in. libgen is also known as Sci-Tech.
    "lg_topic": "libgen",
    # View results: simple
    "view": "simple",
    # Download type: Resumed dl with original filename
    "open": 0,
    # Search with mask (e.g. word*), 0 actually enables this
    "phrase": 0,
}

# modes year, publisher, series, language, extension, tags are possible,
# but way too general and not recommended.
# AFAIK, there isn't a way to combine multiple search modes and respective
# strings to filter down the search.
SEARCH_MODES = ("title", "author", "isbn")

# strangely, libgen only allows these amounts.
SEARCH_RESULTS_PER_PAGE = (25, 50, 100)

FILEHOST_URLS = {
    "libgen.io": "http://libgen.io/ads.php?md5={md5}",
    # currently unresolvable with 8.8.8.8, but works on quad9 and cloudflare
    #    "ambry.pw": "https://ambry.pw/item/detail/id/{id}",
    "library1.org": "http://library1.org/_ads/{md5}",
    "b-ok.org": "http://b-ok.org/md5/{md5}",
    "bookfi.net": "http://bookfi.net/md5/{md5}",
}

DEFAULT_FILEHOST = "libgen.io"

DEFAULT_BOOK_FIELDS = [
    "title",
    "author",
    "year",
    "edition",
    "pages",
    "identifier",
    "extension",
    "filesize",
    "md5",
    "id",
]

ALL_BOOK_FIELDS = {
    "aich",
    "asin",
    "author",
    "bookmarked",
    "btih",
    "city",
    "cleaned",
    "color",
    "commentary",
    "coverurl",
    "crc32",
    "ddc",
    "descr",
    "doi",
    "dpi",
    "edition",
    "extension",
    "filesize",
    "generic",
    "googlebookid",
    "id",
    "identifierwodash",
    "issn",
    "language",
    "lbc",
    "lcc",
    "library",
    "local",
    "locator",
    "md5",
    "openlibraryid",
    "orientation",
    "pages",
    "paginated",
    "periodical",
    "publisher",
    "scanned",
    "searchable",
    "series",
    "sha1",
    "sha256",
    "tags",
    "timeadded",
    "timelastmodified",
    "title",
    "toc",
    "topic",
    "torrent",
    "tth",
    "udc",
    "visible",
    "volumeinfo",
    "year",
}
