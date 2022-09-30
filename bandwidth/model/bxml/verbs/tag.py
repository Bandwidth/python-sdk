"""
tag.py

Bandwidth's Tag BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class Tag(TerminalVerb):

    def __init__(self, content=""):
        """Initialize a <Tag> verb

        Args:
            content (str, optional): Custom tag value. Defaults to "".
        """
        super().__init__(tag="Tag", content=content, attributes=None, nested_verbs=None)
