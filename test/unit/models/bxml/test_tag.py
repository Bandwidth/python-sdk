"""
test_tag.py

Unit tests for the <Tag> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Tag, Verb


class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag(content="Test")

    def test_instance(self):
        assert isinstance(self.tag, Tag)
        assert isinstance(self.tag, Verb)

    def test_to_bxml(self):
        expected = '<Tag>Test</Tag>'
        assert expected == self.tag.to_bxml()
