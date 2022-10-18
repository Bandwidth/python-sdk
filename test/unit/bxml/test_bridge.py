"""
test_bridge.py

Unit tests for the <Bridge> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.bridge import Bridge


class TestBridge(unittest.TestCase):

    def setUp(self):
        self.bridge = Bridge(
            target_call="+19198675309",
            bridge_complete_url="https://example.com",
            tag="test"
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Bridge bridgeCompleteUrl="https://example.com" tag="test">+19198675309</Bridge>'
        assert(expected == self.bridge.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.bridge.add_verb(self.test_verb)
