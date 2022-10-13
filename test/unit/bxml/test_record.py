"""
test_record.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.record import Record


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record()
        self.record.max_duration = 10
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Record maxDuration="10" />'
        assert(expected == self.record.to_bxml())


    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.record.add_verb(self.test_verb)

