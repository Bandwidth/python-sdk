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

from bandwidth.api.conferences_api import ConferencesApi


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConferencesApi()

    def tearDown(self) -> None:
        pass

    def test_download_conference_recording(self) -> None:
        """Test case for download_conference_recording

        Download Conference Recording
        """
        pass

    def test_get_conference(self) -> None:
        """Test case for get_conference

        Get Conference Information
        """
        pass

    def test_get_conference_member(self) -> None:
        """Test case for get_conference_member

        Get Conference Member
        """
        pass

    def test_get_conference_recording(self) -> None:
        """Test case for get_conference_recording

        Get Conference Recording Information
        """
        pass

    def test_list_conference_recordings(self) -> None:
        """Test case for list_conference_recordings

        Get Conference Recordings
        """
        pass

    def test_list_conferences(self) -> None:
        """Test case for list_conferences

        Get Conferences
        """
        pass

    def test_update_conference(self) -> None:
        """Test case for update_conference

        Update Conference
        """
        pass

    def test_update_conference_bxml(self) -> None:
        """Test case for update_conference_bxml

        Update Conference BXML
        """
        pass

    def test_update_conference_member(self) -> None:
        """Test case for update_conference_member

        Update Conference Member
        """
        pass


if __name__ == '__main__':
    unittest.main()