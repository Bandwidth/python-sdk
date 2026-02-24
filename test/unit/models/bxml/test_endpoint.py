"""
test_endpoint.py

Unit tests for the <Endpoint> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Endpoint, Verb


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.endpoint = Endpoint(
            endpoint_id="endpoint-id"
        )

    def test_instance(self):
        assert isinstance(self.endpoint, Endpoint)
        assert isinstance(self.endpoint, Verb)

    def test_to_bxml(self):
        expected = '<Endpoint>endpoint-id</Endpoint>'
        assert expected == self.endpoint.to_bxml()
