"""
test_start_recording.py

Unit tests for the <StartRecording> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.start_recording import StartRecording


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.start_recording = StartRecording(
            recording_available_url = "example.com",
            recording_available_method = "POST",
            transcribe = "true",
            transcription_available_url = "transcription-example.com",
            transcription_available_method = "POST",
            username = "user",
            password = "pass",
            tag = "tag",
            file_format = "wav",
            multi_channel = "true"
        )
        self.test_verb = Verb(tag="test")
        

    def test_to_bxml(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<StartRecording fileFormat="wav" multiChannel="true" password="pass" recordingAvailableMethod="POST" recordingAvailableUrl="example.com" tag="tag" transcribe="true" transcriptionAvailableMethod="POST" transcriptionAvailableUrl="transcription-example.com" username="user" />'
        else:
            expected = '<StartRecording recordingAvailableUrl="example.com" recordingAvailableMethod="POST" transcribe="true" transcriptionAvailableUrl="transcription-example.com" transcriptionAvailableMethod="POST" username="user" password="pass" tag="tag" fileFormat="wav" multiChannel="true" />'
            
        assert(expected == self.start_recording.to_bxml())


    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.start_recording.add_verb(self.test_verb)