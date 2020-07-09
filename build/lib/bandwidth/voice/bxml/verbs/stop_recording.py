"""
stop_recording.py

Representation of Bandwidth's StopRecording BXML verb

@copyright Bandwidth INC
"""

from .base_verb import AbstractBxmlVerb


class StopRecording(AbstractBxmlVerb):

    def to_bxml(self):
        return "<StopRecording/>"
