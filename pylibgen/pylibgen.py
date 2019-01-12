import re
from typing import Iterator
from typing import List
from typing import Union
from urllib.parse import quote_plus

import requests

from . import constants
from . import exceptions


class Book(object):
    """
    Models a Library Genesis book.
    Class properties are dynamically set during initialization if all fields are valid.
    """

    __MANDATORY_FIELDS = ('id', 'md5')

    def __init__(self, **fields: str):
        self.__dict__.update(
            {k: v for k, v in fields.items() if k in constants.ALL_BOOK_FIELDS},
        )
        for f in self.__MANDATORY_FIELDS:
            if f not in self.__dict__:
                raise exceptions.BookException(
                    "Book is missing mandatory field {}.".format(f),
                )

    def get_url(self, filehost=constants.DEFAULT_FILEHOST) -> str:
        url = self.__fmt_filehost_url(filehost, id=self.id, md5=self.md5)
        return url

    def __fmt_filehost_url(self, filehost, **kwargs):
        try:
            return constants.FILEHOST_URLS[filehost].format(**kwargs)
        except KeyError:
            raise exceptions.BookException(
                "filehost {} not supported.\nPlease specify one of: {}".format(
                    filehost, ", ".join(constants.FILEHOST_URLS),
                ),
            )


class Library(object):
    """Library Genesis search interface wrapper."""

    def __init__(self, mirror: str = constants.DEFAULT_MIRROR):
        if mirror not in constants.MIRRORS:
            raise NotImplementedError(
                "Search mirror {} not supported.".format(mirror),
            )
        self.mirror = constants.MIRRORS[mirror]

    def __repr__(self):
        return "<Library ({})>".format(self.mirror.name)

    def search(
        self, query: str, mode: str = "title", page: int = 1, per_page: int = 25,
    ) -> List[str]:
        """Searches Library Genesis.

        Notes:
            For search type isbn, either ISBN 10 or 13 is accepted.

        Args:
            query: Search query.
            mode: Search query mode. Can be one of constants.SEARCH_MODES.
            page: Result page number.
            per_page: Results per page.

        Returns:
            List of Library Genesis book IDs that matched the query.

        Raises:
            pylibgen.exceptions.LibraryException: unexpected/invalid search query.
        """
        if mode not in constants.SEARCH_MODES:
            raise exceptions.LibraryException(
                "Search mode {} not supported.\nPlease specify one of: {}".format(
                    mode, ", ".join(constants.SEARCH_MODES),
                ),
            )

        if page <= 0:
            raise exceptions.LibraryException('page number must be > 0.')

        if per_page not in constants.SEARCH_RESULTS_PER_PAGE:
            raise exceptions.LibraryException(
                (
                    "{} results per page is not supported, sadly.\n"
                    "Please specify one of: {}"
                ).format(
                    per_page, ", ".join(map(str, constants.SEARCH_RESULTS_PER_PAGE)),
                ),
            )

        resp = self.__req(
            self.mirror.search,
            req=quote_plus(query),
            mode=mode,
            page=page,
            per_page=per_page,
        )
        return re.findall(r'<tr.*?><td>(\d+)', resp.text)

    def lookup(
        self,
        ids: List[Union[str, int]],
        fields: List[str] = constants.DEFAULT_BOOK_FIELDS,
    ) -> Iterator[Book]:
        """Looks up one or more books by id and returns Book objects.

        Notes:
            To get book ids, use Library.search().
            The default fields suffice for most use cases,
            but there are a lot more like openlibraryid, publisher, etc.
            To get all fields, use fields=['*'].

        Args:
            ids: Library Genesis book ids.
            fields: Library Genesis book properties.

        Returns:
            iterator of Book objects corresponding to ids, with the specified
            fields filled out and accessible class property.

        Raises:
            requests.HTTPError: a 400 is raised if the response is empty.
        """
        if isinstance(ids, (str, int)):
            ids = [ids]
        ids = tuple(map(str, ids))

        if 'id' not in fields:
            fields.append('id')
        if '*' in fields:
            fields = ['*']

        resp = self.__req(
            self.mirror.lookup,
            ids=','.join(ids),
            fields=','.join(fields),
        ).json()

        if not resp:
            # In rare cases, certain queries can result in a [] resp, e.g.
            # https://github.com/JoshuaRLi/pylibgen/pull/3
            # As of Jan 12 2019 the example in the PR has been resolved,
            # but we're going to keep this here just in case.
            raise requests.HTTPError(400)

        for book_data, _id in zip(resp, ids):
            assert book_data['id'] == _id
            yield Book(**book_data)

    def __req(self, endpoint, **kwargs):
        r = requests.get(endpoint.format(**constants.SEARCH_BASE_PARAMS, **kwargs))
        r.raise_for_status()
        return r
