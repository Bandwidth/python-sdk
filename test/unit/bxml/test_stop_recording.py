"""
test_stop_recording.py

Unit tests for the <StopRecording> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.stop_recording import StopRecording


class TestTag(unittest.TestCase):
    
    def setUp(self):
        self.stop_recording = StopRecording()
        self.test_verb = Verb(tag="test")
    
    def test_to_bxml(self):
        expected = '<StopRecording />'
        assert(expected == self.stop_recording.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.stop_recording.add_verb(self.test_verb)
