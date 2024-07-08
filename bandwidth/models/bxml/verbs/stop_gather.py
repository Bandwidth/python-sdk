"""
stop_gather.py

Bandwidth's StopGather BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StopGather(Verb):

    def __init__(self):
        """Initialize a <StopGather> verb
        """
        super().__init__(tag="StopGather", content=None)
