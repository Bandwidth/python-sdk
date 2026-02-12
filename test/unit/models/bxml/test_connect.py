"""
test_connect.py

Unit tests for the <Connect> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import Endpoint, Connect, NestableVerb, Verb


class TestConnect(unittest.TestCase):

    def setUp(self):
        self.endpoint = Endpoint(
            endpoint_id="endpoint-id",
        )

        self.connect = Connect(
            event_callback_url= "https://callback-test.com",
            destination=[self.endpoint]
        )

    def test_instance(self):
        assert isinstance(self.connect, Connect)
        assert isinstance(self.connect, NestableVerb)
        assert isinstance(self.connect, Verb)

    def test_defaults(self):
        connect = Connect(
            destination=[self.endpoint]
        )
        expected = '<Connect><Endpoint>endpoint-id</Endpoint></Connect>'
        assert expected == connect.to_bxml()

    def test_to_bxml(self):
        expected = '<Connect eventCallbackUrl="https://callback-test.com"><Endpoint>endpoint-id</Endpoint></Connect>'
        assert expected == self.connect.to_bxml()

    def test_add_verb(self):
        connect = Connect()
        expected = '<Connect><Endpoint>endpoint-id</Endpoint></Connect>'
        connect.add_verb(self.endpoint)
        assert expected == connect.to_bxml()
