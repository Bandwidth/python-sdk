"""
start_stream.py

Bandwidth's StartStream BXML verb

@copyright Bandwidth INC
"""
from typing import List

from ..nestable_verb import NestableVerb
from ..verbs.stream_param import StreamParam


class StartStream(NestableVerb):

    def __init__(
        self, destination: str, stream_params: List[StreamParam] = [],
        name: str=None, mode: str=None, tracks: str=None,
        stream_event_url: str=None,
        stream_event_method: str=None,
        username: str=None, password: str=None,
    ):
        """Initialize a <StartStream> verb

        Args:
            name (str, optional): A name to refer to this stream by. Used when sending <StopStream>. If not provided, it will default to the generated stream id as sent in the Media Stream Started webhook.
            mode (str, optional): The mode to use for the stream. unidirectional or bidirectional. Specifies whether the audio being streamed over the WebSocket is bidirectional (the service can both read and write audio over the WebSocket) or unidirectional (one-way, read-only). Default is unidirectional.
            tracks (str, optional): The part of the call to send a stream from. inbound, outbound or both. Default is inbound.
            destination (str, optional): A websocket URI to send the stream to. The audio from the specified tracks will be sent via websocket to this URL as base64-encoded PCMU/G711 audio. See below for more details on the websocket packet format.
            stream_event_url (str, optional): URL to send the associated Webhook events to during this stream's lifetime. Does not accept BXML. May be a relative URL.
            stream_event_method (str, optional): The HTTP method to use for the request to streamEventUrl. GET or POST. Default value is POST.
            username (str, optional): The username to send in the HTTP request to streamEventUrl. If specified, the URLs must be TLS-encrypted (i.e., https).
            password (str, optional): The password to send in the HTTP request to streamEventUrl. If specified, the URLs must be TLS-encrypted (i.e., https).
        
        Nested Verbs:
            StreamParam: (optional) You may specify up to 12 <StreamParam/> elements nested within a <StartStream> tag. These elements define optional user specified parameters that will be sent to the destination URL when the stream is first started.       

        """
        self.destination = destination
        self.stream_params = stream_params
        self.name = name
        self.mode = mode
        self.tracks = tracks
        self.stream_event_url = stream_event_url
        self.stream_event_method = stream_event_method
        self.username = username
        self.password = password
        super().__init__(
            tag="StartStream",
            nested_verbs=self.stream_params
        )

    @property
    def _attributes(self):
        return {
            "destination": self.destination,
            "name": self.name,
            "mode": self.mode,
            "tracks": self.tracks,
            "streamEventUrl": self.stream_event_url,
            "streamEventMethod": self.stream_event_method,
            "username": self.username,
            "password": self.password,
        }
