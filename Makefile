test:
	nose2 -v

wipe-dist:
	rm -rf dist/*

package-pipy: wipe-dist
	python setup.py sdist bdist_wheel
	twine check dist/* 
	
publish-test-pipy: package-pipy
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish-pipy: package-pipy
	twine upload dist/*
