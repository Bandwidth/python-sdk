"""
test_bxml.py

Unit tests for Bxml Model

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.bxml import Bxml


class TestTag(unittest.TestCase):
    
    def setUp(self):
        self.response = Bxml()

    def test_response_init(self):
        """Test initializing the <Bxml> root
        """
        expected_bxml = "<?xml version='1.0' encoding='utf8'?>\n<Bxml />"
        assert self.response.to_bxml() == expected_bxml
