.PHONY: test clean style build register publish

all: build

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/ .cache/

test:
# Local testing using the system python3 installation.
	python3 -m pytest tests/test_*.py

style:
# Ensure PEP 8 compliant code.
	python3 setup.py flake8

build: clean test style
# Builds the package into a source dist and a wheel binary,
# then installs locally.
	python3 setup.py sdist bdist_wheel
	python3 -m pip install dist/*.whl --user --upgrade

register:
# Registers the package on PyPI.
	test -f ~/.pypirc
	python3 setup.py register -r pypi

publish: build register
# Updates the VERSION file, commits and tags that change, pushes to GitHub
# to effectively trigger a tag tarball build and a TravisCI test.
# Then publishes or re-registers (updates metadata) a new version of the
# package to PyPI.
# Must first locally pass tests, build + install successfully,
# and have no uncommitted (unstaged or staged) changes in the current branch.
	@echo "Checking for clean branch ..."
	git diff --quiet
	git diff --quiet --cached
	@echo "Current version: $(shell python3 setup.py --version)"
	@read -p "Enter new version: " NEWVERSION           && \
		echo "$$NEWVERSION" > VERSION                   && \
		git add VERSION                                 && \
		git commit -m "$$NEWVERSION"                    && \
		git tag -a v"$$NEWVERSION" -m "$$NEWVERSION"    && \
		git push -u origin --follow-tags                && \
		python3 setup.py sdist bdist_wheel upload -r pypi
