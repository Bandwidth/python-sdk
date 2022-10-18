"""
test_ring.py

Unit tests for the <Ring> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.ring import Ring


class TestRing(unittest.TestCase):

    def setUp(self):
        self.ring = Ring(
            duration="30",
            answer_call="true",
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Ring duration="30" answerCall="true" />'
        assert(expected == self.ring.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.ring.add_verb(self.test_verb)
