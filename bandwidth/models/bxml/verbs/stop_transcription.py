"""
stop_transcription.py

Bandwidth's Stop Transcription BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StopTranscription(Verb):
    def __init__(
            self,
            name: str = None,
    ):
        """
        Initialize a <StopTranscription> verb
        :param name: The name of the real-time transcription to stop. This is either the user selected name when sending the <StartTranscription> verb, or the system generated name returned in the Real-Time Transcription Started webhook if <StartTranscription> was sent with no name attribute. If no name is specified, then all active call transcriptions will be stopped.
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
