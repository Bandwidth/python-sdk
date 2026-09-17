"""
test_record.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Record, Verb


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record(
            record_complete_url="example.com/completeurl",
            record_complete_method="POST",
            record_complete_fallback_url="backupexample.com/completeurl",
            record_complete_fallback_method="POST",
            recording_available_url="example.com/availableurl",
            recording_available_method="POST",
            transcribe=True,
            transcription_available_url="example.com/transcriptionurl",
            transcription_available_method="POST",
            username="user",
            password="pass",
            fallback_username="user",
            fallback_password="pass",
            tag="tag",
            terminating_digits="#",
            max_duration=10,
            silence_timeout="5",
            file_format="wav",
            detect_language=True,
            recording_name="recording1"
        )

    def test_instance(self):
        assert isinstance(self.record, Record)
        assert isinstance(self.record, Verb)

    def test_to_bxml(self):
        expected = '<Record recordCompleteUrl="example.com/completeurl" recordCompleteMethod="POST" recordCompleteFallbackUrl="backupexample.com/completeurl" recordCompleteFallbackMethod="POST" recordingAvailableUrl="example.com/availableurl" recordingAvailableMethod="POST" transcribe="true" detectLanguage="true" transcriptionAvailableUrl="example.com/transcriptionurl" transcriptionAvailableMethod="POST" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" terminatingDigits="#" maxDuration="10" silenceTimeout="5" fileFormat="wav" recordingName="recording1" />'
        assert expected == self.record.to_bxml()
