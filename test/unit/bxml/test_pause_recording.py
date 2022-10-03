"""
test_pause_recording.py

Unit tests for the <PauseRecording> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.pause_recording import PauseRecording


class TestTag(unittest.TestCase):

    def setUp(self):
        self.pause_recording = PauseRecording()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<PauseRecording />'
        assert(expected == self.pause_recording.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.pause_recording.add_verb(self.test_verb)

