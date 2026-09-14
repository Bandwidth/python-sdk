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
            transfer_answer_fallback_url="https://fallback.example.com/webhooks/transfer_answer",
            transfer_answer_fallback_method="GET",
            transfer_disconnect_url="https://example.com/webhooks/transfer_disconnect",
            transfer_disconnect_method="POST",
            username="user",
            password="pass",
            fallback_username="fallbackUser",
            fallback_password="fallbackPass",
            tag=""
        )

    def test_instance(self):
        assert isinstance(self.phone_number, PhoneNumber)
        assert isinstance(self.phone_number, Verb)

    def test_to_bxml(self):
        expected = '<PhoneNumber transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" transferAnswerFallbackUrl="https://fallback.example.com/webhooks/transfer_answer" transferAnswerFallbackMethod="GET" transferDisconnectUrl="https://example.com/webhooks/transfer_disconnect" transferDisconnectMethod="POST" username="user" password="pass" fallbackUsername="fallbackUser" fallbackPassword="fallbackPass" tag="" uui="abc123">+19195551234</PhoneNumber>'
        assert expected == self.phone_number.to_bxml()
