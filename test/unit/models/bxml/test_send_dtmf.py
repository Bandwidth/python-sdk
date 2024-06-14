"""
test_send_dtmf.py

Unit tests for the <SendDtmf> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml.verbs.send_dtmf import SendDtmf


class TestSendDtmf(unittest.TestCase):

    def setUp(self):
        self.send_dtmf = SendDtmf(
            digits="1234",
            tone_duration=3,
            tone_interval=5
        )
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<SendDtmf toneDuration="3" toneInterval="5">1234</SendDtmf>'
        assert(expected == self.send_dtmf.to_bxml())
