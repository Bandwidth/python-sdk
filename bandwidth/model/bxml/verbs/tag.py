"""
tag.py

Bandwidth's Tag BXML verb

@copyright Bandwidth INC
"""
from ..verb import BxmlVerb


class Tag(BxmlVerb):

    def __init__(self, content=""):
        """Initialize a <Tag> verb

        Args:
            content (str, optional): Custom tag value. Defaults to "".
        """
        super().__init__(tag="Tag", attributes=None, content=content, nested_verbs=None)
    
    def add_verb(self):
        """Adding verbs is not allowed for <Tag>

        Raises:
            AttributeError: This method is not allowed for <Tag>
        """
        raise AttributeError('Adding verbs is not supported by <Tag>')
