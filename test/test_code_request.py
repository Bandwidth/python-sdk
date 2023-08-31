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
from bandwidth.models.code_request import CodeRequest  # noqa: E501
from bandwidth.rest import ApiException

class TestCodeRequest(unittest.TestCase):
    """CodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CodeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeRequest`
        """
        model = bandwidth.models.code_request.CodeRequest()  # noqa: E501
        if include_optional :
            return CodeRequest(
                to = '+19195551234', 
                var_from = '+19195554321', 
                application_id = '66fd98ae-ac8d-a00f-7fcd-ba3280aeb9b1', 
                scope = '2FA', 
                message = 'Your temporary {NAME} {SCOPE} code is {CODE}', 
                digits = 6
            )
        else :
            return CodeRequest(
                to = '+19195551234',
                var_from = '+19195554321',
                application_id = '66fd98ae-ac8d-a00f-7fcd-ba3280aeb9b1',
                message = 'Your temporary {NAME} {SCOPE} code is {CODE}',
                digits = 6,
        )
        """

    def testCodeRequest(self):
        """Test CodeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
