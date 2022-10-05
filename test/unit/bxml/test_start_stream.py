"""
test_start_stream.py

Unit tests for the <StartStream> BXML verb

@copyright Bandwidth Inc.
"""
import os
import pytest
import unittest

from bandwidth.model.bxml.verbs import StartStream, StreamParam

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
            tracks = "inbound",
            destination = "testurl.com",
            stream_event_url="eventurl.com",
            stream_event_method= "POST",
            username = "user",
            password = "pass"
        )
    
    def test_to_bxml(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<StartStream destination="testurl.com" name="stream1" password="pass" streamEventMethod="POST" streamEventUrl="eventurl.com" tracks="inbound" username="user"><StreamParam name="name1" value="value1" /></StartStream>'
        else:
            expected = '<StartStream destination="testurl.com" name="stream1" tracks="inbound" streamEventUrl="eventurl.com" streamEventMethod="POST" username="user" password="pass"><StreamParam name="name1" value="value1" /></StartStream>'
        assert(expected == self.start_stream.to_bxml())
    
    def test_add_verb(self):
        if os.environ['PYTHON_VERSION'] == '3.7':
            expected = '<StartStream destination="testurl.com" name="stream1" password="pass" streamEventMethod="POST" streamEventUrl="eventurl.com" tracks="inbound" username="user"><StreamParam name="name1" value="value1" /><StreamParam name="name2" value="value2" /></StartStream>'
        else:
            expected = '<StartStream destination="testurl.com" name="stream1" tracks="inbound" streamEventUrl="eventurl.com" streamEventMethod="POST" username="user" password="pass"><StreamParam name="name1" value="value1" /><StreamParam name="name2" value="value2" /></StartStream>'
        self.start_stream.add_verb(self.stream_param2)
        assert(expected == self.start_stream.to_bxml())