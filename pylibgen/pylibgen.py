import re
from urllib.parse import quote_plus

import requests

from . import constants, exceptions


class Library(object):
    '''Library Genesis search interface wrapper.'''

    def __init__(self, mirror=constants.DEFAULT_MIRROR):
        if mirror not in constants.MIRRORS:
            raise NotImplementedError(
                'Search mirror `{}` not supported.'.format(mirror)
            )
        self.mirror = constants.MIRRORS[mirror]

    def __repr__(self):
        return '<Library ({})>'.format(self.mirror.name)

    def search(self, query, mode='title', page=1, per_page=25):
        '''Searches Library Genesis.

        Notes:
            For search type isbn, either ISBN 10 or 13 is accepted.

        Args:
            query (str): Search query.
            mode (str): Search query mode.
                Can be one of constants.SEARCH_MODES.
            page (int): Result page number.
            per_page (int): Results per page.

        Returns:
            List of Library Genesis book IDs that matched the query.
        '''
        # TODO: pin some params in __req such as Download type: and view simple
        if mode not in constants.SEARCH_MODES:
            raise exceptions.LibraryException((
                'Search mode "{}" not supported.\n'
                'Please specify one of: {}'
            ).format(mode, ', '.join(constants.SEARCH_MODES)))

        if page <= 0:
            raise exceptions.LibraryException(
                'page number must be > 0.'
            )

        if per_page not in constants.SEARCH_RESULTS_PER_PAGE:
            raise exceptions.LibraryException((
                '{} results per page is not supported, sadly.\n'
                'Please specify one of: {}'
            ).format(per_page, ', '.join(map(str, constants.SEARCH_RESULTS_PER_PAGE))))

        resp = self.__req(
            self.mirror.search,
            req=quote_plus(query),
            column=mode,
        )
        return re.findall("<tr.*?><td>(\d+)", resp.text)

    def lookup(self, ids, fields=constants.DEFAULT_BOOK_FIELDS):
        '''Looks up one or more books by book id and returns Book objects.

        Notes:
            To get book IDs, use Library.search().
            The default fields suffice for most use cases, but there are
            a LOT more like openlibraryid, publisher, etc.
            To get all fields, use fields=['*'].

        Args:
            ids (list): Library Genesis book IDs, str or int.
                        Can also be a singular book id as a str or int.
            fields (list): Library Genesis book properties.

        Returns:
            list of Book objects with properties for the specified
            fields. If only one id was specified, then a Book object
            will be returned and it won't be contained in a list.
        '''
        if isinstance(ids, (str, int)):
            ids = [ids]
        ids = list(map(str, ids))

        resp = self.__req(
            self.mirror.lookup,
            ids=','.join(ids),
            fields=','.join(fields),
        ).json()
        if not resp:
            # https://github.com/JoshuaRLi/pylibgen/pull/3
            raise requests.HTTPError(400)

        if len(resp) == 1:
            resp[0].pop('id', None)
            return Book(id=ids[0], **resp[0])
        else:
            books = []
            for r, i in zip(resp, ids):
                r.pop('id', None)
                books.append(Book(id=i, **r))
            return books

    def __req(self, endpoint, **kwargs):
        r = requests.get(endpoint.format(**kwargs))
        r.raise_for_status()
        return r


class Book(object):
    '''Models a Library Genesis book.'''

    __MANDATORY_FIELDS = ('id', 'md5')

    def __init__(self, **fields):
        # properties are dynamically set based on valid fields
        self.__dict__.update({
            k: v for k, v in fields.items()
            if k in constants.ALL_BOOK_FIELDS
        })
        for f in self.__MANDATORY_FIELDS:
            if f not in self.__dict__:
                raise exceptions.BookException(
                    "Book is missing mandatory field {}.".format(f)
                )

    def get_url(self, filehost=constants.DEFAULT_FILEHOST):
        url = self.__fmt_filehost_url(filehost, id=self.id, md5=self.md5)
        return url

    def __fmt_filehost_url(self, filehost, **kwargs):
        try:
            return constants.FILEHOST_URLS[filehost].format(**kwargs)
        except KeyError:
            raise exceptions.BookException((
                'filehost "{}" not supported.\n'
                'Please specify one of: {}'
            ).format(filehost, ', '.join(constants.FILEHOST_URLS)))
