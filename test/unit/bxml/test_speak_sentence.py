"""
test_speak_sentence.py

Unit tests for the <SpeakSentence> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import SpeakSentence


class TestSpeakSentence(unittest.TestCase):

    def setUp(self):
        self.speak_sentence = SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.',
            voice="julie"
        )

        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<SpeakSentence voice="julie">Hello. Your number is &lt;say-as interpret-as="telephone"&gt;asdf&lt;/say-as&gt;, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence>'
        assert(expected == self.speak_sentence.to_bxml())
