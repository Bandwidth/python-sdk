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
from datetime import datetime

from bandwidth.models.transfer_answer_callback import TransferAnswerCallback

class TestTransferAnswerCallback(unittest.TestCase):
    """TransferAnswerCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferAnswerCallback:
        """Test TransferAnswerCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return TransferAnswerCallback(
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
                transfer_caller_id = '+15555555555',
                transfer_to = '+15555555555'
            )
        else:
            return TransferAnswerCallback(
        )

    def testTransferAnswerCallback(self):
        """Test TransferAnswerCallback"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, TransferAnswerCallback)
        assert instance.event_type == 'bridgeComplete'
        assert isinstance(instance.event_time, datetime)
        assert instance.account_id == '9900000'
        assert instance.application_id == '04e88489-df02-4e34-a0ee-27a91849555f'
        assert instance.var_from == '+15555555555'
        assert instance.to == '+15555555555'
        assert instance.direction == 'inbound'
        assert instance.call_id == 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85'
        assert instance.call_url == 'https://voice.bandwidth.com/api/v2/accounts/9900000/calls/c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85'
        assert isinstance(instance.enqueued_time, datetime)
        assert isinstance(instance.start_time, datetime)
        assert isinstance(instance.answer_time, datetime)
        assert instance.tag == 'exampleTag'
        assert instance.transfer_caller_id == '+15555555555'
        assert instance.transfer_to == '+15555555555'


if __name__ == '__main__':
    unittest.main()
