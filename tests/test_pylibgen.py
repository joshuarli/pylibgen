from pylibgen import pylibgen


def test_api_endpoints():
    lg = pylibgen.Library()
    ids = lg.search('automate the boring stuff', 'title')
    print(ids)
    data = lg.lookup(ids)
    print(data)
    print(lg.get_download_url(data[0]['md5']))
    # TODO check for 200 success on all possible combinations
    # of mirrors and endpoints
