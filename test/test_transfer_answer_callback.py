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
from bandwidth.models.transfer_answer_callback import TransferAnswerCallback  # noqa: E501
from bandwidth.rest import ApiException

class TestTransferAnswerCallback(unittest.TestCase):
    """TransferAnswerCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransferAnswerCallback
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferAnswerCallback`
        """
        model = bandwidth.models.transfer_answer_callback.TransferAnswerCallback()  # noqa: E501
        if include_optional :
            return TransferAnswerCallback(
                event_type = 'bridgeComplete', 
                event_time = '2022-06-17T22:19:40.375Z', 
                account_id = '920012', 
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
                transfer_caller_id = '+15555555555', 
                transfer_to = '+15555555555)'
            )
        else :
            return TransferAnswerCallback(
        )
        """

    def testTransferAnswerCallback(self):
        """Test TransferAnswerCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
