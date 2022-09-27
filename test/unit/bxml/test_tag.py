"""
test_tag.py

Unit tests for the <Tag> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.tag import Tag

class TestTag(unittest.TestCase):
    
    def setUp(self):
        self.tag = Tag(content="Test")
        self.test_verb = Verb(tag="test")

    def tearDown(self):
        pass
    
    def test_to_bxml(self):
        expected = '<Tag>Test</Tag>'
        assert(expected == self.tag.to_bxml())
    
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.tag.add_verb(self.test_verb)

