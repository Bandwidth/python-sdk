"""
endpoint.py

Bandwidth's Endpoint BXML verb (used within Connect)

@copyright Bandwidth INC
"""
from ..verb import Verb


class Endpoint(Verb):

    def __init__(self, endpoint_id: str):
        """Initialize an <Endpoint> verb

        Args:
            endpoint_id (str): The ID of the endpoint to connect to.
        """
        self.endpoint_id = endpoint_id
        super().__init__(
            tag="Endpoint",
            content=endpoint_id
        )

    @property
    def _attributes(self):
        return None
