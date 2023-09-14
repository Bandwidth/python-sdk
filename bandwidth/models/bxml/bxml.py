"""
bxml.py

Class that allows user to generate a Bxml document

@copyright Bandwidth INC
"""
from typing import List

from .root import Root
from .verb import Verb


class Bxml(Root):
    def __init__(self, nested_verbs: List[Verb] = []):
        """Initialize an instance of the <Bxml> root

        Args:
            nested_verbs (list[BxmlVerb], optional): Optional nested verbs to create the model with. Defaults to [].
        """
        super().__init__(tag="Bxml", nested_verbs=nested_verbs)
