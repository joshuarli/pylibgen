import os

from setuptools import find_packages
from setuptools import setup

version = "2.0.0"
url = "https://github.com/JoshuaRLi/pylibgen"

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt")) as f:
    install_requires = f.read()

setup(
    name="pylibgen",
    version=version,
    description="Python interface to Library Genesis.",
    long_description=long_description,
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
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
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
