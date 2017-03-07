import os
import re
import requests

MIRRORS = [
    'libgen.io',
    'gen.lib.rus.ec',
]

s_url = 'http://{}/search.php?req={}&res=100&column={}'
d_url = 'http://{}/get.php?md5={}'


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
