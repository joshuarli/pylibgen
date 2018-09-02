import requests
import pylibgen
import pytest


def check_url(url):
    r = requests.head(url, allow_redirects=True, timeout=10)
    r.raise_for_status()


@pytest.mark.parametrize("fh", pylibgen.constants.FILEHOST_URLS)
def test_filehosts(fh):
    b = pylibgen.Book(id=1421206, md5="1af2c71c1342e850e1e47013b06f9eb9")
    check_url(b.get_url(fh))
