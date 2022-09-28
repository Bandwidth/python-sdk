"""
test_sip_uri.py

Unit tests for the <SipUri> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.sip_uri import SipUri


class TestPhoneNumber(unittest.TestCase):
    
    def setUp(self):
        self.phone_number = SipUri(
            uri="sip:1-999-123-4567@voip-provider.example.net",
            uui="abc123",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            transfer_answer_method="POST",
            transfer_answer_fallback_url="",
            transfer_answer_fallback_method="",
            transfer_disconnect_url="",
            transfer_disconnect_method="",
            username="",
            password="",
            fallback_username="",
            fallback_password="",
            tag="test"
        )
        self.test_verb = Verb(tag="test")
    
    def test_to_bxml(self):
        expected = '<SipUri uui="abc123" transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="test">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        assert(expected == self.phone_number.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.phone_number.add_verb(self.test_verb)
