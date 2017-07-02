pylibgen
==========================
|PyPI Version| |Travis Status| |License MIT|

Python search and download interface for Library Genesis.

Installation
---------------------

pylibgen can be installed through pip!
::

    $ pip3 install pylibgen --user

Alternatively, you can just put a copy of :code:`pylibgen.py` to wherever you need it:
::

    $ curl -L https://git.io/vyES7 -o pylibgen.py

Usage
---------------------

You're probably looking for pylibgen-cli_, which is a CLI wrapper around pylibgen's functionality, but here is a demonstration in the interactive interpreter:

.. code-block:: pycon

    >>> from pylibgen import pylibgen
    >>> lg = pylibgen.Library()
    >>> ids = lg.search('automate the boring stuff', 'title')
    >>> data = lg.lookup(ids)
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

    >>> lg.get_download_url(data[0]['md5'])

    'http://libgen.io/get.php?md5=054255117b2e86251415292ef48320fd&key=NQTP585IPY102LYG'

Compatibility
---------------------

pylibgen is tested to work with python 3.3 - 3.6.

Notes
---------------------

Due to the nature of the service Library Genesis provides, its mirrors often get taken down. Feel free to submit any pull requests to update :code:`pylibgen.MIRRORS` as time goes on!

Support Library Genesis!
--------------------------

:code:`get_download_url` will, by default, parse the temporary download key necessary for a direct download URL from libgen's ads.php redirect.

If you want to support Library Genesis, I recommend passing :code:`enable_ads=True` to :code:`get_download_url`, as this will return the plain download URL, which shows an ad first when visited.

Disclaimer
---------------------

Use this at your own risk. I am not responsible or liable for any piracy, copyright infringement, or other things committed by anyone using pylibgen. Blah blah lawyer stuff, etc.


.. _pylibgen-cli: https://github.com/JoshuaRLi/pylibgen-cli

.. |PyPI Version| image:: https://img.shields.io/pypi/v/pylibgen.svg
   :target: https://pypi.python.org/pypi/pylibgen

.. |Travis Status| image:: https://travis-ci.org/JoshuaRLi/pylibgen.svg?branch=master
    :target: https://travis-ci.org/JoshuaRLi/pylibgen

.. |License MIT| image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/JoshuaRLi/pylibgen/blob/master/LICENSE
