"""
test_ring.py

Unit tests for the <Ring> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml.verbs.ring import Ring, Verb


class TestRing(unittest.TestCase):

    def setUp(self):
        self.ring = Ring(
            duration=30,
            answer_call=True,
        )

    def test_instance(self):
        assert isinstance(self.ring, Ring)
        assert isinstance(self.ring, Verb)

    def test_to_bxml(self):
        expected = '<Ring duration="30" answerCall="True" />'
        assert expected == self.ring.to_bxml()
