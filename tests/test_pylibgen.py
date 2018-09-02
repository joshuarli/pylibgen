from pylibgen import pylibgen, constants

# Ensure that API endpoints are working and returning the
# expected responses for all mirrors.
def test_api_endpoints():
    for mirror in constants.MIRRORS:
        lg = pylibgen.Library(mirror)
        ids = lg.search('automate the boring stuff', 'title')
        assert set(ids) == set([
            '1421206', '1421207', '1421208', '1351717',
            '1381538', '1381540', '1529338',
        ])

        books = lg.lookup(ids)
        assert {book['md5'] for book in books} == {
            'd826b3e593b12422784f50d59c97a966',
            'b34564156c3778261ed03167b09f6694',
            '4e0efdd614737fd66408fd43a9d5ff10',
            '5a64e12e79af379110a31ea04bb6320c',
            'c157d6ec28d1a7c4b528f4e6a1ea4c9e',
            '054255117b2e86251415292ef48320fd',
            '1af2c71c1342e850e1e47013b06f9eb9',
        }

        lg.get_download_url(books[0]['md5'])
