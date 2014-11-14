#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='expertsender',
    version='0.1.2',
    description='Python API library for the ExpertSender email platform',
    author='Gilang Chandrasa',
    author_email='gilang@launchpotato.com',
    url='https://github.com/gchandrasa/expertsender',
    packages=[
        'expertsender',
    ],
    package_dir={'expertsender':
                 'expertsender'},
    install_requires=[
        "requests",
        "lxml",
    ],
)
