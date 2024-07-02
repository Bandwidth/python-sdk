"""
test_hangup.py

Unit tests for the <Hangup> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Hangup, Verb


class TestHangup(unittest.TestCase):

    def setUp(self):
        self.hangup = Hangup()

    def test_instance(self):
        assert isinstance(self.hangup, Hangup)
        assert isinstance(self.hangup, Verb)

    def test_to_bxml(self):
        expected = '<Hangup />'
        assert expected == self.hangup.to_bxml()
