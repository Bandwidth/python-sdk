"""
test_speak_sentence.py

Unit tests for the <SpeakSentence> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs import SpeakSentence

class TestSpeakSentence(unittest.TestCase):
    
    def setUp(self):
        self.speak_sentence = SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.'
        )
        
        self.test_verb = Verb(tag="test")
    
    def test_to_bxml(self):
        expected = '<SpeakSentence>Hello. Your number is &lt;say-as interpret-as="telephone"&gt;asdf&lt;/say-as&gt;, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence>'
        assert(expected == self.speak_sentence.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.speak_sentence.add_verb(self.test_verb)
