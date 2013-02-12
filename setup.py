import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Risk",
    version = "0.0.1",
    author = "Chris Perivolaropoulos, Filon Oikonomou",
    author_email = "darksaga2006@gmail.com",
    description = ("A risk game written in python."),
    license = "GPL",
    keywords = "risk game",
    url = "http://packages.python.org/Risk",
    packages=['risk', 'risk.test'],
    install_requires=['nose', 'networkx','mock'],
    long_description=read('README.txt'),
    test_suite='risk.test',
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
)
