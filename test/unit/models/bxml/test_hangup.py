"""
test_hangup.py

Unit tests for the <Hangup> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml.verbs.hangup import Hangup


class TestHangup(unittest.TestCase):

    def setUp(self):
        self.hangup = Hangup()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Hangup />'
        assert(expected == self.hangup.to_bxml())
