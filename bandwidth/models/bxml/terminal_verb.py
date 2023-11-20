"""
terminal_verb.py

Defines the terminal_verb class BXML verbs that cant have nested_verbs

@copyright Bandwidth INC
"""
from .verb import Verb


class TerminalVerb(Verb):
    """Base class for BXML verbs
    """

    def __init__(self, tag: str, content: str = None):
        """Initialize the verb model

        Args:
            tag (str): Name of the XML element
            content (str, optional): XML element content. Defaults to None.
        """
        super().__init__(tag=tag, content=content, nested_verbs=None)

    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for this class

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for this verb
        """
        raise AttributeError('Adding verbs is not supported by this verb')
