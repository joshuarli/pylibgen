.PHONY: all
all: build

.PHONY: build
build: clean test
	python -m pip install --upgrade setuptools wheel
	python setup.py sdist bdist_wheel

.PHONY: test
test:
	tox

.PHONY: publish
publish: build
	python -m pip install --upgrade twine
	python -m twine upload --sign dist/*

.PHONY: clean
clean:
	rm -rf venv/ build/ dist/ *.egg-info/
	find -type f -iname '*.pyc' -delete
	find -type d -iname '__pycache__' -delete
