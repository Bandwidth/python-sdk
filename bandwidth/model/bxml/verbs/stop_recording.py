"""
record.py

Bandwidth's StopRecording BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class StopRecording(TerminalVerb):

    def __init__(self):
        """Initialize a <StopRecording> verb

        Args: There are no args or text content for StopRecording
        """

        super().__init__(tag="StopRecording")
