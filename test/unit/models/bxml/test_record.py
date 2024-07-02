"""
test_record.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Record, Verb


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record()
        self.record.max_duration = 10

    def test_instance(self):
        assert isinstance(self.record, Record)
        assert isinstance(self.record, Verb)

    def test_to_bxml(self):
        expected = '<Record maxDuration="10" />'
        assert expected == self.record.to_bxml()
