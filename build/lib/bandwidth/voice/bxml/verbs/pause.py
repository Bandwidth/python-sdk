"""
pause.py

Representation of Bandwidth's pause BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

PAUSE_TAG = "Pause"


class Pause(AbstractBxmlVerb):

    def __init__(self, duration):
        """
        Initializes the Pause class with the duration parameter

        :param float duration: The time in seconds to pause
        """
        self.duration = duration

    def to_bxml(self):
        root = etree.Element(PAUSE_TAG)
        if self.duration is not None:
            root.set("duration", str(self.duration))
        return etree.tostring(root).decode()
