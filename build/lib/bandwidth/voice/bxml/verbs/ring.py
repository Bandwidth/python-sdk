"""
ring.py

Representation of Bandwidth's ring BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

RING_TAG = "Ring"


class Ring(AbstractBxmlVerb):

    def __init__(self, duration):
        """
        Initializes the Ring class with the duration parameter

        :param float duration: The time in seconds to ring
        """
        self.duration = duration

    def to_bxml(self):
        root = etree.Element(RING_TAG)
        if self.duration is not None:
            root.set("duration", str(self.duration))
        return etree.tostring(root).decode()
