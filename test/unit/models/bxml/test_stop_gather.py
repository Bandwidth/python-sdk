"""
test_stop_gather.py

Unit tests for the <StopGather> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StopGather, Verb


class TestStopGather(unittest.TestCase):

    def setUp(self):
        self.stop_gather = StopGather()

    def test_instance(self):
        assert isinstance(self.stop_gather, StopGather)
        assert isinstance(self.stop_gather, Verb)

    def test_to_bxml(self):
        expected = '<StopGather />'
        assert expected == self.stop_gather.to_bxml()
