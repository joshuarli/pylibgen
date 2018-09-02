.PHONY: all build test lint publish clean

all: build

build: clean test
	python3 setup.py sdist bdist_wheel --universal > /dev/null

test: lint
	python3 -m pytest -v -s tests/test_*.py

lint:
	python3 -m flake8 --exclude tests/test_*.py,__init__.py,setup.py

publish: build
	python3 -m twine upload --sign dist/*

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/
