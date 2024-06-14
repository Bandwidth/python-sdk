"""
test_redirect.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Verb
from bandwidth.models.bxml import Redirect


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.redirect = Redirect("https://example.com/redirect")
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Redirect redirectUrl="https://example.com/redirect" />'
        assert(expected == self.redirect.to_bxml())
