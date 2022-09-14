"""
start_stream.py

Representation of Bandwidth's start stream BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

START_STREAM_TAG = "StartStream"


class StartStream(AbstractBxmlVerb):

    def __init__(self, destination, name=None, tracks=None, streamEventUrl=None, streamEventMethod=None, username=None, password=None, streamParams=None):
        """
        Initializes the StartStream class with the following parameters

        :param str destination: A websocket URI to send the stream to
        :param str name: A name to refer to this stream by
        :param str tracks: The part of the call to send a stream from. `inbound`, `outbound` or `both`.
        :param str streamEventUrl: URL to send the associated Webhook events to during this stream's lifetime
        :param str streamEventMethod: The HTTP method to use for the request to `streamEventUrl`. `GET` or `POST`
        :param str username: The username to send in the HTTP request to `streamEventUrl`
        :param str password: The password to send in the HTTP request to `streamEventUrl`
        """
        self.destination = destination
        self.name = name
        self.tracks = tracks
        self.streamEventUrl = streamEventUrl
        self.streamEventMethod = streamEventMethod
        self.username = username
        self.password = password
        self.stream_params = streamParams

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(START_STREAM_TAG)
        root.set("destination", self.destination)
        if self.name is not None:
            root.set("name", self.name)
        if self.tracks is not None:
            root.set("tracks", self.tracks)
        if self.streamEventUrl is not None:
            root.set("streamEventUrl", self.streamEventUrl)
        if self.streamEventMethod is not None:
            root.set("streamEventMethod", self.streamEventMethod)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.stream_params is not None:
            for stream_param in self.stream_params:
                root.append(stream_param.to_etree_element())
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
