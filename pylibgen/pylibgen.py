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
        '''Looks up metadata on Library Genesis books.

        Note:
            To get book IDs, use search(). The default fields
            suffice for most use cases, but there are a LOT more
            like openlibraryid, publisher, etc. To get all fields,
            use fields=['*'].

        Args:
            ids (list): Library Genesis book IDs.
            fields (list): Library Genesis book properties.

        Returns:
            List of dicts each containing values for the specified
            fields for a Library Genesis book ID.
            A single dict if only one str or int id is passed in.
        '''
        # Allow for lookup of a single numeric string by auto casting
        # to a list for convenience.
        if isinstance(ids, (str, int)):
            ids = [str(ids)]
        resp = self.__req(
            self.mirror.lookup,
            ids=','.join(ids),
            fields=','.join(fields),
        ).json()
        if not resp:
            # https://github.com/JoshuaRLi/pylibgen/pull/3
            raise requests.HTTPError(400)
        return resp if len(resp) > 1 else resp[0]

    def __req(self, endpoint, **kwargs):
        r = requests.get(endpoint.format(**kwargs))
        r.raise_for_status()
        return r
