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

from hamcrest import *
from test.utils.env_variables import *
from bandwidth import ApiClient, Configuration
from bandwidth.api.transcriptions_api import TranscriptionsApi
from bandwidth.models.call_transcription_metadata import CallTranscriptionMetadata
from bandwidth.models.call_transcription_response import CallTranscriptionResponse
from bandwidth.models.call_transcription_detected_language_enum import CallTranscriptionDetectedLanguageEnum
from bandwidth.models.call_transcription_track_enum import CallTranscriptionTrackEnum
from bandwidth.models.call_transcription import CallTranscription


class TestTranscriptionsApi(unittest.TestCase):
    """TranscriptionsApi unit test stubs"""

    def setUp(self) -> None:
        configuration = Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD,
            host='http://127.0.0.1:4010',
            ignore_operation_servers=True
        )
        api_client = ApiClient(configuration)
        self.transcriptions_api_instance = TranscriptionsApi(api_client)

        self.call_id = "c-abc123"
        self.transcription_id = "t-abc123"

    def test_list_real_time_transcriptions(self) -> None:
        """Test case for list_real_time_transcriptions

        Enumerate transcriptions made with StartTranscription
        """
        response = self.transcriptions_api_instance.list_real_time_transcriptions_with_http_info(
            BW_ACCOUNT_ID, self.call_id)

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(list))
        assert_that(response.data[0], instance_of(CallTranscriptionMetadata))
        assert_that(response.data[0].transcription_id, instance_of(str))
        assert_that(response.data[0].transcription_url, instance_of(str))
        assert_that(response.data[0].transcription_name, instance_of(str))

    def test_get_real_time_transcription(self) -> None:
        """Test case for get_real_time_transcription

        Retrieve a specific transcription
        """
        response = self.transcriptions_api_instance.get_real_time_transcription_with_http_info(
            BW_ACCOUNT_ID, self.call_id, self.transcription_id)

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(CallTranscriptionResponse))
        assert_that(response.data.account_id, has_length(7))
        assert_that(response.data.call_id, has_length(47))
        assert_that(response.data.transcription_id, instance_of(str))
        assert_that(response.data.tracks, instance_of(list))
        assert_that(response.data.tracks[0], instance_of(CallTranscription))
        assert_that(response.data.tracks[0].detected_language, is_in(CallTranscriptionDetectedLanguageEnum))
        assert_that(response.data.tracks[0].track, is_in(CallTranscriptionTrackEnum))
        assert_that(response.data.tracks[0].transcript, instance_of(str))
        assert_that(response.data.tracks[0].confidence, instance_of(float))

    def test_delete_real_time_transcription(self) -> None:
        """Test case for delete_real_time_transcription

        Delete a specific transcription
        """
        response = self.transcriptions_api_instance.delete_real_time_transcription_with_http_info(
            BW_ACCOUNT_ID, self.call_id, self.transcription_id)

        assert_that(response.status_code, equal_to(200))


if __name__ == '__main__':
    unittest.main()
