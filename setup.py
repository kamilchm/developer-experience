#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

readme = open('README.md').read()
with open('requirements-dev.txt') as f:
    required_dev = f.read().splitlines()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='hackernews-cli',
    description='Read HackerNews lika a hacker',
    long_description=readme,
    author='Kamil Chmielewski',
    author_email='kamil.chm@gmail.com',
    url='https://github.com/kamilchm/developer-experience',
    license="Apache License (2.0)",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    setup_requires=['setuptools>=2.2'] + required_dev,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'hn = hncli.cli:cli',
        ],
    },
    vcversioner={
        'version_module_paths': ['hncli/_version.py'],
    },
)
