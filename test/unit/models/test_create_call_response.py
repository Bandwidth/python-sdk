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

from bandwidth.models.create_call_response import CreateCallResponse

class TestCreateCallResponse(unittest.TestCase):
    """CreateCallResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCallResponse:
        """Test CreateCallResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCallResponse`
        """
        model = CreateCallResponse()
        if include_optional:
            return CreateCallResponse(
                application_id = '04e88489-df02-4e34-a0ee-27a91849555f',
                account_id = '9900000',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                to = '+19195551234',
                var_from = '+19195554321',
                enqueued_time = '2022-06-16T13:15:07.160Z',
                call_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/calls/c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                call_timeout = 30,
                callback_timeout = 15,
                tag = 'My custom tag value',
                answer_method = 'POST',
                answer_url = 'https://myServer.example/bandwidth/webhooks/answer',
                answer_fallback_method = 'POST',
                answer_fallback_url = 'https://myFallbackServer.example/bandwidth/webhooks/answer',
                disconnect_method = 'POST',
                disconnect_url = 'https://myServer.example/bandwidth/webhooks/disconnect',
                username = 'mySecretUsername',
                password = 'mySecretPassword1!',
                fallback_username = 'mySecretUsername',
                fallback_password = 'mySecretPassword1!',
                priority = 5
            )
        else:
            return CreateCallResponse(
                application_id = '04e88489-df02-4e34-a0ee-27a91849555f',
                account_id = '9900000',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                to = '+19195551234',
                var_from = '+19195554321',
                call_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/calls/c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                answer_method = 'POST',
                answer_url = 'https://myServer.example/bandwidth/webhooks/answer',
                disconnect_method = 'POST',
        )
        """

    def testCreateCallResponse(self):
        """Test CreateCallResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
