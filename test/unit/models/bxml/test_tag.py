"""
test_tag.py

Unit tests for the <Tag> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import Tag


class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag(content="Test")
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Tag>Test</Tag>'
        assert(expected == self.tag.to_bxml())
