#!/usr/bin/python
# coding: utf-8 -*-

import shutil
from setuptools import setup

# here = os.path.abspath(os.path.dirname(__file__))
# requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="EVE-NG toolset",
    version="0.0.1",
    python_requires=">=3.6",
    scripts=["bin/eve-node-connector"],
    install_requires=required,
    include_package_data=True,
    url="https://github.com/titom73/eve-ng-toolset",
    license="APACHE",
    author="Thomas Grimonet",
    author_email="tom@inetsix.net",
    description=long_description,
)
