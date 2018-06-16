pylibgen
========

|PyPI Version| |Travis Status| |License MIT|

Python interface to Library Genesis.


Installation
------------

pylibgen is tested to support Python 3.4 - 3.6 can be installed via ``pip``. For example:

.. code-block:: sh

    python3 -m pip install pylibgen --user


Usage
-----

.. code-block:: pycon

    >>> from pylibgen import Library
    >>> l = Library()
    >>> # TODO


Support Library Genesis!
------------------------

``Book.get_url()`` will, by default, attempt to bypass any intermediate advertisement pages. If you want to support Library Genesis, I recommend passing ``enable_ads=True`` to ``Library.get_download_url``, which will disable this behavior and return a url that must be visited for a download link.


Development Setup
-----------------

You'll need ``pipenv`` installed. To setup and enter the virtual environment for development:

.. code-block:: sh

    pipenv install --dev && pipenv shell


Disclaimer
----------

Please use ``pylibgen`` with responsibility and at your own risk. I am not responsible or liable for any piracy, copyright infringement, or other offences committed by anyone using this software. Consider supporting your favorite authors by purchasing their works.


.. |PyPI Version| image:: https://img.shields.io/pypi/v/pylibgen.svg
   :target: https://pypi.python.org/pypi/pylibgen

.. |Travis Status| image:: https://travis-ci.org/JoshuaRLi/pylibgen.svg?branch=master
    :target: https://travis-ci.org/JoshuaRLi/pylibgen

.. |License MIT| image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/JoshuaRLi/pylibgen/blob/master/LICENSE
