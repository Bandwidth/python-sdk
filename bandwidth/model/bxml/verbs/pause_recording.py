"""
pause_recording.py

Bandwidth's PauseRecording BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class PauseRecording(TerminalVerb):

    def __init__(self):
        """Initialize a <PauseRecording> verb
        """
        super().__init__(tag="PauseRecording")
