"""
test_redirect.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.redirect import Redirect


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.redirect = Redirect("https://example.com/redirect")
        # self.redirect.redirect_url = "https://example.com/redirect"
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Redirect redirectUrl="https://example.com/redirect" />'
        assert(expected == self.redirect.to_bxml())
