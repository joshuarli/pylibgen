.PHONY: todo clean style test build register publish

all: build

clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info/ .cache/

style:
	flake8 --exclude tests/test_*.py __init__.py

test: style
	python3 -m pytest -s tests/test_*.py

build: clean test
# Builds the package into a source dist and a wheel binary,
# then installs locally.
	python3 setup.py sdist bdist_wheel > /dev/null
	python3 -m pip install dist/*.whl --user --upgrade > /dev/null

register:
# Registers the package on PyPI.
	test -f ~/.pypirc
	python3 setup.py register -r pypi > /dev/null

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
		git commit -S -m "$$NEWVERSION"                 && \
		git tag -s -a v"$$NEWVERSION" -m "$$NEWVERSION" && \
		git push -u origin --follow-tags                && \
		python3 setup.py sdist bdist_wheel upload -r pypi
