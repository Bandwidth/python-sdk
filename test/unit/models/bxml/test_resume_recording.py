"""
test_resume_recording.py

Unit tests for the <ResumeRecording> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import ResumeRecording, Verb


class TestResumeRecording(unittest.TestCase):

    def setUp(self):
        self.resume_recording = ResumeRecording()

    def test_instance(self):
        assert isinstance(self.resume_recording, ResumeRecording)
        assert isinstance(self.resume_recording, Verb)

    def test_to_bxml(self):
        expected = '<ResumeRecording />'
        assert expected == self.resume_recording.to_bxml()
