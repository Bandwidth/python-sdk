"""
test_stop_recording.py

Unit tests for the <StopRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml.verbs.stop_recording import StopRecording, Verb


class TestStopRecording(unittest.TestCase):

    def setUp(self):
        self.stop_recording = StopRecording()

    def test_instance(self):
        assert isinstance(self.stop_recording, StopRecording)
        assert isinstance(self.stop_recording, Verb)

    def test_to_bxml(self):
        expected = '<StopRecording />'
        assert expected == self.stop_recording.to_bxml()
