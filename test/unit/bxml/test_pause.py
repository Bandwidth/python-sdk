"""
test_Pause.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verbs.pause import Pause

class TestPause(unittest.TestCase):
    
    def setUp(self):
        self.pause = Pause(duration="30")
    
    def test_to_bxml(self):
        expected = '<Pause duration="30" />'
        assert(expected == self.pause.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.pause.add_verb(self.test_verb)
