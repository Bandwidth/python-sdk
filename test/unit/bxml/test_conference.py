"""
test_conference.py

Unit tests for the <Conference> BXML verb

@copyright Bandwidth Inc.
"""
import os
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs import Conference


class TestConference(unittest.TestCase):

    def setUp(self):
        self.conference = Conference(
            name="conf1",
            mute = "true",
            hold = "false",
            call_ids_to_coach = "example-call-id",
            conference_event_url = "example.com/eventurl",
            conference_event_method = "POST",
            conference_event_fallback_url = "backupexample.com/eventurl",
            conference_event_fallback_method = "POST",
            username = "user",
            password = "pass",
            fallback_username = "user",
            fallback_password = "pass",
            tag = "tag",
            callback_timeout = "5",
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Conference name="conf1" mute="true" hold="false" callIdsToCoach="example-call-id" conferenceEventUrl="example.com/eventurl" conferenceEventMethod="POST" conferenceEventFallbackUrl="backupexample.com/eventurl" conferenceEventFallbackMethod="POST" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" callbackTimeout="5" />'
        assert(expected == self.conference.to_bxml())
