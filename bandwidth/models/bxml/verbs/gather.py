"""
gather.py

Bandwidth's Gather BXML verb

@copyright Bandwidth INC
"""
from typing import Union, List
from ..nestable_verb import NestableVerb
from .play_audio import PlayAudio
from .speak_sentence import SpeakSentence


class Gather(NestableVerb):

    def __init__(
        self, audio_verbs: List[Union[PlayAudio, SpeakSentence]] = [],
        gather_url: str=None, gather_method: str=None,
        gather_fallback_url: str=None, gather_fallback_method: str=None,
        username: str=None, password: str=None,
        fallback_username: str=None, fallback_password: str=None,
        tag: str=None, terminating_digits: str=None,
        max_digits: int=None, inter_digit_timeout: int=None,
        first_digit_timeout: int=None, repeat_count: int=None,
        input: str=None, hints: str=None,
        language: str=None, partial_result_callback: str=None,
        partial_result_callback_method: str=None, profanity_filter: bool=None,
        speech_model: str=None, speech_timeout: int=None
    ):
        """Initialize a <Gather> verb

        Args:
            gather_url (str, optional): URL to send Gather event to and request new BXML. May be a relative URL.
            gather_method (str, optional): The HTTP method to use for the request to gather_url. GET or POST. Default value is POST.
            gather_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Gather event callback delivery in case gather_url fails to respond.
            gather_fallback_method (str, optional): The HTTP method to use to deliver the Gather event callback to gather_fallback_url. GET or POST. Default value is POST.
            username (str, optional): The username to send in the HTTP request to gather_url.
            password (str, optional): The password to send in the HTTP request to gather_url.
            fallback_username (str, optional): The username to send in the HTTP request to gather_fallback_url.
            fallback_password (str, optional): The password to send in the HTTP request to gather_fallback_url.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or <Tag> verb, or cleared.
                May be cleared by setting tag="". Max length 256 characters.
            terminating_digits (str, optional): When any of these digits are pressed, it will terminate the Gather. Default value is "", which disables this feature.
            max_digits (int, optional): Max number of digits to collect. Default value is 50. Range: decimal values between 1 - 50.
            inter_digit_timeout (int, optional): Time (in seconds) allowed between digit presses before automatically terminating the Gather. Default value is 5. Range: decimal values between 1 - 60.
            first_digit_timeout (int, optional): Time (in seconds) to pause after any audio from nested <SpeakSentence> or <PlayAudio> verb is played (in seconds) before terminating the Gather.
                Default value is 5. Range: decimal values between 0 - 60.
            repeat_count (int, optional): The number of times the audio prompt should be played if no digits are pressed. For example, if this value is 3, the nested audio clip will be played a maximum of three times.
                The delay between repetitions will be equal to first_digit_timeout. Default value is 1. repeat_count * number of verbs must not be greater than 20.
            input (str, optional): The kind of input to collect: dtmf, speech, or dtmf_speech. Default value is dtmf.
            hints (str, optional): Words or phrases that provide context to the speech recognition engine, improving accuracy for expected responses. Only used when input includes speech.
            language (str, optional): The language code used for speech recognition, for example en-US. Only used when input includes speech.
            partial_result_callback (str, optional): URL to send the Partial Result event to as speech is recognized. May be a relative URL. Only used when input includes speech.
            partial_result_callback_method (str, optional): The HTTP method to use for the request to partial_result_callback. GET or POST. Default value is POST.
            profanity_filter (bool, optional): A boolean value to indicate whether profane words are filtered out of the transcription. Default value is true. Only used when input includes speech.
            speech_model (str, optional): The speech recognition model to use for transcribing the caller's speech. Only used when input includes speech.
            speech_timeout (int, optional): Time (in seconds) to wait for speech input before terminating the Gather. Default value is 5. Only used when input includes speech.

        Nested Verbs:
            PlayAudio: (optional) Using the PlayAudio inside the Gather verb will play the media until a digit is received.
            SpeakSentence: (optional) Using the SpeakSentence inside the Gather verb will speak the text until a digit is received.
        """
        self.gather_url = gather_url
        self.gather_method = gather_method
        self.gather_fallback_url = gather_fallback_url
        self.gather_fallback_method = gather_fallback_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.terminating_digits = terminating_digits
        self.max_digits = max_digits
        self.inter_digit_timeout = inter_digit_timeout
        self.first_digit_timeout = first_digit_timeout
        self.repeat_count = repeat_count
        self.input = input
        self.hints = hints
        self.language = language
        self.partial_result_callback = partial_result_callback
        self.partial_result_callback_method = partial_result_callback_method
        self.profanity_filter = profanity_filter
        self.speech_model = speech_model
        self.speech_timeout = speech_timeout
        self.audio_verbs = audio_verbs
        super().__init__(
            tag="Gather",
            nested_verbs=self.audio_verbs)

    @property
    def _attributes(self):
        return {
            "gatherUrl": self.gather_url,
            "gatherMethod": self.gather_method,
            "gatherFallbackUrl": self.gather_fallback_url,
            "gatherFallbackMethod": self.gather_fallback_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
            "terminatingDigits": self.terminating_digits,
            "maxDigits": self.max_digits,
            "interDigitTimeout": self.inter_digit_timeout,
            "firstDigitTimeout": self.first_digit_timeout,
            "repeatCount": self.repeat_count,
            "input": self.input,
            "hints": self.hints,
            "language": self.language,
            "partialResultCallback": self.partial_result_callback,
            "partialResultCallbackMethod": self.partial_result_callback_method,
            "profanityFilter": self.profanity_filter,
            "speechModel": self.speech_model,
            "speechTimeout": self.speech_timeout,
        }
