"""
bxml.py

Class that allows user to generate a Bxml document

@copyright Bandwidth INC
"""
from .root import BxmlRoot
from .verb import BxmlVerb


class Bxml(BxmlRoot):
    def __init__(self, nested_verbs: list[BxmlVerb] = []):
        """Initialize an instance of the <Bxml> root

        Args:
            nested_verbs (list[BxmlVerb], optional): Optional nested verbs to create the model with. Defaults to [].
        """
        super().__init__(tag="Bxml", nested_verbs=nested_verbs)
