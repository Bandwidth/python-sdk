"""
test_stop_gather.py

Unit tests for the <StopGather> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.stop_gather import StopGather


class TestStopGather(unittest.TestCase):

    def setUp(self):
        self.stop_gather = StopGather()
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<StopGather />'
        assert(expected == self.stop_gather.to_bxml())
