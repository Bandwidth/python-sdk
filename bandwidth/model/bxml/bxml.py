"""
bxml.py

Class that allows user to generate a Bxml document

@copyright Bandwidth INC
"""
from .root import BxmlRoot


class Bxml(BxmlRoot):
    def __init__(self, tag="Bxml"):
        super().__init__(tag=tag)
