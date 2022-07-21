"""
speak_sentence.py

Representation of Bandwidth's speak sentence BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

import re

SPEAK_SENTENCE_TAG = "SpeakSentence"
SSML_REGEX = r"&lt;([a-zA-Z//].*?)&gt;"

class SpeakSentence(AbstractBxmlVerb):

    def __init__(self, sentence=None, voice=None, locale=None, gender=None):
        """
        Initializes the SpeakSentence class with the following parameters

        :param str sentence: The sentence to speak 
        :param str voice: The voice to speak the sentence
        :param str locale: The locale of the voice
        :param str gender: The gender of the voice
        """
        self.sentence = sentence
        self.voice = voice
        self.locale = locale
        self.gender = gender

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(SPEAK_SENTENCE_TAG)
        if self.sentence is not None:
            root.text = self.sentence
        if self.voice is not None:
            root.set("voice", self.voice)
        if self.locale is not None:
            root.set("locale", self.locale)
        if self.gender is not None:
            root.set("gender", self.gender)
        return root

    def to_bxml(self):
        return re.sub(SSML_REGEX, r"<\1>", etree.tostring(self.to_etree_element()).decode()) 
