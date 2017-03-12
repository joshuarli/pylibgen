VERSION=$(shell cat VERSION.txt)

test:
	py.test test_*.py

clean:
	rm -rf build/ dist/ *.egg-info/

build: clean
	python3 ./setup.py bdist_wheel
	python3 -m pip install --user dist/*.whl --upgrade  # test installation

register:
	test -f ~/.pypirc  # Check if we have a pypirc before package registration.
	python3 setup.py register -r pypi

publish: test register
	@echo "Going to tag the most recent commit with v$(VERSION), then build + upload to pypi."
	@read -p "[ENTER/RETURN] to continue." continue
	git tag v$(VERSION)
	git push -u origin --tags
	python3 setup.py sdist upload -r pypi
