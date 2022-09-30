"""
hangup.py

Bandwidth's Hangup BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Hangup(Verb):

    def __init__(self):
        """Initialize a <Hangup> verb

        Args:
            None
        """
        super().__init__(tag="Hangup", content=None, attributes=None, nested_verbs=None)
    
    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for <Hangup>

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for <Hangup>
        """
        raise AttributeError('Adding verbs is not supported by <Hangup>')
