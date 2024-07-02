"""
test_response.py

Unit tests for Response Model

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Response


class TestResponse(unittest.TestCase):

    def setUp(self):
        self.response = Response()

    def test_instance(self):
        assert isinstance(self.response, Response)

    def test_response_init(self):
        """Test initializing the <Response> root
        """
        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<Response />"
        assert self.response.to_bxml() == expected_bxml
