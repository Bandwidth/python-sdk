"""
forward.py

Bandwidth's Forward BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Forward(Verb):

    def __init__(
        self, to: str=None, _from: str=None, 
        call_timeout: str=None, diversion_treatment: str=None, 
        diversion_reason: str=None, uui: str=None
    ):
        """Initialize a <Forward> verb

        Args:
            to (str): The phone number destination of the call.
            _from (str, optional): The phone number that the recipient will receive the call from.
            call_timeout (str, optional): The number of seconds to wait before timing out the call.
            diversion_treatment (str, optional): Can be any of the following:
                none: No diversion headers are sent on the outbound leg of the transferred call.
                propagate: Copy the Diversion header from the inbound leg to the outbound leg. Ignored if there is no Diversion header present on the inbound leg.
                stack: After propagating any Diversion header from the inbound leg to the outbound leg, stack on top another Diversion header based on the Request-URI of the inbound call.

                Defaults to none. If diversionTreatment is not specified, no diversion header will be included for the transfer even if one came with the inbound call. Defaults to None.
            diversion_reason (str, optional): Can be any of the following values:
                unknown
                user-busy
                no-answer
                unavailable
                unconditional
                time-of-day
                do-not-disturb
                deflection
                follow-me
                out-of-service
                away

                This parameter is considered only when diversionTreatment is set to stack. Defaults is unknown. 
                Defaults to None.
            uui (str, optional): The value of the User-To-User header to send within the outbound INVITE when forwarding to a SIP URI. 
                Must include the encoding parameter as specified in RFC 7433. Only base64 and jwt encoding are currently allowed. 
                This value, including the encoding specifier, may not exceed 256 characters.
        """
        self.to = to
        self._from = _from
        self.call_timeout = call_timeout
        self.diversion_treatment = diversion_treatment
        self.diversion_reason = diversion_reason
        self.uui = uui

        super().__init__(tag="Forward")

    @property
    def _attributes(self):
        return {
            "to": self.to,
            "_from": self._from,
            "callTimeout": self.call_timeout,
            "diversionTreatment": self.diversion_treatment,
            "diversionReason": self.diversion_reason,
            "uui": self.uui,
        }        
