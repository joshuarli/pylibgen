.PHONY: all build test lint format publish clean

all: build

build: clean test
	python setup.py sdist bdist_wheel --universal > /dev/null

test: lint
	python -m pytest -v -s tests/test_*.py

lint: format
	python -m flake8 --exclude tests/test_*.py,__init__.py,setup.py

format:
	python -m black .

publish: build
	python -m twine upload --sign dist/*

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/
