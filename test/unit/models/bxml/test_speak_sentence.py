"""
test_speak_sentence.py

Unit tests for the <SpeakSentence> BXML verb

@copyright Bandwidth Inc.
"""
import unittest
import xml.etree.ElementTree as ET

from bandwidth.models.bxml import SpeakSentence, Response, Verb, Redirect


class TestSpeakSentence(unittest.TestCase):

    def setUp(self):
        self.speak_sentence = SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.',
            voice="julie",
            gender="female",
            locale="en_US"
        )

    def test_instance(self):
        assert isinstance(self.speak_sentence, SpeakSentence)
        assert isinstance(self.speak_sentence, Verb)

    def test_to_bxml(self):
        expected = '<SpeakSentence voice="julie" gender="female" locale="en_US">Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence>'
        assert expected == self.speak_sentence.to_bxml()

    def test_to_bxml_within_response(self):
        expected = '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n<Response><SpeakSentence voice="julie" gender="female" locale="en_US">Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence></Response>'
        response = Response()
        response.add_verb(self.speak_sentence)
        assert expected == response.to_bxml()

    def test_ssml_unescaped_but_other_attributes_untouched(self):
        redirect = Redirect(redirect_url="https://example.com/a?info=<https://example.com/c.pem>")
        response = Response()
        response.add_verb(redirect)
        response.add_verb(self.speak_sentence)
        bxml = response.to_bxml()
        assert 'info=&lt;https://example.com/c.pem&gt;' in bxml
        assert '<say-as interpret-as="telephone">asdf</say-as>' in bxml
        ET.fromstring(bxml)

    def test_empty_speak_sentence_does_not_swallow_following_verbs(self):
        response = Response()
        response.add_verb(SpeakSentence(text=""))
        response.add_verb(Redirect(redirect_url="https://example.com/a?info=<b>"))
        response.add_verb(SpeakSentence(text="hi <break/>"))
        bxml = response.to_bxml()
        assert 'info=&lt;b&gt;' in bxml
        assert 'hi <break/>' in bxml
