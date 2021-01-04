"""
gather.py

Representation of Bandwidth's gather BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb
from .speak_sentence import SSML_REGEX

import re

GATHER_TAG = "Gather"


class Gather(AbstractBxmlVerb):

    def __init__(self, gather_url=None, gather_method=None, terminating_digits=None, tag=None, max_digits=None,
                inter_digit_timeout=None, username=None, password=None, first_digit_timeout=None,
                play_audio=None, speak_sentence=None, repeat_count=None, nested_verbs=None,
                gather_fallback_url=None, gather_fallback_method=None, fallback_username=None,
                fallback_password=None):
        """
        Initializes the Gather class with the following parameters
        
        :param str gather_url: The url to receive the gather callback
        :param str gather_method: The HTTP method used to send the gather callback
        :param str terminating_digits: The digits used to terminate the gather
        :param str tag: Custom string included in callbacks
        :param int max_digits: Max digits to press in the gather
        :param int inter_digit_timeout: Seconds allowed between digit presses before terminating the gather
        :param str username: The username for callback http authentication
        :param str password: The password for callback http authentication
        :param int first_digit_timeout: Seconds allowed before the first digit press before terminating the gather
        :param PlayAudio play_audio: The PlayAudio tag to include in the gather
        :param SpeakSentence speak_sentence: The SpeakSentence tag to include in the gather
        :param int repeat_count: The number of times to repeat the audio prompt
        :param list<PlayAudio|SpeakSentence> nested_verbs: The list of verbs to nest in the gather
        :param str gather_fallback_url: Fallback url for gather events
        :param str gather_fallback_method: HTTP method for fallback requests
        :param str fallback_username: Basic auth username for fallback requests
        :param str fallback_password: Basic auth password for fallback requests
        """

        self.gather_url = gather_url
        self.gather_method = gather_method
        self.terminating_digits = terminating_digits
        self.tag = tag
        self.max_digits = max_digits
        self.inter_digit_timeout = inter_digit_timeout
        self.username = username
        self.password = password
        self.first_digit_timeout = first_digit_timeout
        self.play_audio = play_audio
        self.speak_sentence = speak_sentence
        self.repeat_count = repeat_count
        self.nested_verbs = nested_verbs
        self.gather_fallback_url = gather_fallback_url
        self.gather_fallback_method = gather_fallback_method
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password

    def to_bxml(self):
        root = etree.Element(GATHER_TAG)
        if self.gather_url is not None:
            root.set("gatherUrl", self.gather_url)
        if self.gather_method is not None:
            root.set("gatherMethod", self.gather_method)
        if self.terminating_digits is not None:
            root.set("terminatingDigits", self.terminating_digits)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.max_digits is not None:
            root.set("maxDigits", str(self.max_digits))
        if self.inter_digit_timeout is not None:
            root.set("interDigitTimeout", str(self.inter_digit_timeout))
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.first_digit_timeout is not None:
            root.set("firstDigitTimeout", str(self.first_digit_timeout))
        if self.repeat_count is not None:
            root.set("repeatCount", str(self.repeat_count))
        if self.gather_fallback_url is not None:
            root.set("gatherFallbackUrl", self.gather_fallback_url)
        if self.gather_fallback_method is not None:
            root.set("gatherFallbackMethod", self.gather_fallback_method)
        if self.fallback_username is not None:
            root.set("fallbackUsername", self.fallback_username)
        if self.fallback_password is not None:
            root.set("fallbackPassword", self.fallback_password)
        if self.play_audio is not None:
            root.append(self.play_audio.to_etree_element())
        if self.speak_sentence is not None:
            root.append(self.speak_sentence.to_etree_element())
        if self.nested_verbs is not None:
            for verb in self.nested_verbs:
                root.append(verb.to_etree_element())
        return re.sub(SSML_REGEX, r"<\1>", etree.tostring(root).decode())
