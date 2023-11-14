"""
start_transcription.py

Bandwidth's Start Transcription BXML verb

@copyright Bandwidth INC
"""
from typing import List

from ..verb import Verb
from ..verbs.custom_param import CustomParam


class StartTranscription(Verb):
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
        :param name:
        :param tracks:
        :param transcription_event_url:
        :param transcription_event_method:
        :param username:
        :param password:
        :param destination:
        :param stabilized:
        :param custom_params:
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
