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
            bridge_complete_url="example.com/completeurl",
            bridge_complete_method="POST",
            bridge_complete_fallback_url="backupexample.com/completeurl",
            bridge_complete_fallback_method="POST",
            bridge_target_complete_url="example.com/targetcompleteurl",
            bridge_target_complete_method="POST",
            bridge_target_complete_fallback_url="backupexample.com/targetcompleteurl",
            bridge_target_complete_fallback_method="POST",
            username="user",
            password="pass",
            fallback_username="user",
            fallback_password="pass",
            tag="tag"
        )

    def test_instance(self):
        assert isinstance(self.bridge, Bridge)
        assert isinstance(self.bridge, Verb)

    def test_to_bxml(self):
        expected = '<Bridge bridgeCompleteUrl="example.com/completeurl" bridgeCompleteMethod="POST" bridgeCompleteFallbackUrl="backupexample.com/completeurl" bridgeCompleteFallbackMethod="POST" bridgeTargetCompleteUrl="example.com/targetcompleteurl" bridgeTargetCompleteMethod="POST" bridgeTargetCompleteFallbackUrl="backupexample.com/targetcompleteurl" bridgeTargetCompleteFallbackMethod="POST" username="user" password="pass" fallbackUsername="user" fallbackPassword="pass" tag="tag">+19198675309</Bridge>'
        assert expected == self.bridge.to_bxml()
