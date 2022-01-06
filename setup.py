#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_namespace_packages, setup

setup(
    name="bytes-distribute",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=["click==8.0.3", "pandas==1.3.5", "XlsxWriter==3.0.2"],
    entry_points={
        "console_scripts": ["bytes-distribute=bytes_distribute.__main__:main"],
    },
)
