"""
test_redirect.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Redirect, Verb


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.redirect = Redirect(
            redirect_url="https://example.com/redirect",
            redirect_method="POST",
            redirect_fallback_url="https://fallback.example.com/redirect",
            redirect_fallback_method="GET",
            username="user",
            password="pass",
            fallback_username="fallbackUser",
            fallback_password="fallbackPass",
            tag="tag"
        )

    def test_instance(self):
        assert isinstance(self.redirect, Redirect)
        assert isinstance(self.redirect, Verb)

    def test_to_bxml(self):
        expected = '<Redirect redirectUrl="https://example.com/redirect" redirectMethod="POST" redirectFallbackUrl="https://fallback.example.com/redirect" redirectFallbackMethod="GET" username="user" password="pass" fallbackUsername="fallbackUser" fallbackPassword="fallbackPass" tag="tag" />'
        assert expected == self.redirect.to_bxml()
