"""
tag.py

Bandwidth's Tag BXML verb

@copyright Bandwidth INC
"""
from ..verb import BxmlVerb


class Tag(BxmlVerb):

    def __init__(self, content=""):
        super().__init__(tag="Tag", attributes=None, content=content, nested_verbs=None)
    
    def add_verb(self) -> Exception:
        raise AttributeError('Adding verbs is not supported by <Tag>')
