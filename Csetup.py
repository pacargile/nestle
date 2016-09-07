#!/usr/bin/env python
import re, os
from distutils.core import setup
from Cython.Build import cythonize
import numpy

# Synchronize version from code.
version = re.findall(r"__version__ = \"(.*?)\"", open("Cnestle.pyx").read())[0]

os.environ["CC"] = "/opt/local/bin/gcc-mp-6"

setup(
   name = 'Cnestle',
   ext_modules = cythonize(["Cnestle.pyx"],compiler_directives={'optimize.use_switch':True,'optimize.unpack_method_calls':True}),
   version=version,
   include_dirs=[numpy.get_include()]
)