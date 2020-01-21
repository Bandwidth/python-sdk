"""
record.py

Representation of Bandwidth's redirect BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

RECORD_TAG = "Record"


class Record(AbstractBxmlVerb):

    def __init__(self, tag=None, username=None, password=None, record_complete_url=None, record_complete_method=None,
        recording_available_url=None, recording_available_method=None, terminating_digits=None, max_duration=None, file_format=None):
        """
        Initializes the Record class with the following parameters

        :param str tag: Optional tag to include in the callback
        :param str username: Username for http authentication on the redirect url
        :param str password: Password for http authentication on the redirect url
        :param str record_complete_url: URL for record complete callback
        :param str record_complete_method: HTTP method for record complete callback
        :param str recording_available_url: URL for record available callback
        :param str recording_available_method: HTTP method for record available callback
        :param str terminating_digits: Digits to terminate the recording
        :param int max_duration: Max duration to record in seconds
        :param str file_format: The file format to save the recording in
        """
        self.tag = tag
        self.username = username
        self.password = password
        self.record_complete_url = record_complete_url
        self.record_complete_method = record_complete_method
        self.recording_available_url = recording_available_url
        self.recording_available_method = recording_available_method
        self.terminating_digits = terminating_digits
        self.max_duration = max_duration
        self.file_format = file_format

    def to_bxml(self):
        root = etree.Element(RECORD_TAG)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.record_complete_url is not None:
            root.set("recordCompleteUrl", self.record_complete_url)
        if self.record_complete_method is not None:
            root.set("recordCompleteMethod", self.record_complete_method)
        if self.recording_available_url is not None:
            root.set("recordingAvailableUrl", self.recording_available_url)
        if self.recording_available_method is not None:
            root.set("recordingAvailableMethod", self.recording_available_method)
        if self.terminating_digits is not None:
            root.set("terminatingDigits", self.terminating_digits)
        if self.max_duration is not None:
            root.set("maxDuration", str(self.max_duration))
        if self.file_format is not None:
            root.set("fileFormat", self.file_format)
        return etree.tostring(root).decode()
