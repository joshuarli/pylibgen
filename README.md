# pylibgen
Python search and download interface for Library Genesis.

pylibgen is Python 3 and depends on the latest version of `requests`.

## Installation

Simply copy `pylibgen.py` to whereever you need it, then import it in your project.

For the lazy: `curl -L https://git.io/vyES7 -o pylibgen.py`

If there is demand, I'll set it up to be pip installable. Shoot me an email or open up an issue if you'd like that!

## Usage

If you're comfortable using the REPL, searching for and downloading books can be a breeze in the terminal!

```
>>> import pylibgen
>>> m = pylibgen.MIRRORS[0]
>>> ids = pylibgen.search(m, 'automate the boring stuff', 'title')
>>> data = pylibgen.lookup(m, ids)
>>> from pprint import pprint; pprint(data[0])
{'author': 'Albert Sweigart',
 'edition': '',
 'extension': 'epub',
 'filesize': '4485769',
 'identifier': '978-1593275990',
 'md5': '054255117b2e86251415292ef48320fd',
 'pages': '0',
 'title': 'Automate the Boring Stuff with Python: Practical Programming for '
          'Total Beginners',
 'year': '2015'}
>>> pylibgen.get_download_url(m, data[0]['md5'])
'http://libgen.io/get.php?md5=054255117b2e86251415292ef48320fd&key=NQTP585IPY102LYG'
```

**NOTE:** Due to the nature of the service Library Genesis provides, its mirrors often get taken down. Feel free to submit any pull requests to update `pylibgen.MIRRORS` as time goes on!

## Disclaimer

Use this at your own risk. I am not responsible/liable for any piracy/copyright infringement/etc. committed by anyone using pylibgen. Blah blah lawyer stuff, etc.