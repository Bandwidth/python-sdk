"""
test_sip_uri.py

Unit tests for the <SipUri> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import SipUri, Verb


class TestSipUri(unittest.TestCase):

    def setUp(self):
        self.sip_uri = SipUri(
            uri="sip:1-999-123-4567@voip-provider.example.net",
            uui="abc123",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            transfer_answer_method="POST",
            transfer_answer_fallback_url="https://fallback.example.com/webhooks/transfer_answer",
            transfer_answer_fallback_method="GET",
            transfer_disconnect_url="https://example.com/webhooks/transfer_disconnect",
            transfer_disconnect_method="POST",
            username="user",
            password="pass",
            fallback_username="fallbackUser",
            fallback_password="fallbackPass",
            tag="test"
        )

    def test_instance(self):
        assert isinstance(self.sip_uri, SipUri)
        assert isinstance(self.sip_uri, Verb)

    def test_to_bxml(self):
        expected = '<SipUri uui="abc123" transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" transferAnswerFallbackUrl="https://fallback.example.com/webhooks/transfer_answer" transferAnswerFallbackMethod="GET" transferDisconnectUrl="https://example.com/webhooks/transfer_disconnect" transferDisconnectMethod="POST" username="user" password="pass" fallbackUsername="fallbackUser" fallbackPassword="fallbackPass" tag="test">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        assert expected == self.sip_uri.to_bxml()
