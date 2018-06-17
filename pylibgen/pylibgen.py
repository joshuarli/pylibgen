import re
from urllib.parse import quote_plus

import requests

from . import constants, exceptions


class Library(object):
    '''Library Genesis interface wrapper.'''

    def __init__(self, mirror=constants.DEFAULT_MIRROR):
        if mirror not in constants.MIRRORS:
            raise NotImplementedError(
                'Search mirror `{}` not supported.'.format(mirror)
            )
        self.mirror = constants.MIRRORS[mirror]

    def __repr__(self):
        return '<Library ({})>'.format(self.mirror.name)

    def search(self, query, mode='title'):
        '''Searches Library Genesis.

        Note:
            For search type isbn, either ISBN 10 or 13 is accepted.

        Args:
            query (str): Search query.
            type (str): Query type. Can be title, author, isbn.

        Returns:
            List of LibraryGenesis book IDs that matched the query.
        '''
        if mode not in constants.SEARCH_MODES:
            # TODO add support for more fields
            raise exceptions.LibraryException((
                'search mode "{}" not supported.\n'
                'Please specify one of: {}'
            ).format(mode, ', '.join(constants.SEARCH_MODES)))

        resp = self.__req(
            self.mirror.search,
            req=quote_plus(query),
            column=mode,
        )
        return re.findall("<tr.*?><td>(\d+)", resp.text)

    def lookup(self, ids, fields=constants.DEFAULT_BOOK_FIELDS):
        '''Looks up one or more books by book id and returns Book objects.

        Notes:
            To get book IDs, use search().
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

    __MANDATORY_FIELDS = ('id', 'md5')

    def __init__(self, **fields):
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
