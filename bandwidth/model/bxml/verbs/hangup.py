"""
hangup.py

Representation of Bandwidth's hangup BXML verb

@copyright Bandwidth INC
"""

from .base_verb import AbstractBxmlVerb


class Hangup(AbstractBxmlVerb):

    def to_bxml(self):
        return "<Hangup/>"
