# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bandwidth.models.tfv_basic_authentication import TfvBasicAuthentication

class TestTfvBasicAuthentication(unittest.TestCase):
    """TfvBasicAuthentication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TfvBasicAuthentication:
        """Test TfvBasicAuthentication
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return TfvBasicAuthentication(
                username = 'username',
                password = 'password'
            )
        else:
            return TfvBasicAuthentication(
                username = 'username',
                password = 'password',
        )

    def testTfvBasicAuthentication(self):
        """Test TfvBasicAuthentication"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, TfvBasicAuthentication)
        assert instance.username == 'username'
        assert instance.password == 'password'

if __name__ == '__main__':
    unittest.main()
