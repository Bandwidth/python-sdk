"""
conference.py

Representation of Bandwidth's conference BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

CONFERENCE_TAG = "Conference"


class Conference(AbstractBxmlVerb):

    def __init__(self, conference_name, mute=None, hold=None, call_ids_to_coach=None,
                conference_event_url=None, conference_event_method=None,
                username=None, password=None, tag=None):
        """
        Init for Conference

        :param str conference_name: The name of the conference
        :param boolean mute: Determines if conference members should be on mute
        :param boolean hold: Determines if conference members should be on hold
        :param string|list<string> call_ids_to_coach: A string of comma separated call IDs to coach, or an array of call IDs to coach
        :param string conference_event_url: The url to receive conference events
        :param string conference_event_method: The HTTP method to send conference events
        :param string username: Basic auth username for events
        :param string password: Basic auth password for events
        :param string tag: Custom tag to be included in events
        """
        self.conference_name = conference_name
        self.mute = mute
        self.hold = hold
        self.call_ids_to_coach = call_ids_to_coach
        self.conference_event_url = conference_event_url
        self.conference_event_method = conference_event_method
        self.username = username
        self.password = password
        self.tag = tag

    def to_bxml(self):
        root = etree.Element(CONFERENCE_TAG)
        root.text = self.conference_name

        if self.mute is not None:
            strn = "true" if self.mute else "false"
            root.set("mute", strn)
        if self.hold is not None:
            strn = "true" if self.hold else "false"
            root.set("hold", strn)
        if self.call_ids_to_coach is not None:
            strn = None
            if isinstance(self.call_ids_to_coach, str):
                strn = self.call_ids_to_coach
            else:
                strn = ",".join(self.call_ids_to_coach)
            root.set("callIdsToCoach", strn)
        if self.conference_event_url is not None:
            root.set("conferenceEventUrl", self.conference_event_url)
        if self.conference_event_method is not None:
            root.set("conferenceEventMethod", self.conference_event_method)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)

        return etree.tostring(root).decode()
