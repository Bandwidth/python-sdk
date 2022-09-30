"""
pause.py
Bandwidth's Pause BXML verb
@copyright Bandwidth INC
"""
from ..verb import Verb
class Pause(Verb):
    def __init__(self, duration:str=None):
        """Initialize a <Pause> verb
        Args:
            duration (str, optional): The time in seconds to pause. Default value is 1.
        """
        self.attributes = {
        "duration": duration
        }

        super().__init__(tag="Pause", content=None, attributes=self.attributes, nested_verbs=None)

    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for <Pause>
        Args:
            verb (Verb): BXML verb
        Raises:
            AttributeError: This method is not allowed for <Pause>
        """
        raise AttributeError('Adding verbs is not supported by <Pause>')
