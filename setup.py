#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'pygit',
    version = '1.0',
    packages = ['pygit'],
    entry_points = {
       'console_scripts' : [
       'pygit = pygit.cli:main'
       ]
   })
