"""
Integration test for Bandwidth's WebRTC Endpoints API
"""
import unittest
from datetime import datetime

from bandwidth import ApiClient, ApiResponse, Configuration
from bandwidth.api.endpoints_api import EndpointsApi
from bandwidth.models.create_web_rtc_connection_request import CreateWebRtcConnectionRequest
from bandwidth.models.create_endpoint_response import CreateEndpointResponse
from bandwidth.models.create_endpoint_response_data import CreateEndpointResponseData
from bandwidth.models.endpoint import Endpoint
from bandwidth.models.endpoint_response import EndpointResponse
from bandwidth.models.list_endpoints_response import ListEndpointsResponse
from bandwidth.models.endpoints import Endpoints
from bandwidth.models.endpoint_type_enum import EndpointTypeEnum
from bandwidth.models.endpoint_direction_enum import EndpointDirectionEnum
from bandwidth.models.endpoint_status_enum import EndpointStatusEnum
from bandwidth.exceptions import UnauthorizedException, NotFoundException
from test.utils.env_variables import *


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi integration test"""

    @classmethod
    def setUpClass(cls) -> None:
        configuration = Configuration(
            client_id=BW_CLIENT_ID,
            client_secret=BW_CLIENT_SECRET
        )
        api_client = ApiClient(configuration)
        cls.endpoints_api_instance = EndpointsApi(api_client)

        unauthorized_configuration = Configuration(
            username='bad_username',
            password='bad_password'
        )
        cls.unauthorized_api_instance = EndpointsApi(ApiClient(unauthorized_configuration))

        cls.account_id = BW_ACCOUNT_ID
        cls.test_endpoint_id = 'endpoint-id'

    def createEndpoint(self):
        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL,
            event_callback_url=BASE_CALLBACK_URL + "/endpoint/callback",
            event_fallback_url=BASE_CALLBACK_URL + "/endpoint/fallback",
            tag="python-sdk-test-endpoint"
        )

        response: ApiResponse = self.endpoints_api_instance.create_endpoint_with_http_info(
            self.account_id,
            create_request
        )

        assert response.status_code == 201
        assert isinstance(response.data, CreateEndpointResponse)
        assert isinstance(response.data.links, list)
        assert len(response.data.links) == 0
        assert isinstance(response.data.errors, list)
        assert len(response.data.errors) == 0
        assert isinstance(response.data.data, CreateEndpointResponseData)
        assert isinstance(response.data.data.endpoint_id, str)
        assert response.data.data.type == EndpointTypeEnum.WEBRTC
        assert isinstance(response.data.data.status, EndpointStatusEnum)
        assert isinstance(response.data.data.token, str)
        assert isinstance(response.data.data.creation_timestamp, datetime)
        assert isinstance(response.data.data.expiration_timestamp, datetime)
        assert response.data.data.tag == "python-sdk-test-endpoint"
        assert isinstance(response.data.data.devices, list)

        self.__class__.endpoint_id = response.data.data.endpoint_id

    def listEndpoints(self):
        response: ApiResponse = self.endpoints_api_instance.list_endpoints_with_http_info(
            self.account_id,
            type=EndpointTypeEnum.WEBRTC,
            limit=10
        )

        assert response.status_code == 200
        assert isinstance(response.data, ListEndpointsResponse)
        assert isinstance(response.data.links, list)
        assert len(response.data.links) == 0
        assert isinstance(response.data.errors, list)
        assert len(response.data.errors) == 0
        assert isinstance(response.data.data, list)
        assert len(response.data.data) > 0

        endpoint = response.data.data[0]
        assert isinstance(endpoint, Endpoints)
        assert isinstance(endpoint.endpoint_id, str)
        assert isinstance(endpoint.type, EndpointTypeEnum)
        assert isinstance(endpoint.status, EndpointStatusEnum)
        assert isinstance(endpoint.creation_timestamp, datetime)
        assert isinstance(endpoint.expiration_timestamp, datetime)

        tagged_endpoint = next((ep for ep in response.data.data if ep.endpoint_id == self.endpoint_id), None)
        assert tagged_endpoint is not None
        assert tagged_endpoint.tag == "python-sdk-test-endpoint"

    def getEndpoint(self):
        response: ApiResponse = self.endpoints_api_instance.get_endpoint_with_http_info(
            self.account_id,
            self.endpoint_id
        )

        assert response.status_code == 200
        assert isinstance(response.data, EndpointResponse)
        assert isinstance(response.data.links, list)
        assert len(response.data.links) == 0
        assert isinstance(response.data.errors, list)
        assert len(response.data.errors) == 0
        assert isinstance(response.data.data, Endpoint)
        assert response.data.data.endpoint_id == self.endpoint_id
        assert response.data.data.type == EndpointTypeEnum.WEBRTC
        assert isinstance(response.data.data.status, EndpointStatusEnum)
        assert isinstance(response.data.data.creation_timestamp, datetime)
        assert isinstance(response.data.data.expiration_timestamp, datetime)
        assert response.data.data.tag == "python-sdk-test-endpoint"
        assert isinstance(response.data.data.devices, list)

    def deleteEndpoint(self):
        response: ApiResponse = self.endpoints_api_instance.delete_endpoint_with_http_info(
            self.account_id,
            self.endpoint_id
        )

        assert response.status_code == 204

    def _steps(self):
        call_order = ['createEndpoint', 'listEndpoints', 'getEndpoint', 'deleteEndpoint']
        for name in call_order:
            yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()

    def assertApiException(self, context, expected_status_code: int):
        assert context.exception.status == expected_status_code

    def test_create_endpoint_unauthorized(self):
        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL
        )

        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.create_endpoint(
                self.account_id,
                create_request
            )

        self.assertApiException(context, 401)

    def test_list_endpoints_unauthorized(self):
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_endpoints(self.account_id)

        self.assertApiException(context, 401)

    def test_get_endpoint_unauthorized(self):
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_endpoint(self.account_id, self.test_endpoint_id)

        self.assertApiException(context, 401)

    def test_get_endpoint_not_found(self):
        with self.assertRaises(NotFoundException) as context:
            self.endpoints_api_instance.get_endpoint(self.account_id, self.test_endpoint_id)

        self.assertApiException(context, 404)

    def test_delete_endpoint_unauthorized(self):
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.delete_endpoint(self.account_id, self.test_endpoint_id)

        self.assertApiException(context, 401)

    def test_delete_endpoint_not_found(self):
        with self.assertRaises(NotFoundException) as context:
            self.endpoints_api_instance.delete_endpoint(self.account_id, self.test_endpoint_id)

        self.assertApiException(context, 404)


if __name__ == '__main__':
    unittest.main()
