.PHONY: clean style test build

all: build

build: clean test
# Builds the package into a source dist and a wheel binary.
	python3 setup.py sdist bdist_wheel --universal > /dev/null
	@printf 'Install the wheel locally (you must exit pipenv) with: python3 -m pip install dist/*.whl --user --upgrade\n'

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/ .cache/

style:
	python3 -m flake8 --exclude tests/test_*.py,__init__.py,setup.py

test: style
	python3 -m pytest -n auto -s tests/test_*.py
