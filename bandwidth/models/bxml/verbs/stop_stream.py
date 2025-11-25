"""
stop_stream.py

Bandwidth's StopStream BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StopStream(Verb):

    def __init__(
        self, name: str, wait: bool = None
    ):
        """Initialize a <StopStream> verb

        Args:
            name (str): The name of the stream to stop. This is either the user selected name when sending the <StartStream> verb, or the system generated name returned in the Media Stream Started webhook if <StartStream> was sent with no name attribute.
            wait (bool, optional): If true, the BXML interpreter will wait for the stream to stop before processing the next verb.
        """
        self.name = name
        self.wait = wait
        super().__init__(
            tag="StopStream",
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
            "wait": self.wait,
        }
