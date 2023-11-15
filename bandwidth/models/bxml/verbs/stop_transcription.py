"""
stop_transcription.py

Bandwidth's Stop Transcription BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class StopTranscription(TerminalVerb):
    def __init__(
            self,
            name: str = None,
    ):
        """
        Initialize a <StopTranscription> verb
        :param name:
        """
        self.name = name

        super().__init__(
            tag="StopTranscription",
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
        }
