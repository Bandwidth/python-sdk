"""
response.py

Class that allows user to generate a Response document

@copyright Bandwidth INC
"""
from .root import BxmlRoot


class Response(BxmlRoot):
    def __init__(self, tag="Response"):
        super().__init__(tag=tag)
