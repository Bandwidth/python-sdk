"""
test_forward.py

Unit tests for the <Forward> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Forward, Verb

class TestForward(unittest.TestCase):

    def setUp(self):
        self.forward = Forward(
            to="19195554321",
            _from="19195554322",
            call_timeout = "15",
            diversion_treatment="propagate",
            diversion_reason="away",
            uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt"
        )

    def test_instance(self):
        assert isinstance(self.forward, Forward)
        assert isinstance(self.forward, Verb)

    def test_to_bxml(self):
        expected = '<Forward to="19195554321" from="19195554322" callTimeout="15" diversionTreatment="propagate" diversionReason="away" uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt" />'
        assert expected == self.forward.to_bxml()
