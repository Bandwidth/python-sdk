"""
tag.py

Bandwidth's Tag BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Tag(Verb):

    def __init__(self, content=""):
        """Initialize a <Tag> verb

        Args:
            content (str, optional): Custom tag value. Defaults to "".
        """
        super().__init__(tag="Tag", content=content, attributes=None, nested_verbs=None)
    
    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for <Tag>

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for <Tag>
        """
        raise AttributeError('Adding verbs is not supported by <Tag>')
