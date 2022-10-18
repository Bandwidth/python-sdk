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
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<Bridge bridgeCompleteUrl="https://example.com" tag="test">+19198675309</Bridge>'
        else:
            expected = '<Bridge bridgeCompleteUrl="https://example.com" tag="test">+19198675309</Bridge>'
        assert(expected == self.bridge.to_bxml())
