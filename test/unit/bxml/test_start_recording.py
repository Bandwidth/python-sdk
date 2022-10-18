"""
test_start_recording.py

Unit tests for the <StartRecording> BXML verb

@copyright Bandwidth Inc.
"""
import os
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.start_recording import StartRecording


class TestStartRecording(unittest.TestCase):

    def setUp(self):
        self.start_recording = StartRecording(
            recording_available_url = "example.com",
            recording_available_method = "POST",
            transcribe = True,
            transcription_available_url = "transcription-example.com",
            transcription_available_method = "POST",
            username = "user",
            password = "pass",
            tag = "tag",
            file_format = "wav",
            multi_channel = True
        )
        self.test_verb = Verb(tag="test")


    def test_to_bxml(self):
        expected = '<StartRecording recordingAvailableUrl="example.com" recordingAvailableMethod="POST" transcribe="True" transcriptionAvailableUrl="transcription-example.com" transcriptionAvailableMethod="POST" username="user" password="pass" tag="tag" fileFormat="wav" multiChannel="True" />'
        assert(expected == self.start_recording.to_bxml())
