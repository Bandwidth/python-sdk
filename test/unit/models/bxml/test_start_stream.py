"""
test_start_stream.py

Unit tests for the <StartStream> BXML verb

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.models.bxml import StartStream, StreamParam, Verb, NestableVerb


class TestStartStream(unittest.TestCase):

    def setUp(self):
        self.stream_param1 = StreamParam(
            name="name1",
            value="value1"
        )

        self.stream_param2 = StreamParam(
            name="name2",
            value="value2"
        )

        self.start_stream = StartStream(
            stream_params=[self.stream_param1],
            name = "stream1",
            mode = "bidirectional",
            tracks = "inbound",
            destination = "testurl.com",
            stream_event_url="eventurl.com",
            stream_event_method= "POST",
            username = "user",
            password = "pass"
        )

    def test_instance(self):
        assert isinstance(self.start_stream, StartStream)
        assert isinstance(self.start_stream, NestableVerb)
        assert isinstance(self.start_stream, Verb)

    def test_to_bxml(self):
        expected = '<StartStream destination="testurl.com" name="stream1" mode="bidirectional" tracks="inbound" streamEventUrl="eventurl.com" streamEventMethod="POST" username="user" password="pass"><StreamParam name="name1" value="value1" /></StartStream>'
        assert expected == self.start_stream.to_bxml()

    def test_add_verb(self):
        expected = '<StartStream destination="testurl.com" name="stream1" mode="bidirectional" tracks="inbound" streamEventUrl="eventurl.com" streamEventMethod="POST" username="user" password="pass"><StreamParam name="name1" value="value1" /><StreamParam name="name2" value="value2" /></StartStream>'
        self.start_stream.add_verb(self.stream_param2)
        assert expected == self.start_stream.to_bxml()
