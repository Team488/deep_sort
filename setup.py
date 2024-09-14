#!/usr/bin/env python

import pathlib

import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


setuptools.setup(name='deep_sort',
      version='0.1',
      description='Python Distribution Utilities',
      author='Saqib Rokadia',
      author_email='saqib@saqibr.com',
      url='https://github.com/rokadias/deep_sort',
      packages=['deep_sort'],
      install_reqs=install_requires,
     )
