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

from bandwidth.models.mfa_unauthorized_request_error import MfaUnauthorizedRequestError

class TestMfaUnauthorizedRequestError(unittest.TestCase):
    """MfaUnauthorizedRequestError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MfaUnauthorizedRequestError:
        """Test MfaUnauthorizedRequestError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return MfaUnauthorizedRequestError(
                message = 'Unauthorized'
            )
        else:
            return MfaUnauthorizedRequestError(
        )

    def testMfaUnauthorizedRequestError(self):
        """Test MfaUnauthorizedRequestError"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, MfaUnauthorizedRequestError)
        assert instance.message == 'Unauthorized'

if __name__ == '__main__':
    unittest.main()
