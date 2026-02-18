"""
connect.py

Bandwidth's Connect BXML verb

@copyright Bandwidth INC
"""
from typing import List

from ..nestable_verb import NestableVerb
from .endpoint import Endpoint


class Connect(NestableVerb):

    def __init__(
        self, destination: List[Endpoint] = [],
        event_callback_url: str = None
    ):
        """Initialize a <Connect> verb

        Args:
            destination (list[Endpoint], optional): An Endpoint ID to connect the call to.
            event_callback_url (str, optional): URL to send events to during the connection lifecycle. May be a relative URL. Defaults to None.
        """
        self.destination = destination
        self.event_callback_url = event_callback_url

        super().__init__(
            tag="Connect",
            nested_verbs=destination
        )

    @property
    def _attributes(self):
        return {
            "eventCallbackUrl": self.event_callback_url
        }
