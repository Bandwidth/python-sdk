"""
stop_stream.py

Bandwidth's StopStream BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class StopStream(TerminalVerb):

    def __init__(
        self, name: str
    ):
        """Initialize a <StopStream> verb

        Args:
            name (str): The name of the stream to stop. This is either the user selected name when sending the <StartStream> verb, or the system generated name returned in the Media Stream Started webhook if <StartStream> was sent with no name attribute.
        """
        self.name = name
        super().__init__(
            tag="StopStream",
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
        }
