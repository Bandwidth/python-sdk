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
from bandwidth.models.conference_recording_metadata import ConferenceRecordingMetadata  # noqa: E501
from bandwidth.rest import ApiException

class TestConferenceRecordingMetadata(unittest.TestCase):
    """ConferenceRecordingMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConferenceRecordingMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceRecordingMetadata`
        """
        model = bandwidth.models.conference_recording_metadata.ConferenceRecordingMetadata()  # noqa: E501
        if include_optional :
            return ConferenceRecordingMetadata(
                account_id = '920012',
                conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9',
                name = 'my-conference-name',
                recording_id = 'r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833',
                duration = 'PT13.67S',
                channels = 1,
                start_time = '2022-06-17T22:19:40.375Z',
                end_time = '2022-06-17T22:20Z',
                file_format = 'wav',
                status = 'completed',
                media_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/conferences/conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9/recordings/r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833/media'
            )
        else :
            return ConferenceRecordingMetadata(
        )
        """

    def testConferenceRecordingMetadata(self):
        """Test ConferenceRecordingMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
