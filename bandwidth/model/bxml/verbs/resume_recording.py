"""
resume_recording.py

Representation of Bandwidth's ResumeRecording BXML verb

@copyright Bandwidth INC
"""

from .base_verb import AbstractBxmlVerb


class ResumeRecording(AbstractBxmlVerb):

    def to_bxml(self):
        return "<ResumeRecording/>"
