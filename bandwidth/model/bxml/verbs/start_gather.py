"""
startGather.py

Representation of Bandwidth's startGather BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

START_GATHER_TAG = "StartGather"


class StartGather(AbstractBxmlVerb):

    def __init__(self, dtmfUrl=None, dtmfMethod=None, username=None, password=None, tag=None):
        """
        Initializes the Gather class with the following parameters

        :param str dtmfUrl: The url to receive the dtmf event
        :param str dtmfMethod: The HTTP method used to send the gather dtmfUrl event
        :param str username: The username for callback http authentication
        :param str password: The password for callback http authentication
        :param str tag:
        """

        self.dtmfUrl = dtmfUrl
        self.dtmfMethod = dtmfMethod
        self.username = username
        self.password = password
        self.tag = tag

    def to_bxml(self):
        root = etree.Element(START_GATHER_TAG)
        if self.dtmfUrl is not None:
            root.set("dtmfUrl", self.dtmfUrl)
        if self.dtmfMethod is not None:
            root.set("dtmfMethod", self.dtmfMethod)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.tag is not None:
            root.set("tag", self.tag)
        return etree.tostring(root).decode()
