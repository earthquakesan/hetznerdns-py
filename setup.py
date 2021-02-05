
import setuptools

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hetznerdns",
    version="1.0.4",
    author="Ivan Ermilov",
    author_email="ivan.s.ermilov@gmail.com",
    description="An API and CLI client for Hetzner DNS service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=load_requirements("requirements.txt"),
    scripts=['scripts/hetznerdns-cli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
