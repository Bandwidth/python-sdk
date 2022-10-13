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
            duration=30,
            answer_call=True,
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<Ring answerCall="True" duration="30" />'
        else:
            expected = '<Ring duration="30" answerCall="True" />'

        assert(expected == self.ring.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.ring.add_verb(self.test_verb)
