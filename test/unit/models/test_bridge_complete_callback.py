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

from bandwidth.models.bridge_complete_callback import BridgeCompleteCallback

class TestBridgeCompleteCallback(unittest.TestCase):
    """BridgeCompleteCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BridgeCompleteCallback:
        """Test BridgeCompleteCallback
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BridgeCompleteCallback`
        """
        model = BridgeCompleteCallback()
        if include_optional:
            return BridgeCompleteCallback(
                event_type = 'bridgeComplete',
                event_time = '2022-06-17T22:19:40.375Z',
                account_id = '9900000',
                application_id = '04e88489-df02-4e34-a0ee-27a91849555f',
                var_from = '+15555555555',
                to = '+15555555555',
                direction = 'inbound',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                call_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/calls/c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                enqueued_time = '2022-06-17T22:20Z',
                start_time = '2022-06-17T22:19:40.375Z',
                answer_time = '2022-06-17T22:20Z',
                tag = 'exampleTag',
                cause = 'busy',
                error_message = 'Call c-2a913f94-6a486f3a-3cae-4034-bcc3-f0c9fa77ca2f is already bridged with another call',
                error_id = '4642074b-7b58-478b-96e4-3a60955c6765'
            )
        else:
            return BridgeCompleteCallback(
        )
        """

    def testBridgeCompleteCallback(self):
        """Test BridgeCompleteCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
