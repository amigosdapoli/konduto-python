import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "konduto-python",
    version = "0.0.1",
    author = "Fernando Paiva",
    author_email = "fernandosjp@gmail.com",
    description = ("Start python wrapper for Konduto API"),
    license = "AGPLv3",
    keywords = "konduto",
    url = "https://github.com/amigosdapoli/konduto-python/",
    packages=['konduto'],
    long_description=read('README'),
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=('requests==2.11.1')
)