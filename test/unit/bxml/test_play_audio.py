"""
test_play_audio.py

Unit tests for the <PlayAudio> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import PlayAudio

class TestPlayAudio(unittest.TestCase):

    def setUp(self):
        self.play_audio = PlayAudio(
            audio_uri="https://audio.url/audio1.wav",
            username="user",
            password="pass"
        )
        self.test_verb = Verb(tag="test")


    def test_to_bxml(self):
        expected = '<PlayAudio username="user" password="pass">https://audio.url/audio1.wav</PlayAudio>'
        assert(expected == self.play_audio.to_bxml())
