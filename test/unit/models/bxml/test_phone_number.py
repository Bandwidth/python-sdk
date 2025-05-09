"""
test_phone_number.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import PhoneNumber, Verb


class TestPhoneNumber(unittest.TestCase):

    def setUp(self):
        self.phone_number = PhoneNumber(
            number="+19195551234",
            uui="abc123",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            transfer_answer_method="POST",
            tag=""
        )

    def test_instance(self):
        assert isinstance(self.phone_number, PhoneNumber)
        assert isinstance(self.phone_number, Verb)

    def test_to_bxml(self):
        expected = '<PhoneNumber transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="" uui="abc123">+19195551234</PhoneNumber>'
        assert expected == self.phone_number.to_bxml()
