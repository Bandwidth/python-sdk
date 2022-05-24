"""
test_api.py

Integration tests for API requests

@copyright Bandwidth Inc.
"""
import os
import time
import pytest
import dateutil.parser
import uuid
from random import seed
from random import randint
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.messaging.exceptions.messaging_exception import MessagingException
from bandwidth.exceptions.api_exception import APIException
from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.models.machine_detection_configuration import MachineDetectionConfiguration
from bandwidth.voice.models.callback_method_enum import CallbackMethodEnum
from bandwidth.voice.models.mode_enum import ModeEnum
from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.webrtc.models.session import Session
from bandwidth.webrtc.models.participant import Participant
from bandwidth.phonenumberlookup.models.order_request import OrderRequest

# prints the print statements to console if test fails
[pytest]
log_cli = True

# seed the random number generator
seed(randint(10, 500))

try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    BW_MESSAGING_APPLICATION_ID = os.environ["BW_MESSAGING_APPLICATION_ID"]
    BASE_CALLBACK_URL = os.environ["BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
except KeyError as e:
    raise Exception("Environmental variables not found")


@pytest.fixture()
def messaging_client():
    bandwidth_client = BandwidthClient(
        messaging_basic_auth_user_name=BW_USERNAME,
        messaging_basic_auth_password=BW_PASSWORD,
    )
    messaging_client = bandwidth_client.messaging_client.client
    return messaging_client


@pytest.fixture()
def voice_client():
    bandwidth_client = BandwidthClient(
        voice_basic_auth_user_name=BW_USERNAME,
        voice_basic_auth_password=BW_PASSWORD,
    )
    voice_client = bandwidth_client.voice_client.client
    return voice_client


@pytest.fixture()
def mfa_client():
    bandwidth_client = BandwidthClient(
        multi_factor_auth_basic_auth_user_name=BW_USERNAME,
        multi_factor_auth_basic_auth_password=BW_PASSWORD,
    )
    mfa_client = bandwidth_client.multi_factor_auth_client.mfa
    return mfa_client


@pytest.fixture()
def web_rtc_client():
    bandwidth_client = BandwidthClient(
        web_rtc_basic_auth_user_name=BW_USERNAME,
        web_rtc_basic_auth_password=BW_PASSWORD,
    )
    web_rtc_client = bandwidth_client.web_rtc_client.client
    return web_rtc_client


@pytest.fixture()
def tn_lookup_client():
    bandwidth_client = BandwidthClient(
        phone_number_lookup_basic_auth_user_name=BW_USERNAME,
        phone_number_lookup_basic_auth_password=BW_PASSWORD,
    )
    tn_lookup_client = bandwidth_client.phone_number_lookup_client.client
    return tn_lookup_client


class TestApi:
    """
    Class that holds basic monitoring tests for the Python SDK. Makes requests to cover JSON call and response,
    error handling, and binary string uploads and downloads
    """
    def test_successful_create_message(self, messaging_client):
        """Create valid request to send an SMS using the Messaging API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        message_body = MessageRequest()
        message_body.application_id = BW_MESSAGING_APPLICATION_ID
        message_body.to = [USER_NUMBER]
        message_body.mfrom = BW_NUMBER
        message_body.text = "Python Monitoring"
        create_response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
        create_response_body = create_response.body

        print(vars(create_response))

        assert (create_response.status_code == 202)
        assert len(create_response_body.id) == 29    # asserts `messageId` returned and matches expected length (29)
        # asserts `owner` matches `mfrom` number and `BW_NUMBER`
        assert create_response_body.owner == create_response_body.mfrom == BW_NUMBER
        assert create_response_body.application_id == BW_MESSAGING_APPLICATION_ID

        # asserts the date string is valid ISO
        assert dateutil.parser.isoparse(str(create_response_body.time))
        assert type(create_response_body.segment_count) is int
        assert create_response_body.to == [USER_NUMBER]
        assert create_response_body.media == message_body.media
        assert create_response_body.text == message_body.text
        assert create_response_body.tag == message_body.tag
        assert create_response_body.priority == message_body.priority

    def test_failed_create_message(self, messaging_client):
        """Create invalid request to send an SMS using the Messaging API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        with pytest.raises(MessagingException):    # asserts that a messaging exception is raised
            message_body = MessageRequest()
            message_body.application_id = BW_MESSAGING_APPLICATION_ID
            message_body.to = ["+1invalid"]
            message_body.mfrom = BW_NUMBER
            message_body.text = "Python Monitoring"

            create_response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
            create_response_body = create_response.body

            print(vars(create_response))

            assert create_response.status_code == 400
            assert type(create_response_body.type) == "request-validation"
            assert type(create_response_body.description) is str

    def test_successful_media_upload_download(self, messaging_client):
        """Upload a binary string and then download it and confirm both files match.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        media_file_name = f'text-media-id-{uuid.uuid4()}'
        media_file = b'12345'
        messaging_client.upload_media(BW_ACCOUNT_ID, media_file_name, media_file)
        upload_response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
        downloaded_media = upload_response.body

        print(vars(upload_response))

        assert upload_response.status_code == 200    # assert successful status
        assert downloaded_media == media_file    # assert the binary strings match

    def test_failed_media_download(self, messaging_client):
        """Attempt to download media that doesnt exist and validate a 404 is returned from the API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        with pytest.raises(MessagingException):  # asserts that a messaging exception is raised
            media_file_name = 'invalid_python_monitoring'
            get_response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
            get_response_body = get_response.body

            print(vars(get_response))

            assert get_response.status_code == 404    # assert status code
            assert get_response_body.type == "object-not-found"
            assert type(get_response_body.description) is str

    def test_successful_create_and_get_call(self, voice_client):
        """Create a successful call and get status of the same call.

        Args:
            voice_client: Contains the basic auth credentials needed to authenticate.

        """
        machine_detection_parameters = MachineDetectionConfiguration()
        machine_detection_parameters.mode = ModeEnum.ASYNC
        machine_detection_parameters.callback_url = BASE_CALLBACK_URL + "/callbacks/machineDetection"
        machine_detection_parameters.callback_method = CallbackMethodEnum.POST
        machine_detection_parameters.detection_timeout = 5.0
        machine_detection_parameters.silence_timeout = 5.0
        machine_detection_parameters.speech_threshold = 5.0
        machine_detection_parameters.speech_end_threshold = 5.0
        machine_detection_parameters.machine_speech_end_threshold = 3.2
        machine_detection_parameters.delay_result = True

        call_body = CreateCallRequest()
        call_body.mfrom = BW_NUMBER
        call_body.to = USER_NUMBER
        call_body.application_id = BW_VOICE_APPLICATION_ID
        call_body.answer_url = BASE_CALLBACK_URL + '/callbacks/answer'
        call_body.answer_method = CallbackMethodEnum.POST
        call_body.disconnect_url = BASE_CALLBACK_URL + '/callbacks/disconnect'
        call_body.disconnect_method = CallbackMethodEnum.GET
        call_body.machine_detection = machine_detection_parameters

        create_response = voice_client.create_call(BW_ACCOUNT_ID, call_body)
        create_response_body = create_response.body
        time.sleep(3)
        get_response = voice_client.get_call(BW_ACCOUNT_ID, create_response.body.call_id)
        get_response_body = get_response.body

        print(vars(create_response))
        print(vars(get_response))

        assert create_response.status_code == 201
        assert len(create_response_body.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_response_body.account_id == BW_ACCOUNT_ID
        assert create_response_body.application_id == BW_VOICE_APPLICATION_ID
        assert create_response_body.to == USER_NUMBER
        assert create_response_body.mfrom == BW_NUMBER
        assert create_response_body.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
               BW_ACCOUNT_ID + "/calls/" + create_response_body.call_id
        assert dateutil.parser.isoparse(str(create_response_body.enqueued_time))    # assert that str(enqueued_time) is datetime
        assert type(create_response_body.call_timeout) is float
        assert type(create_response_body.callback_timeout) is float
        assert create_response_body.answer_method == "POST"
        assert create_response_body.disconnect_method == "GET"
        assert get_response.status_code == 200
        assert get_response_body.call_id == create_response_body.call_id
        assert get_response_body.application_id == BW_VOICE_APPLICATION_ID
        assert get_response_body.account_id == BW_ACCOUNT_ID
        if get_response_body.start_time: 
            assert dateutil.parser.isoparse(str(get_response_body.start_time))
        assert dateutil.parser.isoparse(str(get_response_body.enqueued_time))
        assert dateutil.parser.isoparse(str(get_response_body.last_update))
        if get_response_body.answer_time:    # may be null dependent on timing
            assert dateutil.parser.isoparse(str(get_response_body.answer_time))
        if get_response_body.end_time:    # may be null dependent on timing
            assert dateutil.parser.isoparse(str(get_response_body.end_time))
        if get_response_body.disconnect_cause == "error":
            assert type(get_response_body.error_message) is str
            assert len(get_response_body.error_id) == 36

    def test_failed_create_and_failed_get_call(self, voice_client):
        """Create a failed call and get status of a call that doesnt exist.

        Args:
            voice_client: Contains the basic auth credentials needed to authenticate.

        """
        call_body = CreateCallRequest()
        call_body.mfrom = BW_NUMBER
        call_body.to = "+12345"
        call_body.application_id = BW_VOICE_APPLICATION_ID
        call_body.answer_url = BASE_CALLBACK_URL + '/callbacks/answer'

        with pytest.raises(APIException):
            create_response = voice_client.create_call(BW_ACCOUNT_ID, call_body)
            create_response_body = create_response.body

            get_response = voice_client.get_call(BW_ACCOUNT_ID, "c-fake-call-id")
            get_response_body = get_response.body

            print(vars(create_response))
            print(vars(get_response))

            assert create_response.status_code == 400
            assert type(create_response_body.type) is str
            assert type(create_response_body.description) is str
            assert get_response.status_code == 404
            assert type(get_response_body.type) is str
            assert type(get_response_body.description) is str
            if get_response_body.id:
                assert type(get_response_body.id) is str


    def test_createCall_with_priority(self, voice_client):
        """Create a successful voice api call with priority set

        Args: 
            voice_client: Contains the basic auth credentials needed to authenticate.

        """
        call_body = CreateCallRequest()
        call_body.mfrom = BW_NUMBER
        call_body.to = USER_NUMBER
        call_body.application_id = BW_VOICE_APPLICATION_ID
        call_body.answer_url = BASE_CALLBACK_URL + '/callbacks/answer'
        call_body.answer_method = CallbackMethodEnum.POST
        call_body.disconnect_url = BASE_CALLBACK_URL + '/callbacks/disconnect'
        call_body.disconnect_method = CallbackMethodEnum.GET
        call_body.priority = 1

        create_response = voice_client.create_call(BW_ACCOUNT_ID, call_body)
        create_response_body = create_response.body

        print(vars(create_response))

        assert create_response.status_code == 201
        assert len(create_response_body.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_response_body.account_id == BW_ACCOUNT_ID
        assert create_response_body.application_id == BW_VOICE_APPLICATION_ID
        assert create_response_body.to == USER_NUMBER
        assert create_response_body.mfrom == BW_NUMBER
        assert create_response_body.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
               BW_ACCOUNT_ID + "/calls/" + create_response_body.call_id
        assert dateutil.parser.isoparse(str(create_response_body.enqueued_time))    # assert that str(enqueued_time) is datetime
        assert type(create_response_body.call_timeout) is float
        assert type(create_response_body.callback_timeout) is float
        assert create_response_body.answer_method == "POST"
        assert create_response_body.disconnect_method == "GET"
        assert create_response_body.priority == 1


    def test_successful_mfa_messaging(self, mfa_client):
        """Create a successful messaging MFA request.

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        body = TwoFactorCodeRequestSchema(
            mfrom=BW_NUMBER,
            to=USER_NUMBER,
            application_id=BW_MESSAGING_APPLICATION_ID,
            scope="scope",
            digits=6,
            message="Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        create_response = mfa_client.create_messaging_two_factor(BW_ACCOUNT_ID, body)
        create_response_body = create_response.body

        print(vars(create_response))

        assert create_response.status_code == 200
        assert len(create_response_body.message_id) == 29

    @pytest.mark.skip(reason="API accepts invalid numbers for to/from field")
    def test_failed_mfa_messaging(self, mfa_client):
        """Create a failed messaging MFA request.

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        body = TwoFactorCodeRequestSchema(
            mfrom=BW_NUMBER,
            to="+12345",
            application_id=BW_MESSAGING_APPLICATION_ID,
            scope="scope",
            digits=6,
            message="Your temporary {NAME} {SCOPE} code is {CODE}"
        )

        with pytest.raises(APIException):
            create_response = mfa_client.create_messaging_two_factor(BW_ACCOUNT_ID, body)
            create_response_body = create_response.body

            print(vars(create_response))

            assert create_response.status_code == 400
            assert type(create_response_body.error) is str
            assert type(create_response_body.request_id) is str

    def test_successful_mfa_voice(self, mfa_client):
        """Create a successful voice MFA request.

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        body = TwoFactorCodeRequestSchema(
            mfrom=BW_NUMBER,
            to=USER_NUMBER,
            application_id=BW_VOICE_APPLICATION_ID,
            scope="scope",
            digits=6,
            message="Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        create_response = mfa_client.create_voice_two_factor(BW_ACCOUNT_ID, body)
        create_response_body = create_response.body

        print(vars(create_response))

        assert create_response.status_code == 200
        assert len(create_response_body.call_id) == 47

    def test_failed_mfa_voice(self, mfa_client):
        """Create a failed voice MFA request.

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        body = TwoFactorCodeRequestSchema(
            mfrom=BW_NUMBER,
            to="+12345",
            application_id=BW_MESSAGING_APPLICATION_ID,
            scope="scope",
            digits=6,
            message="Your temporary {NAME} {SCOPE} code is {CODE}"
        )

        with pytest.raises(APIException):
            create_response = mfa_client.create_voice_two_factor(BW_ACCOUNT_ID, body)
            create_response_body = create_response.body

            print(vars(create_response))

            assert create_response.status_code == 400
            assert type(create_response_body.error) is str
            assert type(create_response_body.request_id) is str

    @pytest.mark.skip(reason="No way to currently test a successful code unless we ingest callbacks")
    def test_successful_mfa_verify(self, mfa_client):
        """

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        # TODO: Set the to number to a randomly generated number to avoid rate limiting
        body = TwoFactorVerifyRequestSchema(
            to="+1" + str(randint(1111111111, 9999999999)),
            application_id=BW_VOICE_APPLICATION_ID,
            scope="scope",
            code="123456",
            expiration_time_in_minutes=3
        )
        verify_response = mfa_client.create_verify_two_factor(BW_ACCOUNT_ID, body)
        verify_response_body = verify_response.body

        print(vars(verify_response))

        assert verify_response.status_code == 200
        assert (isinstance(verify_response_body.valid, bool))
        assert verify_response_body.valid is True

    def test_failed_mfa_verify(self, mfa_client):
        """Test an invalid MFA code.

        Args:
            mfa_client: Contains the basic auth credentials needed to authenticate.

        """
        # TODO: Set the to number to a randomly generated number to avoid rate limiting
        body = TwoFactorVerifyRequestSchema(
            to="+1" + str(randint(1111111111, 9999999999)),
            application_id=BW_VOICE_APPLICATION_ID,
            scope="scope",
            code="123456",
            expiration_time_in_minutes=3
        )

        print(body.to)

        verify_response = mfa_client.create_verify_two_factor(BW_ACCOUNT_ID, body)
        verify_response_body = verify_response.body

        print(vars(verify_response))

        assert verify_response.status_code == 200
        assert isinstance(verify_response_body.valid, bool)
        assert verify_response_body.valid is False

    def test_successful_web_rtc_create_get_and_delete_session(self, web_rtc_client):
        """Successfully create, get, and delete a WebRTC session.

        Args:
            web_rtc_client: Contains the basic auth credentials needed to authenticate.

        """
        body = Session(
            tag="DevX Integration Testing"
        )
        create_response = web_rtc_client.create_session(BW_ACCOUNT_ID, body)
        create_response_body = create_response.body

        get_response = web_rtc_client.get_session(BW_ACCOUNT_ID, create_response_body.id)
        get_response_body = get_response.body

        delete_response = web_rtc_client.delete_session(BW_ACCOUNT_ID, create_response_body.id)

        print(vars(create_response))
        print(vars(get_response))
        print(vars(delete_response))

        assert create_response.status_code == 200
        assert type(create_response_body.id) is str
        assert type(create_response_body.tag) is str and create_response_body.tag == "DevX Integration Testing"

        assert get_response.status_code == 200
        assert get_response_body.id == create_response_body.id
        assert type(get_response_body.tag) is str and create_response_body.tag == "DevX Integration Testing"

        assert delete_response.status_code == 204

    @pytest.mark.skip(reason="No way to force a 400 here as the sdk normalizes any tag value to a string and the body \
    is optional")
    def test_failed_web_rtc_create_get_and_delete_session(self, web_rtc_client):
        """

        Args:
            web_rtc_client: Contains the basic auth credentials needed to authenticate.

        """
        body = Session(
            tag="DevX Integration Testing",
        )

        with pytest.raises(APIException):
            create_response = web_rtc_client.create_session(BW_ACCOUNT_ID, body)
            create_response_body = create_response.body

            get_response = web_rtc_client.get_session(BW_ACCOUNT_ID, "Some-ID-That-Doesnt-Exist")
            get_response_body = get_response.body

            delete_response = web_rtc_client.delete_session(BW_ACCOUNT_ID, "Some-ID-That-Doesnt-Exist")

            print(vars(create_response))
            print(vars(get_response))
            print(vars(delete_response))

            assert create_response.status_code == 200
            assert type(create_response_body.id) is str
            assert type(create_response_body.tag) is str and create_response_body.tag == "DevX Integration Testing"

            assert get_response.status_code == 404
            assert type(get_response_body.code) is int
            assert type(get_response_body.message) is str

            assert delete_response.status_code == 404

    def test_successful_web_rtc_create_get_and_delete_participant(self, web_rtc_client):
        """Successfully create, get, and delete a WebRTC participant.

        Args:
            web_rtc_client: Contains the basic auth credentials needed to authenticate.

        """
        body = Participant()
        body.publish_permissions = ["AUDIO", "VIDEO"]
        body.device_api_version = "V3"

        create_response = web_rtc_client.create_participant(BW_ACCOUNT_ID, body)
        create_response_body = create_response.body

        get_response = web_rtc_client.get_participant(BW_ACCOUNT_ID, create_response_body.participant.id)
        get_response_body = get_response.body

        delete_response = web_rtc_client.delete_participant(BW_ACCOUNT_ID, create_response_body.participant.id)

        print(vars(create_response))
        print(vars(get_response))
        print(vars(delete_response))

        assert create_response.status_code == 200
        assert type(create_response_body.participant.id) is str
        assert len(create_response_body.participant.id) is 36
        assert set(create_response_body.participant.publish_permissions) == set(body.publish_permissions)
        assert create_response_body.participant.device_api_version == body.device_api_version

        assert get_response.status_code == 200
        assert type(get_response_body.id) is str
        assert len(get_response_body.id) is 36
        assert set(get_response_body.publish_permissions) == set(body.publish_permissions)
        assert get_response_body.device_api_version == body.device_api_version

        assert delete_response.status_code == 204

    def test_failed_web_rtc_create_get_and_delete_participant(self, web_rtc_client):
        """

        Args:
            web_rtc_client: Contains the basic auth credentials needed to authenticate.

        """
        body = Participant()
        body.publish_permissions = ["AUDIO", "VIDEO", "SOME OTHER INVALID PERMISSION"]
        body.device_api_version = "V3"

        with pytest.raises(APIException):
            create_response = web_rtc_client.create_participant(BW_ACCOUNT_ID, body)
            create_response_body = create_response.body

            get_response = web_rtc_client.get_participant(BW_ACCOUNT_ID, "Some-ID-That-Doesnt-Exist")
            get_response_body = get_response.body

            delete_response = web_rtc_client.delete_participant(BW_ACCOUNT_ID, "Some-ID-That-Doesnt-Exist")

            print(vars(create_response))
            print(vars(get_response))
            print(vars(delete_response))

            assert create_response.status_code == 400
            assert type(create_response_body.code) is int
            assert type(create_response_body.message) is str

            assert get_response.status_code == 404
            assert type(get_response_body.code) is int
            assert type(get_response_body.message) is str

            assert delete_response.status_code == 404

    def test_successful_create_and_get_tn_lookup(self, tn_lookup_client):
        """

        Args:
            tn_lookup_client: Contains the basic auth credentials needed to authenticate.

        """
        body = OrderRequest()
        body.tns = [BW_NUMBER]
        create_response = tn_lookup_client.create_lookup_request(BW_ACCOUNT_ID, body)
        create_response_body = create_response.body

        get_response = tn_lookup_client.get_lookup_request_status(BW_ACCOUNT_ID, create_response_body.request_id)
        get_response_body = get_response.body

        print(vars(create_response))
        print(vars(get_response))

        assert create_response.status_code == 202
        assert len(create_response_body.request_id) is 36
        assert type(create_response_body.request_id) is str
        assert type(create_response_body.status) is str

        assert get_response.status_code == 200
        assert get_response_body.request_id == create_response_body.request_id
        assert type(get_response_body.status) is str
        if get_response_body.result:
            result = get_response_body.result[0]
            assert type(result.response_code) is int

    def test_failed_create_and_get_tn_lookup(self, tn_lookup_client):
        """

        Args:
            tn_lookup_client: Contains the basic auth credentials needed to authenticate.

        """
        body = OrderRequest()
        body.tns = ["+12345"]

        with pytest.raises(APIException):
            create_response = tn_lookup_client.create_lookup_request(BW_ACCOUNT_ID, body)

            get_response = tn_lookup_client.get_lookup_request_status(BW_ACCOUNT_ID, "Some-ID-That-Doesnt-Exist")

            print(vars(create_response))
            print(vars(get_response))

            assert create_response.status_code == 400
            assert get_response.status_code == 404
