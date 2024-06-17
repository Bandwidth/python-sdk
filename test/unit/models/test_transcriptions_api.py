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

from bandwidth.api.transcriptions_api import TranscriptionsApi


class TestTranscriptionsApi(unittest.TestCase):
    """TranscriptionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TranscriptionsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_real_time_transcription(self) -> None:
        """Test case for delete_real_time_transcription

        Delete a specific transcription
        """
        pass

    def test_get_real_time_transcription(self) -> None:
        """Test case for get_real_time_transcription

        Retrieve a specific transcription
        """
        pass

    def test_list_real_time_transcriptions(self) -> None:
        """Test case for list_real_time_transcriptions

        Enumerate transcriptions made with StartTranscription
        """
        pass


if __name__ == '__main__':
    unittest.main()