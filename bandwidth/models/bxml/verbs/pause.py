"""
pause.py

Bandwidth's Pause BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Pause(Verb):
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
