"""
stop_transcription.py

Representation of Bandwidth's StartTranscription BXML verb

@license MIT
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

STOP_TRANSCRIPTION_TAG = "StopTranscription"


class StopTranscription(AbstractBxmlVerb):

    def __init__(
            self,
            name: str = None
    ):
        """
        Initializes the StopTranscription class
        :param name: The name of the real-time transcription to stop. This is either the user selected name when sending the <StartTranscription> verb, or the system generated name returned in the Real-Time Transcription Started webhook if <StartTranscription> was sent with no name attribute. If no name is specified, then all active call transcriptions will be stopped.
        """
        self.name = name

    def to_bxml(self):
        root = etree.Element(STOP_TRANSCRIPTION_TAG)
        if self.name is not None:
            root.set("name", self.name)
        return etree.tostring(root).decode()
