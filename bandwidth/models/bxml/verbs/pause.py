"""
pause.py

Bandwidth's Pause BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class Pause(TerminalVerb):
    def __init__(self, duration:int=1):
        """Initialize a <Pause> verb
        Args:
            duration (str, optional): The time in seconds to pause. Default value is 1.
        """
        self.duration = str(duration)

        super().__init__(tag="Pause")

    @property
    def _attributes(self):
        return {
            "duration": self.duration
        }
