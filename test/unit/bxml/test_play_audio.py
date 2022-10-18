"""
test_play_audio.py

Unit tests for the <PlayAudio> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs import PlayAudio

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

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.play_audio.add_verb(self.test_verb)
