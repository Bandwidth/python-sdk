"""
test_phone_number.py

Unit tests for the <PhoneNumber> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
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
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<PhoneNumber tag="" transferAnswerMethod="POST" transferAnswerUrl="https://example.com/webhooks/transfer_answer">+19195551234</PhoneNumber>'
        else:
            expected = '<PhoneNumber transferAnswerUrl="https://example.com/webhooks/transfer_answer" transferAnswerMethod="POST" tag="">+19195551234</PhoneNumber>'
            
        assert(expected == self.phone_number.to_bxml())
    
    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.phone_number.add_verb(self.test_verb)