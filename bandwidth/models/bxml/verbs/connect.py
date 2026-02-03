"""
connect.py

Bandwidth's Connect BXML verb

@copyright Bandwidth INC
"""
from typing import Union

from ..nestable_verb import NestableVerb
from ..verbs.endpoint import Endpoint


class Connect(NestableVerb):

    def __init__(
        self, destination: Union[Endpoint, None] = None,
        event_callback_url: str = None
    ):
        """Initialize a <Connect> verb

        Args:
            destination (Endpoint, optional): The endpoint destination to connect to. Defaults to None.
            event_callback_url (str, optional): URL to send events to for this Connect verb. Defaults to None.
        """
        self.destination = destination
        self.event_callback_url = event_callback_url

        nested_verbs = []
        if destination is not None:
            nested_verbs.append(destination)

        super().__init__(
            tag="Connect",
            nested_verbs=nested_verbs
        )

    @property
    def _attributes(self):
        return {
            "eventCallbackUrl": self.event_callback_url
        }
