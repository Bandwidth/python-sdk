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
            tag="test",
            transfer_answer_method="POST",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            uui="abc123"
        )
        self.test_verb = Verb(tag="test")
    
    def test_to_bxml(self):
        expected = '<SipUri tag="test" transferAnswerMethod="POST" transferAnswerUrl="https://example.com/webhooks/transfer_answer" uui="abc123">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        assert(expected == self.phone_number.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.phone_number.add_verb(self.test_verb)
