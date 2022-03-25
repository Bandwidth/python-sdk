"""
    Messaging

    Test Bandwidth's HTTP Messaging platform ## Base Path <code>https://messaging.bandwidth.com/api/v2</code>  # noqa: E501

    The version of the OpenAPI document: 4.2.8
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "bandwidth-sdk"
VERSION = "14.0.0"
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
    description="Messaging",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://dev.bandwidth.com/sdks/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Messaging"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Test Bandwidth&#39;s HTTP Messaging platform ## Base Path &lt;code&gt;https://messaging.bandwidth.com/api/v2&lt;/code&gt;  # noqa: E501
    """
)
