#! /usr/bin/env python
#  -*- coding: utf-8 -*-

from setuptools import setup

from bootstrap import bootstrap

version = bootstrap.version()

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='ansible-lint-junit',
    packages=['bootstrap'],
    version=version,
    description='ansible-lint to JUnit converter.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='wasil',
    author_email='piotr.m.boruc@gmail.com',
    url='https://github.com/wasilak/ansible-lint-junit',
    download_url='https://github.com/wasilak/ansible-lint-junit/archive/%s.tar.gz' % (version),
    keywords=['ansible', 'junit'],
    classifiers=[],
    entry_points={
        "console_scripts": ['ansible-lint-junit = bootstrap.bootstrap:main']
    },
    install_requires=[
        'ansible-lint>=5.0.7',
        'lxml>=4.6.3',
    ],
    setup_requires=[
        'lxml',
    ],
)
