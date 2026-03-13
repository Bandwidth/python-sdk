"""
Integration test for Bandwidth's WebRTC Endpoints API
"""
import unittest
from datetime import datetime

from hamcrest import assert_that, has_properties, instance_of, equal_to, greater_than

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
from bandwidth.exceptions import ApiException
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

        cls.unauthorized_api_instance = EndpointsApi(ApiClient())

        cls.account_id = BW_ACCOUNT_ID

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

        assert_that(response.status_code, equal_to(201))
        assert_that(response.data, instance_of(CreateEndpointResponse))
        assert_that(response.data.links, instance_of(list))
        assert_that(len(response.data.links), equal_to(0))
        assert_that(response.data.errors, instance_of(list))
        assert_that(response.data.data, instance_of(CreateEndpointResponseData))
        assert_that(response.data.data, has_properties(
            'endpoint_id', instance_of(str),
            'type', EndpointTypeEnum.WEBRTC,
            'status', instance_of(EndpointStatusEnum),
            'token', instance_of(str),
            'creation_timestamp', instance_of(datetime),
            'expiration_timestamp', instance_of(datetime),
            'tag', equal_to("python-sdk-test-endpoint"),
            'devices', instance_of(list)
        ))

        self.__class__.endpoint_id = response.data.data.endpoint_id

    def listEndpoints(self):
        response: ApiResponse = self.endpoints_api_instance.list_endpoints_with_http_info(
            self.account_id,
            type=EndpointTypeEnum.WEBRTC,
            limit=10
        )

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(ListEndpointsResponse))
        assert_that(response.data.links, instance_of(list))
        assert_that(len(response.data.links), equal_to(0))
        assert_that(response.data.errors, instance_of(list))
        assert_that(response.data.data, instance_of(list))
        assert_that(len(response.data.data), greater_than(0))

        listed_ids = [ep.endpoint_id for ep in response.data.data]
        assert_that(self.endpoint_id in listed_ids, equal_to(True))

        endpoint = response.data.data[0]
        assert_that(endpoint, instance_of(Endpoints))
        assert_that(endpoint, has_properties(
            'endpoint_id', instance_of(str),
            'type', instance_of(EndpointTypeEnum),
            'status', instance_of(EndpointStatusEnum),
            'creation_timestamp', instance_of(datetime),
            'expiration_timestamp', instance_of(datetime)
        ))

    def getEndpoint(self):
        response: ApiResponse = self.endpoints_api_instance.get_endpoint_with_http_info(
            self.account_id,
            self.endpoint_id
        )

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(EndpointResponse))
        assert_that(response.data.links, instance_of(list))
        assert_that(len(response.data.links), equal_to(0))
        assert_that(response.data.errors, instance_of(list))
        assert_that(response.data.data, instance_of(Endpoint))
        assert_that(response.data.data, has_properties(
            'endpoint_id', equal_to(self.endpoint_id),
            'type', EndpointTypeEnum.WEBRTC,
            'status', instance_of(EndpointStatusEnum),
            'creation_timestamp', instance_of(datetime),
            'expiration_timestamp', instance_of(datetime),
            'tag', equal_to("python-sdk-test-endpoint"),
            'devices', instance_of(list)
        ))

    # Note: This endpoint is currently not working in the API, so this test is commented out for now. Once the API issue is resolved, this test should be uncommented and verified.
    # def updateEndpointBxml(self):
    #     bxml = '<?xml version="1.0" encoding="UTF-8"?><Bxml><StartStream name="test_stream"/></Bxml>'
    #     response: ApiResponse = self.endpoints_api_instance.update_endpoint_bxml_with_http_info(
    #         self.account_id,
    #         self.endpoint_id,
    #         bxml
    #     )
    #
    #     assert_that(response.status_code, equal_to(204))
    #     ...

    def deleteEndpoint(self):
        response: ApiResponse = self.endpoints_api_instance.delete_endpoint_with_http_info(
            self.account_id,
            self.endpoint_id
        )

        assert_that(response.status_code, equal_to(204))

    def _steps(self):
        call_order = ['createEndpoint', 'listEndpoints', 'getEndpoint', 'deleteEndpoint']
        for name in call_order:
            yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()

    def test_create_endpoint_unauthorized(self):
        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL
        )

        with self.assertRaises(ApiException) as context:
            self.unauthorized_api_instance.create_endpoint(
                self.account_id,
                create_request
            )

        assert_that(context.exception.status, equal_to(401))


if __name__ == '__main__':
    unittest.main()
