"""
play_audio.py

Representation of Bandwidth's play audio BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

PLAY_AUDIO_TAG = "PlayAudio"


class PlayAudio(AbstractBxmlVerb):

    def __init__(self, url=None, username=None, password=None):
        """
        Initializes the PlayAudio class with the following parameters

        :param str url: The url of the audio to play
        :param str username: The username to authenticate on the url
        :param str password: The password to authenticate on the url
        """
        self.url = url
        self.username = username
        self.password = password

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(PLAY_AUDIO_TAG)
        if self.url is not None:
            root.text = self.url
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
