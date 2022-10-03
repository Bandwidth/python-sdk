"""
test_redirect.py

Unit tests for the <Record> BXML verb

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.model.bxml.verb import Verb
from bandwidth.model.bxml.verbs.redirect import Redirect


class TestRecord(unittest.TestCase):

    def setUp(self):
        self.redirect = Redirect("https://example.com/redirect")
        # self.redirect.redirect_url = "https://example.com/redirect"
        self.test_verb = Verb(tag="test")

    def test_to_bxml(self):
        expected = '<Redirect redirectUrl="https://example.com/redirect" />'
        assert(expected == self.redirect.to_bxml())


    def test_add_verb(self):
        with pytest.raises(AttributeError):
            self.record.add_verb(self.test_verb)

