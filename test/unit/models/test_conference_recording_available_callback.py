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

from bandwidth.models.conference_recording_available_callback import ConferenceRecordingAvailableCallback

class TestConferenceRecordingAvailableCallback(unittest.TestCase):
    """ConferenceRecordingAvailableCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceRecordingAvailableCallback:
        """Test ConferenceRecordingAvailableCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return ConferenceRecordingAvailableCallback(
                event_type = 'bridgeComplete',
                event_time = '2022-06-17T22:19:40.375Z',
                conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9',
                name = 'my-conference-name',
                account_id = '9900000',
                recording_id = 'r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833',
                channels = 1,
                start_time = '2022-06-17T22:19:40.375Z',
                end_time = '2022-06-17T22:20Z',
                duration = 'PT13.67S',
                file_format = 'wav',
                media_url = 'https://voice.bandwidth.com/api/v2/accounts/9900000/conferences/conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9/recordings/r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833/media',
                tag = 'exampleTag',
                status = 'completed'
            )
        else:
            return ConferenceRecordingAvailableCallback(
        )

    def testConferenceRecordingAvailableCallback(self):
        """Test ConferenceRecordingAvailableCallback"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, ConferenceRecordingAvailableCallback)
        assert instance.event_type == 'bridgeComplete'
        assert isinstance(instance.event_time, datetime)
        assert instance.conference_id == 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9'
        assert instance.name == 'my-conference-name'
        assert instance.account_id == '9900000'
        assert instance.recording_id == 'r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833'
        assert instance.channels == 1
        assert isinstance(instance.start_time, datetime)
        assert isinstance(instance.end_time, datetime)
        assert instance.duration == 'PT13.67S'
        assert instance.file_format == 'wav'
        assert instance.media_url == 'https://voice.bandwidth.com/api/v2/accounts/9900000/conferences/conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9/recordings/r-fbe05094-9fd2afe9-bf5b-4c68-820a-41a01c1c5833/media'
        assert instance.tag == 'exampleTag'
        assert instance.status == 'completed'

if __name__ == '__main__':
    unittest.main()
