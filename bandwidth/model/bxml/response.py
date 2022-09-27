"""
response.py

Class that allows user to generate a Response document

@copyright Bandwidth INC
"""
from .root import BxmlRoot
from .verb import BxmlVerb


class Response(BxmlRoot):
    def __init__(self, nested_verbs: list[BxmlVerb] = []):
        """Initialize an instance of the <Response> root

        Args:
            nested_verbs (list[BxmlVerb], optional): Optional nested verbs to create the model with. Defaults to [].
        """
        super().__init__(tag="Response", nested_verbs=nested_verbs)
