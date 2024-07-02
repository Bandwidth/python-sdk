"""
test_stop_transcription.py

Unit tests for the <StopTranscription> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StopTranscription, Verb


class TestStopTranscription(unittest.TestCase):
    def setUp(self) -> None:
        self.stop_transcription = StopTranscription(
            name="transcription1"
        )

    def test_instance(self):
        assert isinstance(self.stop_transcription, StopTranscription)
        assert isinstance(self.stop_transcription, Verb)

    def test_to_bxml(self):
        expected = '<StopTranscription name="transcription1" />'
        assert expected == self.stop_transcription.to_bxml()
