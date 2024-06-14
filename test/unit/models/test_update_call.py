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
import datetime

import bandwidth
from bandwidth.models.update_call import UpdateCall  # noqa: E501
from bandwidth.rest import ApiException

class TestUpdateCall(unittest.TestCase):
    """UpdateCall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateCall
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCall`
        """
        model = bandwidth.models.update_call.UpdateCall()  # noqa: E501
        if include_optional :
            return UpdateCall(
                state = 'active',
                redirect_url = 'https://myServer.example/bandwidth/webhooks/redirect',
                redirect_method = 'POST',
                username = 'mySecretUsername',
                password = 'mySecretPassword1!',
                redirect_fallback_url = 'https://myFallbackServer.example/bandwidth/webhooks/redirect',
                redirect_fallback_method = 'POST',
                fallback_username = 'mySecretUsername',
                fallback_password = 'mySecretPassword1!',
                tag = 'My Custom Tag'
            )
        else :
            return UpdateCall(
        )
        """

    def testUpdateCall(self):
        """Test UpdateCall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
