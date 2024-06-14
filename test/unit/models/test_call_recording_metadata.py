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
from bandwidth.models.call_recording_metadata import CallRecordingMetadata  # noqa: E501
from bandwidth.rest import ApiException

class TestCallRecordingMetadata(unittest.TestCase):
    """CallRecordingMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CallRecordingMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CallRecordingMetadata`
        """
        model = bandwidth.models.call_recording_metadata.CallRecordingMetadata()  # noqa: E501
        if include_optional :
            return CallRecordingMetadata(
                application_id = '04e88489-df02-4e34-a0ee-27a91849555f',
                account_id = '920012',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                parent_call_id = 'c-95ac8d6e-1a31c52e-b38f-4198-93c1-51633ec68f8d',
                recording_id = 'r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833',
                to = '+15555555555',
                var_from = '+15555555555',
                transfer_caller_id = '+15555555555',
                transfer_to = '+15555555555)',
                duration = 'PT13.67S',
                direction = 'inbound',
                channels = 1,
                start_time = '2022-06-17T22:19:40.375Z',
                end_time = '2022-06-17T22:20Z',
                file_format = 'wav',
                status = 'completed',
                media_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/conferences/conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9/recordings/r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833/media',
                transcription = bandwidth.models.transcription_metadata.transcriptionMetadata(
                    id = 't-387bd648-18f3-4823-9d16-746bca0003c9',
                    status = 'completed',
                    completed_time = '2022-06-13T18:46:29.715Z',
                    url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/calls/c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85/recordings/r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85/transcription', )
            )
        else :
            return CallRecordingMetadata(
        )
        """

    def testCallRecordingMetadata(self):
        """Test CallRecordingMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
