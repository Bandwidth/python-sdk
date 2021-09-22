"""
test_api.py

Integration tests for API requests

@copyright Bandwidth INC
"""
import os
import time
import pytest
from datetime import datetime
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.messaging.exceptions.messaging_exception import MessagingException
from bandwidth.exceptions.api_exception import APIException
from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.models.machine_detection_request import MachineDetectionRequest
from bandwidth.voice.models.callback_method_enum import CallbackMethodEnum
from bandwidth.voice.models.mode_enum import ModeEnum
from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.phonenumberlookup.models.order_request import OrderRequest
from bandwidth.configuration import Environment

[pytest]
log_cli = True

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
        response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
        body = response.body
        assert (response.status_code == 202)
        assert len(body.id) == 29    # asserts `messageId` returned and matches expected length (29)
        assert body.owner == body.mfrom == BW_NUMBER    # asserts `owner` matches `mfrom` number and `BW_NUMBER`
        assert body.application_id == BW_MESSAGING_APPLICATION_ID
        assert datetime.fromisoformat(body.time.replace('Z', '+00:00'))    # asserts the date string is valid ISO
        assert type(body.segment_count) is int
        assert body.to == [USER_NUMBER]
        assert body.media == message_body.media
        assert body.text == message_body.text
        assert body.tag == message_body.tag
        assert body.priority == message_body.priority

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
            response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
            body = response.body
            assert response.status_code == 400
            assert type(body.type) == "request-validation"
            assert type(body.description) is str

    def test_successful_media_upload_download(self, messaging_client):
        """Upload a binary string and then download it and confirm both files match.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        media_file_name = 'python_monitoring'
        media_file = b'12345'
        messaging_client.upload_media(BW_ACCOUNT_ID, media_file_name, media_file)
        response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
        downloaded_media = response.body
        assert response.status_code == 200    # assert successful status
        assert downloaded_media == media_file    # assert the binary strings match

    def test_failed_media_download(self, messaging_client):
        """Attempt to download media that doesnt exist and validate a 404 is returned from the API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        with pytest.raises(MessagingException):  # asserts that a messaging exception is raised
            media_file_name = 'invalid_python_monitoring'
            response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
            body = response.body
            assert response.status_code == 404    # assert status code
            assert body.type == "object-not-found"
            assert type(body.description) is str

    def test_successful_create_and_get_call(self, voice_client):
        """Create a successful call and get status of the same call.

        Args:
            voice_client: Contains the basic auth credentials needed to authenticate.

        """
        machine_detection_parameters = MachineDetectionRequest()
        machine_detection_parameters.mode = ModeEnum.ASYNC
        machine_detection_parameters.callback_url = BASE_CALLBACK_URL + "/callbacks/machineDetection"
        machine_detection_parameters.callback_method = CallbackMethodEnum.POST
        machine_detection_parameters.detection_timeout = 5.0
        machine_detection_parameters.silence_timeout = 5.0
        machine_detection_parameters.speech_threshold = 5.0
        machine_detection_parameters.speech_end_threshold = 5.0
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

        # create call
        create_response = voice_client.create_call(BW_ACCOUNT_ID, call_body)
        create_response_body = create_response.body

        # check create call response
        assert create_response.status_code == 201
        assert len(create_response_body.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_response_body.account_id == BW_ACCOUNT_ID
        assert create_response_body.application_id == BW_VOICE_APPLICATION_ID
        assert create_response_body.to == USER_NUMBER
        assert create_response_body.mfrom == BW_NUMBER
        assert create_response_body.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
               BW_ACCOUNT_ID + "/calls/" + create_response_body.call_id
        assert datetime.fromisoformat(str(create_response_body.start_time))    # assert that str(start_time) is datetime
        assert type(create_response_body.call_timeout) is float
        assert type(create_response_body.callback_timeout) is float
        assert create_response_body.answer_method == "POST"
        assert create_response_body.disconnect_method == "GET"

        time.sleep(3)
        # get call
        get_response = voice_client.get_call(BW_ACCOUNT_ID, create_response.body.call_id)
        get_response_body = get_response.body

        print(vars(get_response_body))

        # check get call response
        assert get_response.status_code == 200
        assert get_response_body.call_id == create_response_body.call_id
        assert get_response_body.application_id == BW_VOICE_APPLICATION_ID
        assert get_response_body.account_id == BW_ACCOUNT_ID
        assert datetime.fromisoformat(str(get_response_body.start_time))
        assert datetime.fromisoformat(str(get_response_body.last_update))
        if get_response_body.answer_time:    # may be null dependent on timing
            assert datetime.fromisoformat(str(get_response_body.answer_time))
        if get_response_body.end_time:    # may be null dependent on timing
            assert datetime.fromisoformat(str(get_response_body.end_time))
        if get_response_body.disconnect_cause == "error":
            assert type(get_response_body.error_message) is str
            assert len(get_response_body.error_id) == 36

    def test_failed_create_and_failed_get_call(self, voice_client):
        """Create a successful call and get status of the same call.

        Args:
            voice_client: Contains the basic auth credentials needed to authenticate.

        """
        call_body = CreateCallRequest()
        call_body.mfrom = BW_NUMBER
        call_body.to = "+12345"
        call_body.application_id = BW_VOICE_APPLICATION_ID
        call_body.answer_url = BASE_CALLBACK_URL + '/callbacks/answer'

        # create invalid call
        with pytest.raises(APIException):
            create_response = voice_client.create_call(BW_ACCOUNT_ID, call_body)
            create_response_body = create_response.body

            assert create_response.status_code == 400
            assert type(create_response_body.type) is str
            assert type(create_response_body.description) is str

        # get invalid call
        with pytest.raises(APIException):
            get_response = voice_client.get_call(BW_ACCOUNT_ID, "c-fake-call-id")
            get_response_body = get_response.body

            assert get_response.status_code == 404

    def test_