"""
ring.py

Representation of Bandwidth's ring BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

RING_TAG = "Ring"


class Ring(AbstractBxmlVerb):

    def __init__(self, duration=None, answer_call=None):
        """
        Initializes the Ring class with the duration parameter

        :param float duration: The time in seconds to ring
        :param boolean answer_call: Whether or not to accept the incoming call while playing the ring
        """
        self.duration = duration
        self.answer_call = answer_call

    def to_bxml(self):
        root = etree.Element(RING_TAG)
        if self.duration is not None:
            root.set("duration", str(self.duration))
        if self.answer_call is not None:
            root.set("answerCall", str(self.answer_call))
        return etree.tostring(root).decode()
