"""
test_Pause.py

Unit tests for the <Pause> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.pause import Pause


class TestPause(unittest.TestCase):

    def setUp(self):
        self.pause = Pause(duration=30)
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Pause duration="30" />'
        assert(expected == self.pause.to_bxml())
