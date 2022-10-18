"""
test_phone_number.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import os
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.phone_number import PhoneNumber


class TestPhoneNumber(unittest.TestCase):

    def setUp(self):
        self.phone_number = PhoneNumber(
            number="+19195551234",
            transfer_answer_url="https://example.com/webhooks/transfer_answer",
            transfer_answer_method="POST",
            tag=""
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<PhoneNumber transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="">+19195551234</PhoneNumber>'
        assert(expected == self.phone_number.to_bxml())
