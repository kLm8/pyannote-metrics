#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2014 CNRS (Hervé BREDIN - http://herve.niderb.fr)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import versioneer
versioneer.versionfile_source = 'pyannote/metrics/_version.py'
versioneer.versionfile_build = versioneer.versionfile_source
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'pyannote-metrics-'

from setuptools import setup, find_packages

setup(

    # package
    namespace_packages = ['pyannote'],
    packages=find_packages(),
    install_requires=[
        'pyannote.core >= 0.0.2',
    ],
    # versioneer
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    # PyPI
    name='pyannote.metrics',
    description=('PyAnnote metrics'),
    author='Hervé Bredin',
    author_email='bredin@limsi.fr',
    url='http://herve.niderb.fr/',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering"
    ],        
)