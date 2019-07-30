#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os
import roulette
import codecs

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(HERE, *parts), 'r').read()


long_description = read('README.md')

setup(
    name='roulette',
    version=roulette.__version__,
    author=roulette.__author__,
    author_email='xyzlxw@hotmail.com',
    url='http://github.com/xyzlxw/roulette/',
    license='MIT Licence',
    description='casino game',
    long_description=long_description,
    platforms='any',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
    ],
)
