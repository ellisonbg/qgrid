#!/usr/bin/env python
#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

setup(
    name='qgrid',
    version='0.1.0',
    description='A Pandas DataFrame viewer for IPython Notebook.',
    author='Quantopian Inc.',
    author_email='tshawver@quantopian.com',
    packages=['qgrid'],
    license='Apache 2.0',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],
    install_requires=[
        'numpy',
        'pandas',
        'ipython[notebook]',
    ],
    url="https://github.com/quantopian/qgrid"
)
