from setuptools import setup

setup(
    name='ansible-lint-junit',
    packages=['bootstrap'],
    version='0.8',
    description='ansible-lint to JUnit converter.',
    author='wasil',
    author_email='piotr.m.wasilewski@gmail.com',
    url='https://github.com/wasilak/ansible-lint-junit',
    download_url='https://github.com/wasilak/ansible-lint-junit/archive/0.8.tar.gz',
    keywords=['ansible', 'junit'],
    classifiers=[],
    entry_points = {
        "console_scripts": ['ansible-lint-junit = bootstrap.bootstrap:main']
    },
    install_requires=[
        'ansible-lint',
    ],
)
