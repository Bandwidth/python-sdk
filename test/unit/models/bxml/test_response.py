"""
test_response.py

Unit tests for Response Model

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Response, Redirect, SpeakSentence


class TestResponse(unittest.TestCase):

    def setUp(self):
        self.response = Response()

    def test_instance(self):
        assert isinstance(self.response, Response)

    def test_response_init(self):
        """Test initializing the <Response> root
        """
        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<Response />"
        assert self.response.to_bxml() == expected_bxml

    def test_ssml_unescaped_but_other_attributes_untouched(self):
        """SSML in <SpeakSentence> text is un-escaped; escaped characters in other elements' attributes are not
        """
        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<Response><Redirect redirectUrl=\"https://example.com/a?info=&lt;https://example.com/c.pem&gt;\" /><SpeakSentence voice=\"julie\" gender=\"female\" locale=\"en_US\">Hello. Your number is <say-as interpret-as=\"telephone\">asdf</say-as>, lets play a game.</SpeakSentence></Response>"
        self.response.add_verb(Redirect(redirect_url="https://example.com/a?info=<https://example.com/c.pem>"))
        self.response.add_verb(SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game.',
            voice="julie",
            gender="female",
            locale="en_US"
        ))
        assert expected_bxml == self.response.to_bxml()

    def test_empty_speak_sentence_does_not_swallow_following_verbs(self):
        """A <SpeakSentence> with no text must not capture the verbs that follow it
        """
        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<Response><SpeakSentence /><Redirect redirectUrl=\"https://example.com/a?info=&lt;b&gt;\" /><SpeakSentence>hi <break/></SpeakSentence></Response>"
        self.response.add_verb(SpeakSentence(text=""))
        self.response.add_verb(Redirect(redirect_url="https://example.com/a?info=<b>"))
        self.response.add_verb(SpeakSentence(text="hi <break/>"))
        assert expected_bxml == self.response.to_bxml()
