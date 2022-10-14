"""
test_resume_recording.py

Unit tests for the <ResumeRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.resume_recording import ResumeRecording


class TestResumeRecording(unittest.TestCase):

    def setUp(self):
        self.resume_recording = ResumeRecording()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<ResumeRecording />'
        assert(expected == self.resume_recording.to_bxml())
