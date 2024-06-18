"""
test_stream_param.py

Unit tests for the <StreamParam> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StreamParam, Verb


class TestStreamParam(unittest.TestCase):

    def setUp(self):
        self.stream_param = StreamParam(
            name="name1",
            value="value1"
        )

    def test_instance(self):
        assert isinstance(self.stream_param, StreamParam)
        assert isinstance(self.stream_param, Verb)

    def test_to_bxml(self):
        expected = '<StreamParam name="name1" value="value1" />'
        assert expected == self.stream_param.to_bxml()
