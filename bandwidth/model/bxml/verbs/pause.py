"""
pause.py
Bandwidth's Pause BXML verb
@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb
class Pause(TerminalVerb):
    def __init__(self, duration:str=None):
        """Initialize a <Pause> verb
        Args:
            duration (str, optional): The time in seconds to pause. Default value is 1.
        """
        self.duration = duration

        super().__init__(tag="Pause", content=None)
    @property
    def _attributes(self):
        return {
            "duration": self.duration
        }