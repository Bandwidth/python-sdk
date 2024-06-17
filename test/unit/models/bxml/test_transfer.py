"""
test_transfer.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Transfer, PhoneNumber, SipUri, Verb, NestableVerb


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
            call_timeout = "15",
            transfer_caller_id = "+19195554321",
            transfer_caller_display_name="test",
            tag = "test"
        )

    def test_instance(self):
        assert isinstance(self.transfer, Transfer)
        assert isinstance(self.transfer, NestableVerb)
        assert isinstance(self.transfer, Verb)

    def test_to_bxml(self):
        expected = '<Transfer transferCallerId="+19195554321" transferCallerDisplayName="test" callTimeout="15" tag="test"><SipUri uui="test">sip@bw.com</SipUri></Transfer>'
        assert expected == self.transfer.to_bxml()

    def test_add_verb(self):
        expected = '<Transfer transferCallerId="+19195554321" transferCallerDisplayName="test" callTimeout="15" tag="test"><SipUri uui="test">sip@bw.com</SipUri><PhoneNumber tag="test">+19195551234</PhoneNumber></Transfer>'
        self.transfer.add_transfer_recipient(self.phone_number)
        assert expected == self.transfer.to_bxml()
