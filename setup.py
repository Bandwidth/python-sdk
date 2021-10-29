# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='bandwidth-sdk',
    version='13.0.0',
    description='Bandwidth\'s set of APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Bandwidth',
    author_email='letstalk@bandwidth.com',
    url='https://dev.bandwidth.com/',
    keywords=["bandwidth"],
    packages=find_packages(),
    python_requires='>=3.6.0',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    ],
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0',
        'enum34>=1.1.6',
        'lxml>=4.3.4'
    ]
)
