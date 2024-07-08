"""
send_dtmf.py

Bandwidth's SendDtmf BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class SendDtmf(Verb):

    def __init__(
        self, digits: str,
        tone_duration: int=None,
        tone_interval: int=None,
    ):
        """Initialize a <SendDtmf> verb

        Args:
            digits (str): String containing the DTMF characters to be sent in a call. Allows a maximum of 50 characters. The digits will be sent one-by-one with a marginal delay.
            tone_duration (int, optional): The length (in milliseconds) of each DTMF tone. Default value is 200. Range: decimal values between 50 - 5000.
            tone_interval (int, optional): The duration of silence (in milliseconds) following each DTMF tone. Default value is 400. Range: decimal values between 50 - 5000.
        """
        self.digits = digits
        self.tone_duration = tone_duration
        self.tone_interval = tone_interval
        super().__init__(
            tag="SendDtmf",
            content=self.digits
        )

    @property
    def _attributes(self):
        return {
            "toneDuration": self.tone_duration,
            "toneInterval": self.tone_interval
        }
