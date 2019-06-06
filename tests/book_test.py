import http.client
from urllib.parse import urlsplit

import pytest

import pylibgen


def check(url):
    u = urlsplit(url)
    # as with libraries, filehosts are also http, and it would be nice to check for https support
    # if filehosts ever switch over. In that case, also add SSL error checking, and don't xfail it.
    conn = http.client.HTTPConnection(u.netloc, timeout=5)
    conn.request("HEAD", u.path + u.query)
    r = conn.getresponse()
    return r.status == 200


@pytest.mark.parametrize("filehost", pylibgen.constants.FILEHOSTS)
def test_filehosts(filehost):
    b = pylibgen.Book(id=1_421_206, md5="1af2c71c1342e850e1e47013b06f9eb9")
    check(b.get_url(filehost))
