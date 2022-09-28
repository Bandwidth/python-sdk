"""
test_transfer.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verbs.transfer import Transfer
from bandwidth.model.bxml.verbs.phone_number import PhoneNumber
from bandwidth.model.bxml.verbs.sip_uri import SipUri


class TestTransfer(unittest.TestCase):
    
    def setUp(self):
        self.sip_uri = SipUri(
            uri="sip@bw.com",
            uui="test"
        )
        self.phone_number = PhoneNumber(
            number="+19195551234",
            tag="test"
        )
        self.transfer = Transfer(
            transfer_to=[self.sip_uri],
            transfer_caller_id = "+19195554321",
            call_timeout = "15",
            transfer_complete_url = "",
            transfer_complete_method = "",
            transfer_complete_fallback_url = "",
            transfer_complete_fallback_method = "",
            username = "",
            password = "",
            fallback_username = "",
            fallback_password = "",
            tag = "test"
        )
    
    def test_to_bxml(self):
        expected = '<Transfer transferCallerId="+19195554321" callTimeout="15" tag="test"><SipUri uui="test">sip@bw.com</SipUri></Transfer>'
        assert(expected == self.transfer.to_bxml())
    
    def test_add_verb(self):
        expected = '<Transfer transferCallerId="+19195554321" callTimeout="15" tag="test"><SipUri uui="test">sip@bw.com</SipUri><PhoneNumber tag="test">+19195551234</PhoneNumber></Transfer>'
        self.transfer.add_transfer_recipient(self.phone_number)
        assert(expected == self.transfer.to_bxml())
