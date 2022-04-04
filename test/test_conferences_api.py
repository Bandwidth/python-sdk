"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import bandwidth
from bandwidth.api.conferences_api import ConferencesApi  # noqa: E501


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self):
        self.api = ConferencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_conference_recording(self):
        """Test case for download_conference_recording

        Download Conference Recording  # noqa: E501
        """
        pass

    def test_get_conference(self):
        """Test case for get_conference

        Get Conference Information  # noqa: E501
        """
        pass

    def test_get_conference_member(self):
        """Test case for get_conference_member

        Get Conference Member  # noqa: E501
        """
        pass

    def test_get_conference_recording(self):
        """Test case for get_conference_recording

        Get Conference Recording Information  # noqa: E501
        """
        pass

    def test_get_conference_recordings(self):
        """Test case for get_conference_recordings

        Get Conference Recordings  # noqa: E501
        """
        pass

    def test_get_conferences(self):
        """Test case for get_conferences

        Get Conferences  # noqa: E501
        """
        pass

    def test_modify_conference(self):
        """Test case for modify_conference

        Update Conference  # noqa: E501
        """
        pass

    def test_modify_conference_member(self):
        """Test case for modify_conference_member

        Update Conference Member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
