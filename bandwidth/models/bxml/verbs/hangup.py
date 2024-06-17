"""
hangup.py

Bandwidth's Hangup BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Hangup(Verb):

    def __init__(self):
        """Initialize a <Hangup> verb

        Args:
            None
        """
        super().__init__(tag="Hangup")
