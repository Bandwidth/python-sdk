"""
start_transcription.py

Representation of Bandwidth's StartTranscription BXML verb

@license MIT
"""

from typing import List

from lxml import etree

from .base_verb import AbstractBxmlVerb
from .custom_param import CustomParam

START_TRANSCRIPTION_TAG = "StartTranscription"


class StartTranscription(AbstractBxmlVerb):

    def __init__(
            self,
            name: str = None,
            tracks: str = None,
            transcription_event_url: str = None,
            transcription_event_method: str = None,
            username: str = None,
            password: str = None,
            destination: str = None,
            stabilized: bool = None,
            custom_params: List[CustomParam] = None,
    ):
        """
        Initializes the StartTranscription class
        :param name: A name to refer to this transcription by. Used when sending <StopTranscription>. If not provided, it will default to the generated transcription id as sent in the Real-Time Transcription Started webhook.
        :param tracks: The part of the call to send a transcription from. inbound, outbound or both. Default is inbound.
        :param transcription_event_url: URL to send the associated Webhook events to during this real-time transcription's lifetime. Does not accept BXML. May be a relative URL.
        :param transcription_event_method: The HTTP method to use for the request to transcriptionEventUrl. GET or POST. Default value is POST.
        :param username: The username to send in the HTTP request to transcriptionEventUrl. If specified, the transcriptionEventUrl must be TLS-encrypted (i.e., https).
        :param password: The password to send in the HTTP request to transcriptionEventUrl. If specified, the transcriptionEventUrl must be TLS-encrypted (i.e., https).
        :param destination: A websocket URI to send the transcription to. A transcription of the specified tracks will be sent via websocket to this URL as a series of JSON messages. See below for more details on the websocket packet format.
        :param stabilized: Whether to send transcription update events to the specified destination only after they have become stable. Requires destination. Defaults to true.
        :param custom_params: These elements define optional user specified parameters that will be sent to the destination URL when the real-time transcription is first started.
        """
        self.name = name
        self.tracks = tracks
        self.transcription_event_url = transcription_event_url
        self.transcription_event_method = transcription_event_method
        self.username = username
        self.password = password
        self.destination = destination
        self.stabilized = stabilized
        self.custom_params = custom_params

    def to_bxml(self):
        root = etree.Element(START_TRANSCRIPTION_TAG)
        if self.name is not None:
            root.set("name", self.name)
        if self.tracks is not None:
            root.set("tracks", self.tracks)
        if self.transcription_event_url is not None:
            root.set("transcriptionEventUrl", self.transcription_event_url)
        if self.transcription_event_method is not None:
            root.set("transcriptionEventMethod", self.transcription_event_method)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.destination is not None:
            root.set("destination", self.destination)
        if self.stabilized is not None:
            root.set("stabilized", str(self.stabilized).lower())
        if self.custom_params is not None:
            for custom_param in self.custom_params:
                root.append(custom_param.to_etree_element())
        return etree.tostring(root).decode()
