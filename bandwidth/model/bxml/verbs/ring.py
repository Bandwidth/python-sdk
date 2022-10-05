"""
ring.py

Bandwidth's Ring BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class Ring(TerminalVerb):

    def __init__(
        self, duration: str = None,
        answer_call: str = None,
    ):
        """Initialize a <Ring> verb

        Args:
            duration (str, optional): How many seconds to play ringing on the call. Default value is 5. Range: decimal values between 0.1 - 86400.
            answer_call (str, optional): A boolean indicating whether or not to answer the call when Ring is executed on an unanswered incoming call. Default value is 'true'.
        """
        self.duration = duration
        self.answer_call = answer_call
        super().__init__(tag="Ring")

    @property
    def _attributes(self):
        return {
            "duration": self.duration,
            "answerCall": self.answer_call,
        }
