"""
start_recording.py

Bandwidth's StartRecording BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class StartRecording(Verb):

    def __init__(
        self, recording_available_url: str = None,
        recording_available_method: str = None,
        transcribe: bool = None, transcription_available_url: str = None,
        transcription_available_method: str = None,  username: str=None,
        password: str=None, tag: str=None,
        file_format: str = None, multi_channel: bool = None
    ):
        """Initialize a <StartRecording> verb

        Args:
            recording_available_url (str, optional): URL to send the Recording Available event to once it has been processed. Does not accept BXML. May be a relative URL. Defaults to None.
            recording_available_method (str, optional): The HTTP method to use for the request to recordingAvailableUrl. GET or POST. Default value is POST.
            transcribe (str, optional): A boolean value to indicate that recording should be transcribed. Transcription can succeed only for recordings of length greater than 500 milliseconds and less than 4 hours. Default is false. Defaults to None.
            transcription_available_url (str, optional): URL to send the Transcription Available event to once it has been processed. Does not accept BXML. May be a relative URL. Defaults to None.
            transcription_available_method (str, optional): The HTTP method to use for the request to transcriptionAvailableUrl. GET or POST. Default value is POST. Defaults to None.
            username (str, optional): The username to send in the HTTP request to recordCompleteUrl, recordingAvailableUrl or transcriptionAvailableUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            password (str, optional): The password to send in the HTTP request to recordCompleteUrl, recordingAvailableUrl or transcriptionAvailableUrl. If specified, the URLs must be TLS-encrypted (i.e., https). Defaults to None.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or <Tag> verb, or cleared. May be cleared by setting tag="". Max length 256 characters. Defaults to None.
            file_format (str, optional): The audio format that the recording will be saved as: mp3 or wav. Default value is wav. Defaults to None.            max_duration (str, optional): Maximum length of recording (in seconds). Max 10800 (3 hours). Default value is 60. Defaults to None.
            multi_channel (str, optional): A boolean value indicating whether or not the recording file should separate each side of the call into its own audio channel. Default value is false.

        """
        self.recording_available_url = recording_available_url
        self.recording_available_method = recording_available_method
        self.transcribe = transcribe
        self.transcription_available_url = transcription_available_url
        self.transcription_available_method = transcription_available_method
        self.username = username
        self.password = password
        self.tag = tag
        self.file_format = file_format
        self.multi_channel = multi_channel
        super().__init__(tag="StartRecording")

    @property
    def _attributes(self):
        return {
            "recordingAvailableUrl": self.recording_available_url,
            "recordingAvailableMethod": self.recording_available_method,
            "transcribe": self.transcribe,
            "transcriptionAvailableUrl": self.transcription_available_url,
            "transcriptionAvailableMethod": self.transcription_available_method,
            "username": self.username,
            "password": self.password,
            "tag": self.tag,
            "fileFormat": self.file_format,
            "multiChannel": self.multi_channel
        }
