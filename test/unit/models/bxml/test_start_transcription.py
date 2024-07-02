"""
test_start_transcription.py

Unit tests for the <StartTranscription> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StartTranscription, CustomParam, Verb, NestableVerb


class TestStartTranscription(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_param1 = CustomParam(
            name="name1",
            value="value1"
        )

        self.custom_param2 = CustomParam(
            name="name2",
            value="value2"
        )

        self.start_transcription = StartTranscription(
            name="transcription1",
            tracks="both",
            transcription_event_url="eventurl.com",
            transcription_event_method="POST",
            username="user",
            password="pass",
            destination="testurl.com",
            stabilized=True,
            custom_params=[self.custom_param1]
        )

    def test_instance(self):
        assert isinstance(self.start_transcription, StartTranscription)
        assert isinstance(self.start_transcription, NestableVerb)
        assert isinstance(self.start_transcription, Verb)

    def test_to_bxml(self):
        expected = '<StartTranscription name="transcription1" tracks="both" transcriptionEventUrl="eventurl.com" transcriptionEventMethod="POST" username="user" password="pass" destination="testurl.com" stabilized="True"><CustomParam name="name1" value="value1" /></StartTranscription>'
        assert expected == self.start_transcription.to_bxml()

    def test_add_verb(self):
        expected = '<StartTranscription name="transcription1" tracks="both" transcriptionEventUrl="eventurl.com" transcriptionEventMethod="POST" username="user" password="pass" destination="testurl.com" stabilized="True"><CustomParam name="name1" value="value1" /><CustomParam name="name2" value="value2" /></StartTranscription>'
        self.start_transcription.add_verb(self.custom_param2)
        assert expected == self.start_transcription.to_bxml()
