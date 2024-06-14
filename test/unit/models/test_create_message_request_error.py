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
from bandwidth.models.create_message_request_error import CreateMessageRequestError  # noqa: E501
from bandwidth.rest import ApiException

class TestCreateMessageRequestError(unittest.TestCase):
    """CreateMessageRequestError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateMessageRequestError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMessageRequestError`
        """
        model = bandwidth.models.create_message_request_error.CreateMessageRequestError()  # noqa: E501
        if include_optional :
            return CreateMessageRequestError(
                type = '',
                description = '',
                field_errors = [
                    bandwidth.models.field_error.fieldError(
                        field_name = 'from',
                        description = ''+invalid' must be replaced with a valid E164 formatted telephone number', )
                    ]
            )
        else :
            return CreateMessageRequestError(
                type = '',
                description = '',
        )
        """

    def testCreateMessageRequestError(self):
        """Test CreateMessageRequestError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
