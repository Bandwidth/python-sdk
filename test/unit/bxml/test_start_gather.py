"""
test_start_gather.py

Unit tests for the <StartGather> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.start_gather import StartGather


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

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.start_gather.add_verb(self.test_verb)
