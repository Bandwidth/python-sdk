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
        self.content = content
        super().__init__(tag="Tag", content=self.content)
