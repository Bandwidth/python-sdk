"""
record.py

Bandwidth's ResumeRecording BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class ResumeRecording(TerminalVerb):

    def __init__(
        self
    ):
        """Initialize a <ResumeRecording> verb

        Args: There are no args or text content for ResumeRecording
        """

        super().__init__(tag="ResumeRecording", content=None)
