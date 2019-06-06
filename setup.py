import os

from setuptools import find_packages
from setuptools import setup

version = "2.0.2"
url = "https://github.com/JoshuaRLi/pylibgen"

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt")) as f:
    install_requires = f.read()

with open(os.path.join(here, "requirements-dev.txt")) as f:
    dev_requires = f.read()

setup(
    name="pylibgen",
    version=version,
    description="Python interface to Library Genesis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url=url,
    download_url="{}/archive/v{}.tar.gz".format(url, version),
    author="Joshua Li",
    author_email="josh@jrl.ninja",
    maintainer="Joshua Li",
    maintainer_email="josh@jrl.ninja",
    keywords=[
        "libgen",
        "library",
        "genesis",
        "search",
        "download",
        "books",
        "ebooks",
        "textbooks",
    ],
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        # linting and formatting tools (flake8, black) we let pre-commit pin versions
        # build and publishing tools (setuptools, wheel, twine) we always want latest (see makefile)
        # only dev dependencies that should be pinned in extras (imo) is testing (pytest) and pre-commit
        "dev": dev_requires,
    },
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
