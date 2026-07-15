"""
refer_sip_uri.py

Bandwidth's ReferSipUri BXML element

@copyright Bandwidth INC
"""
from ..verb import Verb


class ReferSipUri(Verb):

    def __init__(self, uri: str):
        """Initialize a <SipUri> child element for use within <Refer>.

        Unlike the SipUri used with <Transfer>, this element carries only the
        destination URI — no transfer callbacks, auth, or UUI headers apply
        to a SIP REFER.

        Args:
            uri (str): The SIP URI to refer the call to (e.g. sip:user@host.example.com).
        """
        self.uri = uri
        super().__init__(
            tag="SipUri",
            content=self.uri,
        )

    @property
    def _attributes(self):
        return None
