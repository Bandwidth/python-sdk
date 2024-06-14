"""
test_stream_param.py

Unit tests for the <StreamParam> BXML verb

@copyright Bandwidth Inc.
"""
import unittest


from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import StreamParam


class TestStreamParam(unittest.TestCase):

    def setUp(self):
        self.stream_param = StreamParam(
            name="name1",
            value="value1"
        )
        self.test_verb = Verb(tag="test")


    def test_to_bxml(self):
        expected = '<StreamParam name="name1" value="value1" />'
        assert(expected == self.stream_param.to_bxml())
