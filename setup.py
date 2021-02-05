
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hetznerdns",
    version="1.0.0",
    author="Ivan Ermilov",
    author_email="ivan.s.ermilov@gmail.com",
    description="An API and CLI client for Hetzner DNS service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    scripts=['scripts/hetznerdns-cli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
