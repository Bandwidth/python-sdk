"""
pause_recording.py

Bandwidth's PauseRecording BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class PauseRecording(Verb):

    def __init__(self):
        """Initialize a <PauseRecording> verb
        """
        super().__init__(tag="PauseRecording")
