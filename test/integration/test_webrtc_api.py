"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


from array import array
import unittest

import bandwidth
from hamcrest import *
from bandwidth.api import participants_api, sessions_api
from bandwidth.exceptions import NotFoundException, UnauthorizedException
from bandwidth.model.create_participant_request import CreateParticipantRequest
from bandwidth.model.create_participant_response import CreateParticipantResponse
from bandwidth.model.publish_permissions_enum import PublishPermissionsEnum
from bandwidth.model.device_api_version_enum import DeviceApiVersionEnum
from bandwidth.model.participant import Participant
from bandwidth.model.session import Session
from bandwidth.model.subscriptions import Subscriptions
from bandwidth.model.participant_subscription import ParticipantSubscription
from test.utils.env_variables import *


class TestSessionsApi(unittest.TestCase):
    """SessionsApi unit test stubs"""

    def setUp(self):
        # API Client
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)
        self.sessions_api_instance = sessions_api.SessionsApi(api_client)
        self.participants_api_instance = participants_api.ParticipantsApi(api_client)
        self.account_id = BW_ACCOUNT_ID

        # Participant Properties
        self.callback_url = 'https://example.com/callback'
        self.publish_permissions = [
                PublishPermissionsEnum('AUDIO'),
                PublishPermissionsEnum('VIDEO')
            ]
        self.participant_tag = 'python integration participant tag'
        self.device_api_version = DeviceApiVersionEnum('V3')
        self.participant_id = ''

        # Participant Request
        self.create_participant_request = CreateParticipantRequest(
            callback_url=self.callback_url,
            publish_permissions=self.publish_permissions,
            tag=self.participant_tag,
            device_api_version=self.device_api_version
        )

        # Session Properties
        self.session_tag = 'python integration session tag'
        self.session_id = ''

        # Session Request
        self.session = Session(
            tag=self.session_tag
        )

        self.stream_aliases = ['python integration alias']

    def create_participant(self):
        """Test creating participant
        """
        response = self.participants_api_instance.create_participant(self.account_id, create_participant_request=self.create_participant_request, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))

        assert_that(response[0], instance_of(CreateParticipantResponse))
        assert_that(response[0], has_properties(
                'participant', instance_of(Participant),
                'participant', has_properties(
                    'device_api_version', self.device_api_version,
                    'id', instance_of(str),
                    'publish_permissions', contains_inanyorder(
                        PublishPermissionsEnum('AUDIO'),
                        PublishPermissionsEnum('VIDEO')),
                    'tag', self.participant_tag
                ),
            'token', instance_of(str)
        ))

        self.participant_id = response[0].participant.id
        
    def delete_participant(self):
        """Test deleting participant
        """
        response = self.participants_api_instance.delete_participant(self.account_id, self.participant_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(204))

    def get_participant(self):
        """Test getting participant
        """
        response = self.participants_api_instance.get_participant(self.account_id, self.participant_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))
        assert_that(response[0], instance_of(Participant))
        assert_that(response[0], has_properties(
            'device_api_version', self.device_api_version,
            'id', self.participant_id,
            'publish_permissions', contains_inanyorder(
                PublishPermissionsEnum('AUDIO'),
                PublishPermissionsEnum('VIDEO')),
            'sessions', [self.session_id],
            'subscriptions', has_properties(
                'participants', instance_of(list)
            ),
            'tag', self.participant_tag
        ))
    
    def add_participant_to_session(self):
        """Test adding participant to session
        """
        response = self.sessions_api_instance.add_participant_to_session(self.account_id, self.session_id, self.participant_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(204))
        

    def create_session(self):
        """Test creating session
        """
        response = self.sessions_api_instance.create_session(self.account_id, session=self.session, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))

        assert_that(response[0], instance_of(Session))
        assert_that(response[0], has_properties(
            'id', instance_of(str),
            'tag', self.session_tag,
            'participant_ids', instance_of(array),
            'participant_ids', empty()
        ))

        self.session_id = response[0].id

    def delete_session(self):
        """Test deleting session
        """
        response = self.sessions_api_instance.delete_session(self.account_id, self.session_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(204))

    def get_participant_subscriptions(self):
        """Test getting participant subscriptions
        """
        response = self.sessions_api_instance.get_participant_subscriptions(self.account_id, self.session_id, self.participant_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))

        assert_that(response[0], has_properties(
            'participants', instance_of(list),
            'session_id', self.session_id
        ))
        assert_that(response[0].participants[0], instance_of(ParticipantSubscription))
        assert_that(response[0].participants[0], has_properties(
            'participant_id', self.participant_id,
            'stream_aliases', self.stream_aliases
        ))

    def get_session(self):
        """Test getting session
        """
        response = self.sessions_api_instance.get_session(self.account_id, self.session_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))

        assert_that(response[0], has_properties(
            'id', self.session_id,
            'tag', self.session_tag,
            'participant_ids', contains_exactly(self.participant_id)
        ))

    def list_session_participants(self):
        """Test listing session participants
        """
        response = self.sessions_api_instance.list_session_participants(self.account_id, self.session_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(200))

        assert_that(response[0], instance_of(list))
        assert_that(response[0][0], instance_of(Participant))
        assert_that(response[0][0], has_properties(
            'device_api_version', self.device_api_version,
            'id', self.participant_id,
            'publish_permissions', contains_inanyorder(
                PublishPermissionsEnum('AUDIO'),
                PublishPermissionsEnum('VIDEO')),
            'sessions', [self.session_id],
            'tag', self.participant_tag
        ))

    def remove_participant_from_session(self):
        """Test removing participant from session
        """
        response = self.sessions_api_instance.remove_participant_from_session(self.account_id, self.session_id, self.participant_id, _return_http_data_only=False)

        assert_that(response[1], equal_to(204))

    def update_participant_subscriptions(self):
        """Test updating participant subscriptions
        """
        subscriptions = Subscriptions(
            session_id=self.session_id,
            participants=[
                ParticipantSubscription(
                    participant_id=self.participant_id,
                    stream_aliases=self.stream_aliases,
                )
            ],
        )

        response = self.sessions_api_instance.update_participant_subscriptions(self.account_id, self.session_id, self.participant_id, subscriptions=subscriptions, _return_http_data_only=False)

        assert_that(response[1], equal_to(204))

    def get_participant_unauthorized(self):
        """Test getting participant with unauthorized API client 
        """
        unauthorized_api_client = bandwidth.ApiClient()
        unauthorized_participants_api_instance = participants_api.ParticipantsApi(unauthorized_api_client)

        assert_that(calling(unauthorized_participants_api_instance.get_participant).with_args(
            self.account_id, self.participant_id, _return_http_data_only=False)), raises(UnauthorizedException)

    def get_participant_not_found(self):
        """Test getting nonexistent participant
        """
        assert_that(calling(self.participants_api_instance.get_participant).with_args(
            self.account_id, self.participant_id)), raises(NotFoundException)

    def _steps(self) -> None:
            call_order = ['create_participant', 'create_session', 'add_participant_to_session',
                          'get_session', 'list_session_participants', 'update_participant_subscriptions',
                          'get_participant_subscriptions', 'get_participant', 'remove_participant_from_session',
                          'delete_session', 'delete_participant', 'get_participant_unauthorized', 'get_participant_not_found']
            for name in call_order: 
                yield name, getattr(self, name)

    def test_steps(self) -> None:
        """Test each function from _steps.call_order in specified order
        """
        for name, step in self._steps():
            step()

if __name__ == '__main__':
    unittest.main()