"""
conference.py

Bandwidth's Conference BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Conference(Verb):

    def __init__(
        self, name: str, mute: str=None,
        hold: str=None, call_ids_to_coach: str=None,
        conference_event_url: str=None, conference_event_method: str=None,
        conference_event_fallback_url: str=None, conference_event_fallback_method: str=None,
        username: str=None, password: str=None,
        fallback_username: str=None, fallback_password: str=None,
        tag: str=None, callback_timeout: str=None,
    ):
        """Initialize a <Conference> verb

        Args:
            name (str): The name of the conference. Can contain up to 100 characters of letters, numbers, and the symbols -, _, and .
            mute (str, optional): A boolean value to indicate whether the member should be on mute in the conference. When muted, a member can hear others speak, but others cannot hear them speak. Defaults to false.
            hold (str, optional): A boolean value to indicate whether the member should be on hold in the conference. When on hold, a member cannot hear others, and they cannot be heard. Defaults to false.
            call_ids_to_coach (str, optional): A comma-separated list of call ids to coach. When a call joins a conference with this attribute set, it will coach the listed calls.
                Those calls will be able to hear and be heard by the coach, but other calls in the conference will not hear the coach.
            conference_event_url (str, optional): URL to send Conference events to. The URL, method, username, and password are set by the BXML document that creates the conference,
                and all events related to that conference will be delivered to that same endpoint. If more calls join afterwards and also have this property (or any other webhook related properties like username and password),
                they will be ignored and the original webhook information will be used. This URL may be a relative endpoint.
            conference_event_method (str, optional): The HTTP method to use for the request to conferenceEventUrl. GET or POST. Default value is POST.
            conference_event_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the conference webhook deliveries in case conferenceEventUrl fails to respond.
            conference_event_fallback_method (str, optional): The HTTP method to use to deliver the conference webhooks to conferenceEventFallbackUrl. GET or POST. Default value is POST.
            username (str, optional):The username to send in the HTTP request to conferenceEventUrl.
            password (str, optional): The password to send in the HTTP request to conferenceEventUrl.
            fallback_username (str, optional): The username to send in the HTTP request to conferenceEventFallbackUrl.
            fallback_password (str, optional): The password to send in the HTTP request to conferenceEventFallbackUrl.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or <Tag> verb, or cleared. May be cleared by setting tag="".
                Max length 256 characters. Defaults to None.
            callback_timeout (str, optional): This is the timeout (in seconds) to use when delivering webhooks for the conference.
                If not set, it will inherit the webhook timeout from the call that creates the conference. Can be any numeric value (including decimals) between 1 and 25.

        Nested Verbs:
            PlayAudio: (optional)
            SpeakSentence: (optional)
            StartRecording: (optional)
            StopRecording: (optional)
            PauseRecording: (optional)
            ResumeRecording: (optional)
        """
        self.name = name
        self.mute = mute
        self.hold = hold
        self.call_ids_to_coach = call_ids_to_coach
        self.conference_event_url = conference_event_url
        self.conference_event_method = conference_event_method
        self.conference_event_fallback_url = conference_event_fallback_url
        self.conference_event_fallback_method = conference_event_fallback_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.callback_timeout = callback_timeout
        super().__init__(
            tag="Conference"
        )

    @property
    def _attributes(self):
        return {
            "name": self.name,
            "mute": self.mute,
            "hold": self.hold,
            "callIdsToCoach": self.call_ids_to_coach,
            "conferenceEventUrl": self.conference_event_url,
            "conferenceEventMethod": self.conference_event_method,
            "conferenceEventFallbackUrl": self.conference_event_fallback_url,
            "conferenceEventFallbackMethod": self.conference_event_fallback_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
            "callbackTimeout": self.callback_timeout,
        }
