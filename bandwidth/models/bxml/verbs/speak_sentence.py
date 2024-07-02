"""
speak_sentence.py

Bandwidth's SpeakSentence BXML verb

@copyright Bandwidth INC
"""
import re

import xml.etree.ElementTree as ET

from ..nestable_verb import NestableVerb


class SpeakSentence(NestableVerb):

    def __init__(
        self, text: str, voice: str=None, 
        gender: str=None, locale: str=None
    ):
        """Initialize a <SpeakSentence> verb

        Args:
            text (str): The text to speak. Cannot be blank. Can be a mixture of plain text and SSML tags. 
                You can find a list of supported SSML tags here: https://dev.bandwidth.com/docs/voice/bxml/speakSentence/#supported-ssml-tags
            voice (str, optional): Selects the voice of the speaker. Consult the voice column in the below table for valid values.
                If the voice attribute is present, gender and locale are ignored. You can find a list of supported voices here: https://dev.bandwidth.com/docs/voice/bxml/speakSentence/#supported-voices
            gender (str, optional): Selects the gender of the speaker. Valid values are "male" or "female". Default "female".
            locale (str, optional): Selects the locale of the speaker. Consult the locale column in the below table for valid values. Default "en_US"
        """
        self.text = text
        self.voice = voice
        self.gender = gender
        self.locale = locale
        super().__init__(
            tag="SpeakSentence",
            content=self.text,
        )

    @property
    def _attributes(self):
        return {
            "voice": self.voice,
            "gender": self.gender,
            "locale": self.locale,
        }

    def to_bxml(self) -> str:
        xml_document = self._generate_xml()
        return re.sub(self.ssml_regex, r"<\1>", ET.tostring(xml_document._root).decode('utf8'))
