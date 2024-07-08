"""
test_pause_recording.py

Unit tests for the <PauseRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import PauseRecording, Verb


class TestPauseRecording(unittest.TestCase):

    def setUp(self):
        self.pause_recording = PauseRecording()

    def test_instance(self):
        assert isinstance(self.pause_recording, PauseRecording)
        assert isinstance(self.pause_recording, Verb)

    def test_to_bxml(self):
        expected = '<PauseRecording />'
        assert expected == self.pause_recording.to_bxml()
