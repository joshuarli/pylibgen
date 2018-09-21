.PHONY: all build test publish clean

all: build

build: clean test
	python setup.py sdist bdist_wheel --universal > /dev/null

test:
	tox

publish: build
	python -m twine upload --sign dist/*

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/
