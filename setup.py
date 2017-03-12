#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
from setuptools import setup, find_packages
from codecs import open

AUTHOR = 'Joshua Li'
AUTHOR_GH = 'JoshuaRLi'
AUTHOR_MAIL = 'joshua.r.li.98@gmail.com'
PACKAGE_NAME = 'pylibgen'
LICENSE = 'MIT'
DESCRIPTION = 'Python search and download interface for Library Genesis.'
KEYWORDS = 'libgen library genesis search download books ebooks textbooks joshuarli'
REQUIRED_PACKAGES = [
    'requests',
]
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

######################################################################

_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read().strip()

with open(os.path.join(_here, 'VERSION.txt'), 'r') as f:
    VERSION = f.read().strip()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    download_url='https://github.com/{}/{}/tarball/v{}'.format(AUTHOR_GH, PACKAGE_NAME, VERSION),
    long_description=LONG_DESCRIPTION,
    url='https://github.com/{}/{}'.format(AUTHOR_GH, PACKAGE_NAME),
    author=AUTHOR,
    author_email=AUTHOR_MAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
)
