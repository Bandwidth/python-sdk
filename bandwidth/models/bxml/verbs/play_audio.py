"""
play_audio.py

Bandwidth's PlayAudio BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class PlayAudio(Verb):

    def __init__(
        self, audio_uri: str, 
        username: str=None, password: str=None
    ):
        """Initialize a <PlayAudio> verb

        Args:
            audio_uri (str): The URL of the audio file to play. May be a relative URL.
            username (str, optional): The username to send in the HTTP request to audio_uri.
            password (str, optional): The password to send in the HTTP request to audio_uri.
        """
        self.audio_uri = audio_uri
        self.username = username
        self.password = password
        super().__init__(
            tag="PlayAudio",
            content=self.audio_uri,
        )

    @property
    def _attributes(self):
        return {
            "username": self.username,
            "password": self.password,
        }
