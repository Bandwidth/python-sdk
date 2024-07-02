"""
record.py

Bandwidth's ResumeRecording BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class ResumeRecording(Verb):

    def __init__(
        self
    ):
        """Initialize a <ResumeRecording> verb

        Args: There are no args or text content for ResumeRecording
        """

        super().__init__(tag="ResumeRecording", content=None)
