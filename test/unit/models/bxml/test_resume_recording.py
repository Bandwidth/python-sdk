"""
test_resume_recording.py

Unit tests for the <ResumeRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import ResumeRecording


class TestResumeRecording(unittest.TestCase):

    def setUp(self):
        self.resume_recording = ResumeRecording()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<ResumeRecording />'
        assert(expected == self.resume_recording.to_bxml())
