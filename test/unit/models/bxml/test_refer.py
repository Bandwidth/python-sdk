"""
test_refer.py

Unit tests for the <Refer> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Refer, ReferSipUri, SipUri, Verb, NestableVerb


class TestRefer(unittest.TestCase):

    def setUp(self):
        self.sip_uri = ReferSipUri(uri="sip:alice@atlanta.example.com")
        self.refer = Refer(
            sip_uri=self.sip_uri,
            refer_complete_url="https://example.com/handleRefer",
            refer_complete_method="POST",
            tag="test"
        )

    def test_instance(self):
        assert isinstance(self.refer, Refer)
        assert isinstance(self.refer, NestableVerb)
        assert isinstance(self.refer, Verb)

    def test_to_bxml(self):
        expected = '<Refer referCompleteUrl="https://example.com/handleRefer" referCompleteMethod="POST" tag="test"><SipUri>sip:alice@atlanta.example.com</SipUri></Refer>'
        assert expected == self.refer.to_bxml()

    def test_minimal(self):
        minimal_refer = Refer(sip_uri=ReferSipUri(uri="sip:bob@example.com"))
        expected = '<Refer><SipUri>sip:bob@example.com</SipUri></Refer>'
        assert expected == minimal_refer.to_bxml()

    def test_refer_sip_uri_is_not_transfer_sip_uri(self):
        """ReferSipUri is a distinct type from the Transfer SipUri — no Transfer-specific
        attributes (transfer_answer_url, uui, auth, etc.) are accepted."""
        assert not isinstance(self.sip_uri, SipUri)
        assert isinstance(self.sip_uri, ReferSipUri)

    def test_refer_sip_uri_has_no_transfer_attributes(self):
        """ReferSipUri carries only uri — no Transfer baggage."""
        assert not hasattr(self.sip_uri, 'transfer_answer_url')
        assert not hasattr(self.sip_uri, 'uui')
        assert not hasattr(self.sip_uri, 'username')
        assert not hasattr(self.sip_uri, 'password')
