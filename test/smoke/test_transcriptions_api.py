"""
Integration test for Bandwidth's Voice Transcriptions API
"""
import unittest

from bandwidth import ApiClient, Configuration
from bandwidth.api.transcriptions_api import TranscriptionsApi


class TestTranscriptionsApi(unittest.TestCase):
    """TranscriptionsApi integration Test"""

    def setUp(self) -> None:
        configuration = Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = ApiClient(configuration)

        self.calls_api_instance = calls_api.CallsApi(api_client)
        self.transcriptions_api_instance = transcriptions_api.TranscriptionsApi(api_client)

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
