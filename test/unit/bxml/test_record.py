"""
test_record.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import Record


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record()
        self.record.max_duration = 10
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Record maxDuration="10" />'
        assert(expected == self.record.to_bxml())
