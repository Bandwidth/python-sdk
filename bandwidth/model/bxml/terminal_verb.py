"""
verb.py

Defines the base verb class for all BXML verbs

@copyright Bandwidth INC
"""
from .verb import Verb


class TerminalVerb(Verb):
    """Base class for BXML verbs
    """

    def __init__(self, tag: str, content: str = None, attributes: dict = None, nested_verbs: list[Verb] = None):
        """Initialize the verb model

        Args:
            tag (str): Name of the XML element
            content (str, optional): XML element content. Defaults to None.
            attributes (dict, optional): XML element attributes. Defaults to None.
            nested_verbs (list[BxmlVerb], optional): XML element children. Defaults to None.
        """
        super().__init__(tag=tag, content=content, attributes=attributes, nested_verbs=nested_verbs)

    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for this class

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for <SipUri>
        """
        raise AttributeError('Adding verbs is not supported by this verb')
