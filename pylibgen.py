import os
import re
import json
import requests

MIRRORS = [
    'libgen.io',
    'gen.lib.rus.ec',
]

s_url = 'http://{}/search.php?req={}&res=100&column={}'
d_url = 'http://{}/get.php?md5={}'
q_url = 'http://{}/json.php?ids={}&fields={}'


def get_metadata(mirror, ids, fields=[
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
    j = get_metadata(MIRRORS[0], ids=['1', '2', '3'])
    from pprint import pprint
    pprint(j)
