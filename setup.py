"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""

import os
from setuptools import setup, find_packages  # noqa: H301

NAME = "bandwidth-sdk"
VERSION = os.environ['RELEASE_VERSION']
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Bandwidth",
    author="Bandwidth",
    author_email="letstalk@bandwidth.com",
    url="https://dev.bandwidth.com/sdks/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Bandwidth"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Bandwidth&#39;s Communication APIs  # noqa: E501
    """
)
