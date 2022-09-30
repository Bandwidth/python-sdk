"""
test_sip_uri.py

Unit tests for the <SipUri> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.sip_uri import SipUri


class TestSipUri(unittest.TestCase):

    def setUp(self):
        self.sip_uri = SipUri(
            uri="sip:1-999-123-4567@voip-provider.example.net",
            uui="abc123",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            transfer_answer_method="POST",
            tag="test"
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<SipUri tag="test" transferAnswerMethod="POST" transferAnswerUrl="https://example.com/webhooks/transfer_answer" uui="abc123">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        else:
            expected = '<SipUri uui="abc123" transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="test">sip:1-999-123-4567@voip-provider.example.net</SipUri>'
        assert(expected == self.sip_uri.to_bxml())

    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.sip_uri.add_verb(self.test_verb)
