"""
stream_param.py

Bandwidth's StreamParam BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StreamParam(Verb):

    def __init__(
        self, name: str, value: str
    ):
        """Initialize a <StreamParam> verb

        Args:
            name (str): The name of this parameter, up to 256 characters.
            value (str): The value of this parameter, up to 2048 characters.
        """
        self.name = name
        self.value = value
        super().__init__(
            tag="StreamParam"
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
            "value": self.value,
        }
