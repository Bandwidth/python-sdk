"""
test_start_recording.py

Unit tests for the <StartRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StartRecording, Verb


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

    def test_instance(self):
        assert isinstance(self.start_recording, StartRecording)
        assert isinstance(self.start_recording, Verb)

    def test_to_bxml(self):
        expected = '<StartRecording recordingAvailableUrl="example.com" recordingAvailableMethod="POST" transcribe="True" transcriptionAvailableUrl="transcription-example.com" transcriptionAvailableMethod="POST" username="user" password="pass" tag="tag" fileFormat="wav" multiChannel="True" />'
        assert expected == self.start_recording.to_bxml()
