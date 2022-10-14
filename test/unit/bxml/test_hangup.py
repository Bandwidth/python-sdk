"""
test_hangup.py

Unit tests for the <Hangup> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.hangup import Hangup


class TestHangup(unittest.TestCase):
    
    def setUp(self):
        self.hangup = Hangup()
        self.test_verb = Verb(tag="test")
    
    def test_to_bxml(self):
        expected = '<Hangup />'
        assert(expected == self.hangup.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.hangup.add_verb(self.test_verb)

