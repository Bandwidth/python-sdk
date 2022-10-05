"""
test_stop_stream.py

Unit tests for the <StopStream> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.stop_stream import StopStream


class TestTag(unittest.TestCase):

    def setUp(self):
        self.stop_stream = StopStream(name="conf")
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<StopStream name="conf" />'
        assert(expected == self.stop_stream.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.stop_stream.add_verb(self.test_verb)

