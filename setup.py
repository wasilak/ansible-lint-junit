from setuptools import setup

from bootstrap import bootstrap

version = bootstrap.version()

setup(
    name='ansible-lint-junit',
    packages=['bootstrap'],
    version=version,
    description='ansible-lint to JUnit converter.',
    author='wasil',
    author_email='piotr.m.wasilewski@gmail.com',
    url='https://github.com/wasilak/ansible-lint-junit',
    download_url='https://github.com/wasilak/ansible-lint-junit/archive/%s.tar.gz' % (version),
    keywords=['ansible', 'junit'],
    classifiers=[],
    entry_points={
        "console_scripts": ['ansible-lint-junit = bootstrap.bootstrap:main']
    },
    install_requires=[
        'ansible-lint',
        'lxml',
    ],
    setup_requires=[
        'lxml',
    ],
)
