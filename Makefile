test:
	nose2 -v

wipe-dist:
	rm -rf dist/*

package-pypi: wipe-dist
	python setup.py sdist bdist_wheel
	twine check dist/* 
	
publish-test-pypi: package-pypi
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish-pypi: package-pypi
	twine upload dist/*
