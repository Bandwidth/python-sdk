"""
test_bridge.py

Unit tests for the <Bridge> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Bridge, Verb


class TestBridge(unittest.TestCase):

    def setUp(self):
        self.bridge = Bridge(
            target_call="+19198675309",
            bridge_complete_url="https://example.com",
            tag="test"
        )

    def test_instance(self):
        assert isinstance(self.bridge, Bridge)
        assert isinstance(self.bridge, Verb)

    def test_to_bxml(self):
        expected = '<Bridge bridgeCompleteUrl="https://example.com" tag="test">+19198675309</Bridge>'
        assert expected == self.bridge.to_bxml()
