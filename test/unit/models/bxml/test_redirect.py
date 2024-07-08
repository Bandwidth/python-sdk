"""
test_redirect.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Redirect, Verb


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.redirect = Redirect("https://example.com/redirect")

    def test_instance(self):
        assert isinstance(self.redirect, Redirect)
        assert isinstance(self.redirect, Verb)

    def test_to_bxml(self):
        expected = '<Redirect redirectUrl="https://example.com/redirect" />'
        assert expected == self.redirect.to_bxml()
