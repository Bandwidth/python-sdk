"""
test_forward.py

Unit tests for the <Forward> BXML verb

@copyright Bandwidth Inc.
"""
import os
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.forward import Forward

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
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Forward to="19195554321" _from="19195554322" callTimeout="15" diversionTreatment="propagate" diversionReason="away" uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt" />'
        assert(expected == self.forward.to_bxml())
