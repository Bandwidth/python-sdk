"""
test_Pause.py

Unit tests for the <Pause> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Pause, Verb


class TestPause(unittest.TestCase):

    def setUp(self):
        self.pause = Pause(duration=30)

    def test_instance(self):
        assert isinstance(self.pause, Pause)
        assert isinstance(self.pause, Verb)

    def test_to_bxml(self):
        expected = '<Pause duration="30" />'
        assert expected == self.pause.to_bxml()
