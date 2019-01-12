import pytest
import requests

import pylibgen


def check_url(url):
    r = requests.head(url, allow_redirects=True, timeout=3)
    r.raise_for_status()


@pytest.mark.parametrize("fh", pylibgen.constants.FILEHOST_URLS)
def test_filehosts(fh):
    b = pylibgen.Book(id=1_421_206, md5="1af2c71c1342e850e1e47013b06f9eb9")
    try:
        check_url(b.get_url(fh))
    except requests.exceptions.ReadTimeout:
        pytest.xfail(f"Attempt to reach filehost {fh} timed out.")
    except requests.exceptions.SSLError:
        pytest.xfail(
            f"SSLError occurred with filehost {fh}, but an actual browser"
            "might have the appropriate certs.",
        )
