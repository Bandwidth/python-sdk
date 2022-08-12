"""
pause_recording.py

Representation of Bandwidth's PauseRecording BXML verb

@copyright Bandwidth INC
"""

from .base_verb import AbstractBxmlVerb


class PauseRecording(AbstractBxmlVerb):

    def to_bxml(self):
        return "<PauseRecording/>"
