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

from bandwidth.models.multi_channel_action import MultiChannelAction
from bandwidth.models.rbm_action_base import RbmActionBase
from bandwidth.models.rbm_action_dial import RbmActionDial
from bandwidth.models.rbm_action_open_url import RbmActionOpenUrl
from bandwidth.models.rbm_action_view_location import RbmActionViewLocation
from bandwidth.models.multi_channel_action_calendar_event import MultiChannelActionCalendarEvent

class TestMultiChannelAction(unittest.TestCase):
    """MultiChannelAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiChannelAction:
        """Test MultiChannelAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

    def testMultiChannelAction(self):
        """Test MultiChannelAction"""
        model_rbm_action_base = MultiChannelAction(RbmActionBase(
            type='REPLY',
            text='Hello world',
            post_back_data='[B@32298473'
        ))
        model_rbm_action_dial = MultiChannelAction(RbmActionDial(
            type='DIAL_PHONE',
            text='Hello world',
            post_back_data='[B@32298473',
            phone_number='1234567890'
        ))
        model_rbm_action_view_location = MultiChannelAction(RbmActionViewLocation(
            type='SHOW_LOCATION',
            text='Hello world',
            post_back_data='[B@32298473',
            latitude='37.7749',
            longitude='-122.4194',
            label='San Francisco'
        ))
        model_multi_channel_action_calendar_event = MultiChannelAction(MultiChannelActionCalendarEvent(
            type = 'CREATE_CALENDAR_EVENT',
            text = 'Hello world',
            post_back_data = 'U0dWc2JHOGdkMjl5YkdRPQ==',
            title = 'Meeting with John',
            start_time = '2022-09-14T18:20:16Z',
            end_time = '2022-09-14T18:20:16Z',
            description = 'Discuss the new project'
        ))
        model_rbm_action_open_url = MultiChannelAction(RbmActionOpenUrl(
            type='OPEN_URL',
            text='Hello world',
            post_back_data='[B@32298473',
            url='https://www.example.com'
        ))

        assert model_rbm_action_base is not None
        assert isinstance(model_rbm_action_base, MultiChannelAction)
        assert isinstance(model_rbm_action_base.actual_instance, RbmActionBase)
        assert model_rbm_action_dial is not None
        assert isinstance(model_rbm_action_dial, MultiChannelAction)
        assert isinstance(model_rbm_action_dial.actual_instance, RbmActionDial)
        assert model_rbm_action_view_location is not None
        assert isinstance(model_rbm_action_view_location, MultiChannelAction)
        assert isinstance(model_rbm_action_view_location.actual_instance, RbmActionViewLocation)
        assert model_multi_channel_action_calendar_event is not None
        assert isinstance(model_multi_channel_action_calendar_event, MultiChannelAction)
        assert isinstance(model_multi_channel_action_calendar_event.actual_instance, MultiChannelActionCalendarEvent)
        assert model_rbm_action_open_url is not None
        assert isinstance(model_rbm_action_open_url, MultiChannelAction)
        assert isinstance(model_rbm_action_open_url.actual_instance, RbmActionOpenUrl)
        

if __name__ == '__main__':
    unittest.main()
