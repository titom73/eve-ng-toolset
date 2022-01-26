#!/usr/bin/python
# coding: utf-8 -*-

import shutil
from setuptools import setup
import inetsixEve

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="eve-ng-toolset",
    version="{}".format(inetsixEve.__version__),
    python_requires=">=3.6",
    packages=['inetsixEve'],
    scripts=["bin/eve-nodes-connector", "bin/eve-lab-manager"],
    install_requires=required,
    include_package_data=True,
    url="https://github.com/titom73/eve-ng-toolset",
    license="APACHE",
    author="{}".format(inetsixEve.__author__),
    author_email="{}".format(inetsixEve.__email__),
    description=long_description,
)
