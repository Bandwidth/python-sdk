"""
test_speak_sentence.py

Unit tests for the <SpeakSentence> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import SpeakSentence, Response


class TestSpeakSentence(unittest.TestCase):

    def setUp(self):
        self.speak_sentence = SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.',
            voice="julie"
        )

        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<SpeakSentence voice="julie">Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence>'
        assert expected == self.speak_sentence.to_bxml()

    def test_to_bxml_within_response(self):
        expected = '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n<Response><SpeakSentence voice="julie">Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence></Response>'
        response = Response()
        response.add_verb(self.speak_sentence)
        assert expected == response.to_bxml()
