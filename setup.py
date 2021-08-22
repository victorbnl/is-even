#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='is-even',
    version='1.0.1',
    description='Return true if the given number is even.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Victor B",
    author_email="victor.bonnelle@protonmail.com",
    maintainer="Victor B",
    maintainer_email="victor.bonnelle@protonmail.com",
    url='https://github.com/victorbnl/is-even/',
    packages=[
        'is_even'
    ]
)
