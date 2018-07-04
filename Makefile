.PHONY: build publish clean style test

all: build

# Builds the package into a source dist and a wheel binary.
build: clean test
	python3 setup.py sdist bdist_wheel --universal > /dev/null

publish: build
	python3 -m twine upload --sign dist/*

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/ .cache/

style:
	python3 -m flake8 --exclude tests/test_*.py,__init__.py,setup.py

test: style
	python3 -m pytest -v -s tests/test_*.py
