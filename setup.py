#!/usr/bin/env python
from setuptools import setup
import os


# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-block-content',
    version='0.0.1',
    description="A way to embed user-editable and themed micro-content.",
    author='Benjamin W Stookey',
    author_email='ben@aashe.org',
    url='https://github.com/aashe/django-block-content',
    long_description=read("README.md"),
    packages=[
        'block_content',
        'block_content.migrations'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
    install_requires=["Django<=1.4"]
)
