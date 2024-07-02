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
            tag="test"
        )

    def test_instance(self):
        assert isinstance(self.sip_uri, SipUri)
        assert isinstance(self.sip_uri, Verb)

    def test_to_bxml(self):
        expected = '<SipUri uui="abc123" transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="test">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        assert expected == self.sip_uri.to_bxml()
