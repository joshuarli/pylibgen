.PHONY: all
all: build

.PHONY: build
build: clean test
	python setup.py sdist bdist_wheel > /dev/null

.PHONY: test
test:
	tox

.PHONY: publish
publish: build
	python -m twine upload --sign dist/*

.PHONY: clean
clean:
	rm -rf venv/ build/ dist/ *.egg-info/
	find -type f -iname '*.pyc' -delete
	find -type d -iname '__pycache__' -delete
