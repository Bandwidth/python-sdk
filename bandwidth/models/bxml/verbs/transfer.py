"""
transfer.py

Bandwidth's Transfer BXML verb

@copyright Bandwidth INC
"""
from typing import Union, List

from ..nestable_verb import NestableVerb
from ..verbs.phone_number import PhoneNumber
from ..verbs.sip_uri import SipUri


class Transfer(NestableVerb):

    def __init__(
        self, transfer_to: List[Union[PhoneNumber, SipUri]] = [],
        transfer_caller_id: str=None, transfer_caller_display_name: str=None, call_timeout: str=None,
        transfer_complete_url: str=None, transfer_complete_method: str=None,
        transfer_complete_fallback_url: str=None,
        transfer_complete_fallback_method: str=None, username: str=None,
        password: str=None, fallback_username: str=None,
        fallback_password: str=None, tag: str=None,
        diversion_treatment: str=None, diversion_reason: str=None
    ):
        """Initialize a <Transfer> verb

        Args:
            transfer_to (list[PhoneNumber, SipUri], optional): List of recipients to transfer a call to. Defaults to [].
            transfer_caller_id (str, optional): The caller ID to use when the call is transferred, if different. Must be in E.164 format (e.g. +15555555555) or be one of the following strings Restricted, Anonymous, Private, or Unavailable. Leave as default to pass along the number of the remote party. Defaults to None.
            transfer_caller_display_name (str, optional): The caller display name to use when the call is transferred. May not exceed 256 characters nor contain control characters such as new lines.
            call_timeout (str, optional):The timeout (in seconds) for the callee to answer the call after it starts ringing. If the call does not start ringing within 30s, the call will be cancelled regardless of this value. Range: decimal values between 1 - 300. Default value is 30 seconds. Defaults to None.
            transfer_complete_url (str, optional): URL to send the Transfer Complete event to and request new BXML. Optional but recommended. See below for further details. May be a relative URL. Defaults to None.
            transfer_complete_method (str, optional): The HTTP method to use for the request to transferCompleteUrl. GET or POST. Default value is POST. Defaults to None.
            transfer_complete_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Transfer Complete callback delivery in case transferCompleteUrl fails to respond. Defaults to None.
            transfer_complete_fallback_method (str, optional): The HTTP method to use to deliver the Transfer Complete callback to transferCompleteFallbackUrl. GET or POST. Default value is POST. Defaults to None.
            username (str, optional): The username to send in the HTTP request to transferCompleteUrl. Defaults to None.
            password (str, optional): The password to send in the HTTP request to transferCompleteUrl. Defaults to None.
            fallback_username (str, optional): The username to send in the HTTP request to transferCompleteFallbackUrl. Defaults to None.
            fallback_password (str, optional): The password to send in the HTTP request to transferCompleteFallbackUrl. Defaults to None.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or cleared. May be cleared by setting tag="" Max length 256 characters. Defaults to None.
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
        """
        self.transfer_to = transfer_to
        self.transfer_caller_id = transfer_caller_id
        self.transfer_caller_display_name = transfer_caller_display_name
        self.call_timeout = call_timeout
        self.transfer_complete_url = transfer_complete_url
        self.transfer_complete_method = transfer_complete_method
        self.transfer_complete_fallback_url = transfer_complete_fallback_url
        self.transfer_complete_fallback_method = transfer_complete_fallback_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.diversion_treatment = diversion_treatment
        self.diversion_reason = diversion_reason
        super().__init__(
            tag="Transfer",
            nested_verbs=self.transfer_to
        )

    @property
    def _attributes(self):
        return {
            "transferCallerId": self.transfer_caller_id,
            "transferCallerDisplayName": self.transfer_caller_display_name,
            "callTimeout": self.call_timeout,
            "transferCompleteUrl": self.transfer_complete_url,
            "transferCompleteMethod": self.transfer_complete_method,
            "transferCompleteFallbackUrl": self.transfer_complete_fallback_url,
            "transferCompleteFallbackMethod": self.transfer_complete_fallback_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
            "diversionTreatment": self.diversion_treatment,
            "diversionReason": self.diversion_reason
        }

    def add_transfer_recipient(self, recipient: Union[PhoneNumber, SipUri]):
        super().add_verb(recipient)
