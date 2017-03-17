import os
import re
import json
import requests
import webbrowser
from urllib.parse import quote_plus

import topic_tuple

# Mirrors may change over time as they get taken down.
# These two work at the time of development.
MIRRORS = [
    'libgen.io',
    'gen.lib.rus.ec',
]

#SEARCH_URL = 'http://{}/search.php?req=100&res={}&column={}' # changed search format
SEARCH_URL = 'http://{}/search.php?req={}&open=0&column={}'
LOOKUP_URL = 'http://{}/json.php?ids={}&fields={}'
DOWNLOAD_URL = 'http://{}/get.php?md5={}'

TOPICS = topic_tuple.TOPICS

def search(mirror, query, type='title'):
    '''Performs a search query to libgen and returns a list of
    libgen book IDs that matched the query.

    You can specify a search type: title, author, isbn, topic.
    For ISBN searches, the query can be ISBN 10 or 13, either is fine.
    '''
    assert(type in {'title', 'author', 'isbn', 'topic'})

    if type == 'topic':
        assert(TOPICS[query]), 'for a list of possible topics run pylibgen.topics() or pylibgen.classes()'
        print(TOPICS[query])
        url = SEARCH_URL.format(mirror, TOPICS[query], type)
    else:
        url = SEARCH_URL.format(mirror, quote_plus(query), type)
    r = requests.get(url); r.raise_for_status()
    return re.findall("<tr.*?><td>(\d+)", r.text)



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
    url = LOOKUP_URL.format(mirror, ','.join(ids), ','.join(fields))
    r = requests.get(url); r.raise_for_status()
    return r.json()


def get_download_url(mirror, md5, enable_ads=False):
    '''Given the libgen MD5 hash of a book, this returns a valid but
    temporary (keys expire) URL for a direct download. The key is parsed
    from the initial redirect to ads.php.

    If you want to support Library Genesis, setting enable_ads to True
    will just return the download URL with no key, which redirects to ads.php.
    '''
    url = DOWNLOAD_URL.format(mirror, md5)
    if enable_ads:
        return url
    r = requests.get(url); r.raise_for_status()
    key = re.findall("&key=(.*?)'", r.text)[0]
    return url + '&key={}'.format(key)



def download(mirror, md5, dest='.', use_browser=False):
    '''Downloads a book given its libgen MD5 hash to the destination directory.
    
    Libgen seems to delay programmatically sent dl requests, even if the UA
    string is spoofed and the URL contains a good key, so I recommend just 
    using get_download_url. Alternatively, you can set use_browser=True, which
    will just open up the download URL in a new browser tab.
    
    Note that if you spam download requests, libgen will temporarily 503.
    Again, I recommend using get_download_url and downloading from the browser.
    '''
    auth_url = get_download_url(mirror, md5)

    if use_browser:
        webbrowser.open_new_tab(auth_url)
        return

    r = requests.get(auth_url); r.raise_for_status()

    with open(os.path.join(dest, md5), 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

def topics():
    '''Print the possible list of topics.
    
    Libgen seems to delay programmatically sent dl requests, even if the UA
    string is spoofed and the URL contains a good key, so I recommend just 
    using get_download_url. Alternatively, you can set use_browser=True, which
    will just open up the download URL in a new browser tab.
    
    Note that if you spam download requests, libgen will temporarily 503.
    Again, I recommend using get_download_url and downloading from the browser.
    '''

    sorted_t = sorted(TOPICS, key=lambda tup: tup[1], reverse=True)
    sorted_t = sorted(sorted_t, key=lambda tup: tup[0])
    print("Possible topics are")
    for t in sorted_t:
        if t.find('/') != -1:
            print(t)

def classes():
    '''Print the possible list of classes.
    
    Libgen seems to delay programmatically sent dl requests, even if the UA
    string is spoofed and the URL contains a good key, so I recommend just 
    using get_download_url. Alternatively, you can set use_browser=True, which
    will just open up the download URL in a new browser tab.
    
    Note that if you spam download requests, libgen will temporarily 503.
    Again, I recommend using get_download_url and downloading from the browser.
    '''

    sorted_t = sorted(TOPICS, key=lambda tup: tup[1], reverse=True)
    sorted_t = sorted(sorted_t, key=lambda tup: tup[0])
    print("Possible classes are")
    for t in sorted_t:
        if t.find('/') == -1:
            print(t)



