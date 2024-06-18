"""
record.py

Bandwidth's Record BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Record(Verb):

    def __init__(
        self, record_complete_url: str=None,
        record_complete_method: str=None,
        record_complete_fallback_url: str=None,
        record_complete_fallback_method: str=None,
        recording_available_url: str=None,
        recording_available_method: str=None,
        transcribe: str=None, transcription_available_url: str=None,
        transcription_available_method: str=None,  username: str=None,
        password: str=None, fallback_username: str=None,
        fallback_password: str=None, tag: str=None,
        terminating_digits: str=None, max_duration: int=60,
        silence_timeout: str=None, file_format: str=None
    ):
        """Initialize a <Record> verb

        Args:
            record_complete_url (str, optional): URL to send the Record Complete event to once the recording has ended. Accepts BXML, and may be a relative URL. This callback will not be sent if the recording ended due to the call hanging up. Defaults to None.
            record_complete_method (str, optional): The HTTP method to use for the request to recordCompleteUrl. GET or POST. Default value is POST. Defaults to None.
            record_complete_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Record Complete callback delivery in case recordCompleteUrl fails to respond. Defaults to None.
            record_complete_fallback_method (str, optional): The HTTP method to use to deliver the Record Complete callback to recordCompleteFallbackUrl. GET or POST. Default value is POST. Defaults to None.
            recording_available_url (str, optional): URL to send the Recording Available event to once it has been processed. Does not accept BXML. May be a relative URL. Defaults to None.
            recording_available_method (str, optional): The HTTP method to use for the request to recordingAvailableUrl. GET or POST. Default value is POST. Defaults to None.
            transcribe (str, optional): A boolean value to indicate that recording should be transcribed. Transcription can succeed only for recordings of length greater than 500 milliseconds and less than 4 hours. Default is false. Defaults to None.
            transcription_available_url (str, optional): URL to send the Transcription Available event to once it has been processed. Does not accept BXML. May be a relative URL. Defaults to None.
            transcription_available_method (str, optional): The HTTP method to use for the request to transcriptionAvailableUrl. GET or POST. Default value is POST. Defaults to None.
            username (str, optional): The username to send in the HTTP request to recordCompleteUrl, recordingAvailableUrl or transcriptionAvailableUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            password (str, optional): The password to send in the HTTP request to recordCompleteUrl, recordingAvailableUrl or transcriptionAvailableUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            fallback_username (str, optional): The username to send in the HTTP request to recordCompleteFallbackUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            fallback_password (str, optional): The password to send in the HTTP request to recordCompleteFallbackUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or <Tag> verb, or cleared. May be cleared by setting tag="". Max length 256 characters. Defaults to None.
            terminating_digits (str, optional): When pressed, this digit will terminate the recording. Default value is “#”. This feature can be disabled with "". Defaults to None.
            max_duration (int, optional): Maximum length of recording (in seconds). Max 10800 (3 hours). Default value is 60. Defaults to None.
            silence_timeout (str, optional): Length of silence after which to end the recording (in seconds). Max is equivalent to the maximum maxDuration value. Default value is 0, which means no timeout. Defaults to None.
            file_format (str, optional): The audio format that the recording will be saved as: mp3 or wav. Default value is wav. Defaults to None.
        """
        self.record_complete_url = record_complete_url
        self.record_complete_method = record_complete_method
        self.record_complete_fallback_url = record_complete_fallback_url
        self.record_complete_fallback_method = record_complete_fallback_method
        self.recording_available_url = recording_available_url
        self.recording_available_method = recording_available_method
        self.transcribe = transcribe
        self.transcription_available_url = transcription_available_url
        self.transcription_available_method = transcription_available_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.terminating_digits = terminating_digits
        self.max_duration = max_duration
        self.silence_timeout = silence_timeout
        self.file_format = file_format

        super().__init__(tag="Record", content=None)

    @property
    def _attributes(self):
        return {
            "recordCompleteUrl": self.record_complete_url,
            "recordCompleteMethod": self.record_complete_method,
            "recordCompleteFallback_url": self.record_complete_fallback_url,
            "recordCompleteFallback_method": self.record_complete_fallback_method,
            "recordingAvailableUrl": self.recording_available_url,
            "recordingAvailableMethod": self.recording_available_method,
            "transcribe": self.transcribe,
            "transcriptionAvailableUrl": self.transcription_available_url,
            "transcriptionAvailableMethod": self.transcription_available_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
            "terminatingDigits": self.terminating_digits,
            "maxDuration": self.max_duration,
            "silenceTimeout": self.silence_timeout,
            "fileFormat": self.file_format
        }
