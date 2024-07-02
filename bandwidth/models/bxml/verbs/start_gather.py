"""
start_gather.py

Bandwidth's StartGather BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StartGather(Verb):

    def __init__(
        self, dtmf_url: str, dtmf_method: str=None, username: str=None,
        password: str=None, tag: str=None,
    ):
        """Initialize a <StartGather> verb

        Args:
            dtmf_url (str): URL to send the DTMF event to. May be a relative URL..
            dtmf_method (str, optional): The HTTP method to use for the request to dtmfUrl. GET or POST. Default value is POST. Defaults to None.
            username (str, optional): The username to send in the HTTP request to dtmfUrl. Defaults to None.
            password (str, optional): The password to send in the HTTP request to dtmfUrl. Defaults to None.
            tag (str, optional):  A custom string that will be sent with these and all future callbacks unless overwritten by a future tag attribute or cleared. May be cleared by setting tag="" Max length 256 characters. Defaults to None.
        """
        self.dtmf_url = dtmf_url
        self.dtmf_method = dtmf_method
        self.username = username
        self.password = password
        self.tag = tag
        super().__init__(
            tag="StartGather"
        )

    @property
    def _attributes(self):
        return {
            "dtmfUrl": self.dtmf_url,
            "dtmfMethod": self.dtmf_method,
            "username": self.username,
            "password": self.password,
            "tag": self.tag
        }
