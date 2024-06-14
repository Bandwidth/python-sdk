"""
test_stop_recording.py

Unit tests for the <StopRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml.verbs.stop_recording import StopRecording


class TestStopRecording(unittest.TestCase):

    def setUp(self):
        self.stop_recording = StopRecording()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<StopRecording />'
        assert(expected == self.stop_recording.to_bxml())
