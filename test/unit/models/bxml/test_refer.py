"""
test_refer.py

Unit tests for the <Refer> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Refer, SipUri, Verb, NestableVerb


class TestRefer(unittest.TestCase):

    def setUp(self):
        self.sip_uri = SipUri(
            uri="sip:alice@atlanta.example.com"
        )
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
        minimal_refer = Refer(sip_uri=SipUri(uri="sip:bob@example.com"))
        expected = '<Refer><SipUri>sip:bob@example.com</SipUri></Refer>'
        assert expected == minimal_refer.to_bxml()
