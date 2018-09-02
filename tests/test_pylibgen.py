from pylibgen import Library, constants

def test_api_endpoints():
    for mirror in constants.MIRRORS:
        lg = Library(mirror)
        ids = lg.search('automate the boring stuff', 'title')
        assert isinstance(ids, list)
        assert set(ids) == set([
            '1421206', '1421207', '1421208', '1351717',
            '1381538', '1381540', '1529338', '2149756',
        ])

        books = lg.lookup(ids)
        assert isinstance(books, list)
        assert isinstance(books[0], dict)
        assert {book['md5'].lower() for book in books} == {
            'd826b3e593b12422784f50d59c97a966',
            'b34564156c3778261ed03167b09f6694',
            '4e0efdd614737fd66408fd43a9d5ff10',
            '5a64e12e79af379110a31ea04bb6320c',
            'c157d6ec28d1a7c4b528f4e6a1ea4c9e',
            '054255117b2e86251415292ef48320fd',
            '1af2c71c1342e850e1e47013b06f9eb9',
            '2699081bc2e3908ece25013109941028',
        }

        book = lg.lookup(1421206)
        assert isinstance(book, dict)
        assert book['md5'] == '1af2c71c1342e850e1e47013b06f9eb9'
