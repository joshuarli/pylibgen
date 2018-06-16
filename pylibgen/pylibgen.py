import re
from urllib.parse import quote_plus

import requests

from . import constants


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
        assert(mode in ('title', 'author', 'isbn'))
        resp = self.__req(
            self.mirror.search,
            req=quote_plus(query),
            column=mode,
        )
        return re.findall("<tr.*?><td>(\d+)", resp.text)

    def lookup(self, ids, fields=constants.DEFAULT_SEARCH_FIELDS):
        '''Looks up one or more books by book id.

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
        resp = self.__req(
            self.mirror.lookup,
            ids=','.join(map(str, ids)),
            fields=','.join(fields),
        ).json()
        if not resp:
            # https://github.com/JoshuaRLi/pylibgen/pull/3
            raise requests.HTTPError(400)
        if len(resp) == 1:
            return Book(**resp[0])
        else:
            return [Book(**r) for r in resp]

    def __req(self, endpoint, **kwargs):
        r = requests.get(endpoint.format(**kwargs))
        r.raise_for_status()
        return r


class Book(object):

    def __init__(self, **fields):
        # TODO filter based on constants.ALL_FIELDS
        self.__dict__.update(fields)

    def get_url(self):
        raise NotImplementedError()
