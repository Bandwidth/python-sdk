"""
start_transcription.py

Bandwidth's Start Transcription BXML verb

@copyright Bandwidth INC
"""
from typing import List

from ..nestable_verb import NestableVerb
from ..verbs.custom_param import CustomParam


class StartTranscription(NestableVerb):
    def __init__(
            self, name: str = None,
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
        Initialize a <StartTranscription> verb
        :param name: A name to refer to this transcription by. Used when sending <StopTranscription>. If not provided, it will default to the generated transcription id as sent in the Real-Time Transcription Started webhook.
        :param tracks: The part of the call to send a transcription from. inbound, outbound or both. Default is inbound.
        :param transcription_event_url: URL to send the associated Webhook events to during this real-time transcription's lifetime. Does not accept BXML. May be a relative URL.
        :param transcription_event_method: The HTTP method to use for the request to transcriptionEventUrl. GET or POST. Default value is POST.
        :param username: The username to send in the HTTP request to transcriptionEventUrl. If specified, the transcriptionEventUrl must be TLS-encrypted (i.e., https).
        :param password: The password to send in the HTTP request to transcriptionEventUrl. If specified, the transcriptionEventUrl must be TLS-encrypted (i.e., https).
        :param destination:  A websocket URI to send the transcription to. A transcription of the specified tracks will be sent via websocket to this URL as a series of JSON messages. See below for more details on the websocket packet format.
        :param stabilized:  A websocket URI to send the transcription to. A transcription of the specified tracks will be sent via websocket to this URL as a series of JSON messages. See below for more details on the websocket packet format.
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

        super().__init__(
            tag="StartTranscription",
            nested_verbs=self.custom_params
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
            "tracks": self.tracks,
            "transcriptionEventUrl": self.transcription_event_url,
            "transcriptionEventMethod": self.transcription_event_method,
            "username": self.username,
            "password": self.password,
            "destination": self.destination,
            "stabilized": self.stabilized,
        }
