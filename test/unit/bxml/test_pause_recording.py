"""
test_pause_recording.py

Unit tests for the <PauseRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import PauseRecording


class TestPauseRecording(unittest.TestCase):

    def setUp(self):
        self.pause_recording = PauseRecording()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<PauseRecording />'
        assert(expected == self.pause_recording.to_bxml())
