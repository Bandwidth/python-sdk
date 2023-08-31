"""
hangup.py

Bandwidth's Hangup BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class Hangup(TerminalVerb):

    def __init__(self):
        """Initialize a <Hangup> verb

        Args:
            None
        """
        super().__init__(tag="Hangup")
