"""
start_recording.py

Representation of Bandwidth's StartRecording BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

START_RECORDING_TAG = "StartRecording"


class StartRecording(AbstractBxmlVerb):

    def __init__(self, tag=None, username=None, password=None, recording_available_url=None, recording_available_method=None,
        file_format=None, multi_channel=None):
        """
        Initializes the Record class with the following parameters

        :param str tag: Optional tag to include in the callback
        :param str username: Username for http authentication on the redirect url
        :param str password: Password for http authentication on the redirect url
        :param str recording_available_url: URL for record available callback
        :param str recording_available_method: HTTP method for record available callback
        :param str file_format: The file format to save the recording in
        :param bool multi_channel: Whether or not to record the channels separately (default is false, 1 recording)
        """
        self.tag = tag
        self.username = username
        self.password = password
        self.recording_available_url = recording_available_url
        self.recording_available_method = recording_available_method
        self.file_format = file_format
        self.multi_channel = multi_channel

    def to_bxml(self):
        root = etree.Element(START_RECORDING_TAG)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.recording_available_url is not None:
            root.set("recordingAvailableUrl", self.recording_available_url)
        if self.recording_available_method is not None:
            root.set("recordingAvailableMethod", self.recording_available_method)
        if self.file_format is not None:
            root.set("fileFormat", self.file_format)
        if self.multi_channel is not None:
            #Convert True to "true", or False to "false"
            strn = "true" if self.multi_channel else "false"
            root.set("multiChannel", strn)
        return etree.tostring(root).decode()
