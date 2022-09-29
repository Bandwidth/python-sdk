"""
bridge.py

Bandwidth's Bridge BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Tag(Verb):

    # TODO: Finish adding attributes
    def __init__(self, target_call, bridge_complete_url=None, bridge_complete_method=None):
        super().__init__(tag="Bridge", content=target_call, attributes=None, nested_verbs=None)
    
    def add_verb(self, verb: Verb):
        raise AttributeError('Adding verbs is not supported by <Bridge>')
