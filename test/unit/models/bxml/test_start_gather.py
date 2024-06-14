"""
test_start_gather.py

Unit tests for the <StartGather> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import StartGather


class TestStartGather(unittest.TestCase):

    def setUp(self):
        self.start_gather = StartGather(
            dtmf_url="https://example.com/startgather",
            dtmf_method="POST",
            username="user",
            password="pass",
            tag="tag"
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<StartGather dtmfUrl="https://example.com/startgather" dtmfMethod="POST" username="user" password="pass" tag="tag" />'
        assert(expected == self.start_gather.to_bxml())
