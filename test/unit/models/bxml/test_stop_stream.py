"""
test_stop_stream.py

Unit tests for the <StopStream> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StopStream, Verb


class TestStopStream(unittest.TestCase):

    def setUp(self):
        self.stop_stream = StopStream(name="conf")

    def test_instance(self):
        assert isinstance(self.stop_stream, StopStream)
        assert isinstance(self.stop_stream, Verb)

    def test_to_bxml(self):
        expected = '<StopStream name="conf" />'
        assert expected == self.stop_stream.to_bxml()
