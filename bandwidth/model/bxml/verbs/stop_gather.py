"""
stopGather.py

Representation of Bandwidth's stopGather BXML verb

@copyright Bandwidth INC
"""

from .base_verb import AbstractBxmlVerb


class StopGather(AbstractBxmlVerb):

    def to_bxml(self):
        return "<StopGather/>"
