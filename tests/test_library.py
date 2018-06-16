import pylibgen

def test__mirrors():
    for mirror in pylibgen.constants.MIRRORS:
        l = pylibgen.Library(mirror)
        ids = l.search('automate the boring stuff', 'title')
        assert isinstance(ids, list)
        assert set(ids) == set([
            '1421206', '1421207', '1421208', '1351717',
            '1381538', '1381540', '1529338', '2149756',
        ])

        books = l.lookup(ids)
        assert isinstance(books, list)
        assert all((isinstance(b, pylibgen.Book) for b in books))
        assert {(book.id, book.md5) for book in books} == {
            ('1529338', 'd826b3e593b12422784f50d59c97a966'),
            ('1421207', 'b34564156c3778261ed03167b09f6694'),
            ('1381538', '4e0efdd614737fd66408fd43a9d5ff10'),
            ('1381540', '5a64e12e79af379110a31ea04bb6320c'),
            ('1421208', 'c157d6ec28d1a7c4b528f4e6a1ea4c9e'),
            ('1351717', '054255117b2e86251415292ef48320fd'),
            ('1421206', '1af2c71c1342e850e1e47013b06f9eb9'),
            ('2149756', '2699081bc2e3908ece25013109941028'),
        }

        book = l.lookup(1421206)
        assert isinstance(book, pylibgen.Book)
        assert (book.id, book.md5) == \
               ('1421206', '1af2c71c1342e850e1e47013b06f9eb9')