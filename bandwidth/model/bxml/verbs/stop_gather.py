"""
stop_gather.py

Bandwidth's StopGather BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class StopGather(TerminalVerb):

    def __init__(self):
        """Initialize a <StopGather> verb
        """
        super().__init__(tag="StopGather", content=None)
