"""
record.py

Bandwidth's StopRecording BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StopRecording(Verb):

    def __init__(self):
        """Initialize a <StopRecording> verb

        Args: There are no args or text content for StopRecording
        """

        super().__init__(tag="StopRecording")
