import os
from setuptools import setup, find_packages

VERSION = '1.3.1'
REPO = 'https://github.com/JoshuaRLi/pylibgen'

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read().strip()

setup(
    name='pylibgen',
    version=VERSION,
    description='Python interface to Library Genesis.',
    long_description=LONG_DESC,
    license='MIT',
    url=REPO,
    download_url='{}/archive/v{}.tar.gz'.format(REPO, VERSION),
    author='Joshua Li',
    author_email='joshua.r.li.98@gmail.com',
    maintainer='Joshua Li',
    maintainer_email='joshua.r.li.98@gmail.com',
    keywords=[
        'libgen',
        'library',
        'genesis',
        'search',
        'download',
        'books',
        'ebooks',
        'textbooks',
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'wheel',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
