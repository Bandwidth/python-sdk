"""
refer.py

Bandwidth's Refer BXML verb

@copyright Bandwidth INC
"""
from ..nestable_verb import NestableVerb
from .sip_uri import SipUri


class Refer(NestableVerb):

    def __init__(
        self, sip_uri: SipUri,
        refer_complete_url: str=None, refer_complete_method: str=None,
        tag: str=None
    ):
        """Initialize a <Refer> verb

        The <Refer> verb sends a SIP REFER to the remote endpoint, asking it
        to redirect the call to a new SIP URI. Unlike <Transfer>, a successful
        REFER terminates the call on Bandwidth's side: the remote endpoint
        redirects away from Bandwidth entirely. This is a SIP protocol
        property, not a Bandwidth design choice. As a result, BXML returned in
        response to the referComplete callback is only meaningful for failure
        handling — there is no live call to act on after success.

        Args:
            sip_uri (SipUri): The SIP URI to refer the call to. Required.
                Exactly one <SipUri> child element is allowed.
            refer_complete_url (str, optional): URL to send the Refer Complete
                event to when the REFER flow finishes (success or failure).
                May be a relative URL. Defaults to None.
            refer_complete_method (str, optional): The HTTP method to use for
                the request to referCompleteUrl. GET or POST. Default value
                is POST. Defaults to None.
            tag (str, optional): A custom string that will be sent with this
                and all future callbacks unless overwritten by a future tag
                attribute or cleared. May be cleared by setting tag="". Max
                length 256 characters. Defaults to None.
        """
        self.sip_uri = sip_uri
        self.refer_complete_url = refer_complete_url
        self.refer_complete_method = refer_complete_method
        self.tag = tag
        super().__init__(
            tag="Refer",
            nested_verbs=[self.sip_uri]
        )

    @property
    def _attributes(self):
        return {
            "referCompleteUrl": self.refer_complete_url,
            "referCompleteMethod": self.refer_complete_method,
            "tag": self.tag
        }
