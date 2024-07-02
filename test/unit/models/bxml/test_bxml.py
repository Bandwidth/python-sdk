"""
test_bxml.py

Unit tests for Bxml Model

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Bxml


class TestBxml(unittest.TestCase):

    def setUp(self):
        self.bxml = Bxml()

    def test_instance(self):
        assert isinstance(self.bxml, Bxml)

    def test_bxml_init(self):
        """Test initializing the <Bxml> root
        """
        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<Bxml />"
        assert self.bxml.to_bxml() == expected_bxml
