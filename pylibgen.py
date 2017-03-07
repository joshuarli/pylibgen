import os
import re
import json
import requests
from urllib.parse import quote_plus

# Mirrors may change over time as they get taken down.
# These two work at the time of development.
MIRRORS = [
    'libgen.io',
    'gen.lib.rus.ec',
]

s_url = 'http://{}/search.php?req={}&res=100&column={}'
d_url = 'http://{}/get.php?md5={}'
q_url = 'http://{}/json.php?ids={}&fields={}'


def search(mirror, query, type='title'):
    '''Performs a search query to libgen and returns a list of
    libgen book IDs that matched the query.

    You can specify a search type: title, author, isbn.
    For ISBN searches, the query can be ISBN 10 or 13, either is fine.
    '''
    assert(type in {'title', 'author', 'isbn'})
    url = s_url.format(mirror, quote_plus(query), type)
    html = requests.get(url).text
    return re.findall("<tr.*?><td>(\d+)", html)


def lookup(mirror, ids, fields=[
        'title', 'author', 'year', 'edition', 'pages',
        'identifier', 'extension', 'filesize', 'md5'
    ]):
    '''Returns a list of JSON dicts each containing metadata field
    values for each libgen book ID. Uses the unofficial libgen query
    API to retrieve this information.
    
    The default fields are probably enough, but there are a LOT
    more like openlibraryid, publisher, etc. To get all fields,
    use fields=['*'].
    '''
    url = q_url.format(mirror, ','.join(ids), ','.join(fields))
    return requests.get(url).json()


def download(mirror, md5, dest='.'):
    '''Downloads a book given its libgen MD5 hash to the destination
    directory. Bypasses ads.php redirect by parsing the download key.'''
    
    url = d_url.format(mirror, md5)
    key = re.findall("&key=(.*?)'", requests.get(url).text)[0]
    r = requests.get(url + '&key={}'.format(key))

    # TODO either get or pass metadata such as book title
    # and file extension so I can save a properly named file.
    with open(os.path.join(dest, md5), 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)


if __name__ == '__main__':
    # Example usage.
    m = MIRRORS[0]

    data = lookup(m, ids=search(
        m, 'automate the boring stuff', 'title'
    ))
    
    from pprint import pprint
    for entry in data:
        if entry.get('extension', '') in {'pdf'}:
            pprint(entry)
            print('\nDownloading...\n')
            download(m, entry['md5'])
