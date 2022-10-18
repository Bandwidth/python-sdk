"""
test_ring.py

Unit tests for the <Ring> BXML verb

@copyright Bandwidth Inc.
"""
import os
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.ring import Ring


class TestRing(unittest.TestCase):

    def setUp(self):
        self.ring = Ring(
            duration=30,
            answer_call=True,
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Ring duration="30" answerCall="true" />'
        assert(expected == self.ring.to_bxml())
