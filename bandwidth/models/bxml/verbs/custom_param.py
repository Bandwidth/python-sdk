"""
custom_param.py

Bandwidth's Custom Param BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class CustomParam(TerminalVerb):
    def __init__(self, name: str = None, value: str = None):
        """
        Initialize a <CustomParam> verb
        :param name:
        :param value:
        """
        self.name = name
        self.value = value

        super().__init__(
            tag="CustomParam",
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
            "value": self.value,
        }
