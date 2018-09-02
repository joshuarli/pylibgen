import os
from setuptools import setup

AUTHOR_GITHUB = 'JoshuaRLi'
SETUP_BASE = {
    'name': 'pylibgen',
    'description': 'Python search and download interface for Library Genesis.',
    'license': 'MIT',
    'author': 'Joshua Li',
    'author_email': 'joshua.r.li.98@gmail.com',
    'keywords': [
        'libgen',
        'library',
        'genesis',
        'search',
        'download',
        'books',
        'ebooks',
        'textbooks',
    ],
    # 'packages': find_packages(exclude=['tests']),
    'py_modules': [
        'pylibgen',
    ],
    # 'entry_points': {
    #     'console_scripts': [
    #         'executable_name=package:module:main',
    #     ],
    # },
    'install_requires': [
        'requests',
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
}

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    SETUP_BASE['long_description'] = f.read().strip()

with open(os.path.join(here, 'VERSION'), 'r') as f:
    SETUP_BASE['version'] = f.read().strip()

setup(
    url='https://github.com/{0}/{name}'.format(
        AUTHOR_GITHUB, **SETUP_BASE
    ),
    download_url='https://github.com/{0}/{name}/tarball/v{version}'.format(
        AUTHOR_GITHUB, **SETUP_BASE
    ),
    **SETUP_BASE
)
