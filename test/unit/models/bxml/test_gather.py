"""
test_gather.py

Unit tests for the <Gather> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import PlayAudio, SpeakSentence, Gather, Verb, NestableVerb


class TestGather(unittest.TestCase):

    def setUp(self):
        self.play_audio = PlayAudio(
            audio_uri="https://audio.url/audio1.wav",
            username="user",
            password="pass"
        )

        self.speak_sentence = SpeakSentence(
            text='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.'
        )

        self.gather = Gather(
            gather_url="test.com",
            gather_method="POST",
            gather_fallback_url= "fallback-test.com",
            gather_fallback_method="GET",
            username="user",
            password="pass",
            fallback_username="user",
            fallback_password="pass",
            tag = "tag",
            terminating_digits = "2",
            max_digits = 5,
            inter_digit_timeout = 1,
            first_digit_timeout = 3,
            repeat_count = 2,
            audio_verbs=[self.play_audio]
        )

    def test_instance(self):
        assert isinstance(self.gather, Gather)
        assert isinstance(self.gather, NestableVerb)
        assert isinstance(self.gather, Verb)

    def test_defaults(self):
        gather = Gather(
            audio_verbs=[self.play_audio]
        )
        expected = '<Gather><PlayAudio username="user" password="pass">https://audio.url/audio1.wav</PlayAudio></Gather>'
        assert expected == gather.to_bxml()

    def test_to_bxml(self):
        expected = '<Gather gatherUrl="test.com" gatherMethod="POST" gatherFallbackUrl="fallback-test.com" gatherFallbackMethod="GET" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" terminatingDigits="2" maxDigits="5" interDigitTimeout="1" firstDigitTimeout="3" repeatCount="2"><PlayAudio username="user" password="pass">https://audio.url/audio1.wav</PlayAudio></Gather>'
        assert expected == self.gather.to_bxml()

    def test_add_verb(self):
        expected = '<Gather gatherUrl="test.com" gatherMethod="POST" gatherFallbackUrl="fallback-test.com" gatherFallbackMethod="GET" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag" terminatingDigits="2" maxDigits="5" interDigitTimeout="1" firstDigitTimeout="3" repeatCount="2"><PlayAudio username="user" password="pass">https://audio.url/audio1.wav</PlayAudio><SpeakSentence>Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence></Gather>'
        self.gather.add_verb(self.speak_sentence)
        assert expected == self.gather.to_bxml()
