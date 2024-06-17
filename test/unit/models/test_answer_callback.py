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

from bandwidth.models.answer_callback import AnswerCallback

class TestAnswerCallback(unittest.TestCase):
    """AnswerCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnswerCallback:
        """Test AnswerCallback
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnswerCallback`
        """
        model = AnswerCallback()
        if include_optional:
            return AnswerCallback(
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
                machine_detection_result = bandwidth.models.machine_detection_result.machineDetectionResult(
                    value = 'answering-machine', 
                    duration = 'PT4.9891287S', )
            )
        else:
            return AnswerCallback(
        )
        """

    def testAnswerCallback(self):
        """Test AnswerCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
