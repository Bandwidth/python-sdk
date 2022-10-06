"""
test_conference.py

Unit tests for the <Conference> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs import *

class TestConference(unittest.TestCase):

    def setUp(self):
        self.play_audio = PlayAudio(
            audio_uri="https://audio.url/audio1.wav"
        )

        self.speak_sentence = SpeakSentence(
            text='Hello there.'
        )
        self.start_recording = StartRecording(
            recording_available_url = "example.com",
            recording_available_method = "POST",
            username = "user",
            password = "pass",
            tag = "tag",
            file_format = "wav",
            multi_channel = "true"
        )

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
            audio_and_recording_verbs=[self.play_audio, self.start_recording]
        )

    def test_to_bxml(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<Conference callIdsToCoach="example-call-id" callbackTimeout="5" conferenceEventFallbackMethod="POST" conferenceEventFallbackUrl="backupexample.com/eventurl" conferenceEventMethod="POST" conferenceEventUrl="example.com/eventurl" fallbackPassword="pass" fallbackUsername="user" hold="false" mute="true" password="pass" tag="tag" username="user">conf1<PlayAudio>https://audio.url/audio1.wav</PlayAudio><StartRecording fileFormat="wav" multiChannel="true" password="pass" recordingAvailableMethod="POST" recordingAvailableUrl="example.com" tag="tag" username="user" /></Conference>'
        else:
            expected = '<Conference mute="true" hold="false" callIdsToCoach="example-call-id" conferenceEventUrl="example.com/eventurl" conferenceEventMethod="POST" conferenceEventFallbackUrl="backupexample.com/eventurl" conferenceEventFallbackMethod="POST" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" callbackTimeout="5">conf1<PlayAudio>https://audio.url/audio1.wav</PlayAudio><StartRecording recordingAvailableUrl="example.com" recordingAvailableMethod="POST" username="user" password="pass" tag="tag" fileFormat="wav" multiChannel="true" /></Conference>'
        assert(expected == self.conference.to_bxml())

    def test_add_verb(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<Conference callIdsToCoach="example-call-id" callbackTimeout="5" conferenceEventFallbackMethod="POST" conferenceEventFallbackUrl="backupexample.com/eventurl" conferenceEventMethod="POST" conferenceEventUrl="example.com/eventurl" fallbackPassword="pass" fallbackUsername="user" hold="false" mute="true" password="pass" tag="tag" username="user">conf1<PlayAudio>https://audio.url/audio1.wav</PlayAudio><StartRecording fileFormat="wav" multiChannel="true" password="pass" recordingAvailableMethod="POST" recordingAvailableUrl="example.com" tag="tag" username="user" /><SpeakSentence>Hello there.</SpeakSentence></Conference>'
        else:
            expected = '<Conference mute="true" hold="false" callIdsToCoach="example-call-id" conferenceEventUrl="example.com/eventurl" conferenceEventMethod="POST" conferenceEventFallbackUrl="backupexample.com/eventurl" conferenceEventFallbackMethod="POST" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" callbackTimeout="5">conf1<PlayAudio>https://audio.url/audio1.wav</PlayAudio><StartRecording recordingAvailableUrl="example.com" recordingAvailableMethod="POST" username="user" password="pass" tag="tag" fileFormat="wav" multiChannel="true" /><SpeakSentence>Hello there.</SpeakSentence></Conference>'
        self.conference.add_verb(self.speak_sentence)
        assert(expected == self.conference.to_bxml())
