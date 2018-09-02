import pylibgen
import pytest

test_books = {
    # Automate the Boring Stuff with Python: Practical Programming for Total Beginners
    ("automate the boring stuff", "title"): {
        # id: hash
        "1529338": "d826b3e593b12422784f50d59c97a966",
        "1421207": "b34564156c3778261ed03167b09f6694",
        "1381538": "4e0efdd614737fd66408fd43a9d5ff10",
        "1381540": "5a64e12e79af379110a31ea04bb6320c",
        "1421208": "c157d6ec28d1a7c4b528f4e6a1ea4c9e",
        "1351717": "054255117b2e86251415292ef48320fd",
        "1421206": "1af2c71c1342e850e1e47013b06f9eb9",
        "2149756": "2699081bc2e3908ece25013109941028",
    },
    # Free software, free society: selected essays of Richard M. Stallman
    ("1882114981", "isbn"): {
        "112887": "861c055b960e7f36d95164cab34e0e97",
        "310297": "3b46ed45310545cc1f6d7b627f9b640d",
    },
    # Same as above, but ISBN 13 instead of 10
    ("9781882114986", "isbn"): {
        "112887": "861c055b960e7f36d95164cab34e0e97",
        "310297": "3b46ed45310545cc1f6d7b627f9b640d",
    },
}


@pytest.mark.parametrize("mirror", pylibgen.constants.MIRRORS)
@pytest.mark.parametrize("test_book", list(test_books.items()))
def test_mirror(mirror, test_book):
    search_params, md5_of_ids = test_book
    l = pylibgen.Library(mirror)
    ids = l.search(*search_params)

    assert isinstance(ids, list)
    assert set(ids) == set(md5_of_ids.keys())

    books = l.lookup(ids)
    assert isinstance(books, list)
    assert all((isinstance(b, pylibgen.Book) for b in books))
    for book in books:
        assert md5_of_ids[book.id] == book.md5.lower()


@pytest.mark.parametrize("mirror", pylibgen.constants.MIRRORS)
def test_all_book_fields(mirror):
    l = pylibgen.Library(mirror)
    book = l.lookup("112887", fields=["*"])
    assert set(book.__dict__.keys()) == pylibgen.constants.ALL_BOOK_FIELDS
