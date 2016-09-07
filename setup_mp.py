#!/usr/bin/env python
import re
from setuptools import setup

# Synchronize version from code.
version = re.findall(r"__version__ = \"(.*?)\"", open("nestle_mp.py").read())[0]

setup(name="nestle_mp", 
      version=version,
      py_modules=["nestle_mp"]
      )
