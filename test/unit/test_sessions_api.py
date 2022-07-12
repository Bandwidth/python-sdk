"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import bandwidth
from bandwidth.api.sessions_api import SessionsApi  # noqa: E501


class TestSessionsApi(unittest.TestCase):
    """SessionsApi unit test stubs"""

    def setUp(self):
        self.api = SessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_participant_to_session(self):
        """Test case for add_participant_to_session

        Add Participant to Session  # noqa: E501
        """
        pass

    def test_create_session(self):
        """Test case for create_session

        Create Session  # noqa: E501
        """
        pass

    def test_delete_session(self):
        """Test case for delete_session

        Delete Session  # noqa: E501
        """
        pass

    def test_get_participant_subscriptions(self):
        """Test case for get_participant_subscriptions

        Get Participant Subscriptions  # noqa: E501
        """
        pass

    def test_get_session(self):
        """Test case for get_session

        Get Session  # noqa: E501
        """
        pass

    def test_list_session_participants(self):
        """Test case for list_session_participants

        List Participants in Session  # noqa: E501
        """
        pass

    def test_remove_participant_from_session(self):
        """Test case for remove_participant_from_session

        Remove Participant from Session  # noqa: E501
        """
        pass

    def test_update_participant_subscriptions(self):
        """Test case for update_participant_subscriptions

        Update Participant Subscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()