# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bandwidth.models.conference_redirect_callback import ConferenceRedirectCallback

class TestConferenceRedirectCallback(unittest.TestCase):
    """ConferenceRedirectCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceRedirectCallback:
        """Test ConferenceRedirectCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceRedirectCallback`
        """
        model = ConferenceRedirectCallback()
        if include_optional:
            return ConferenceRedirectCallback(
                event_type = 'bridgeComplete',
                event_time = '2022-06-17T22:19:40.375Z',
                conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9',
                name = 'my-conference-name',
                tag = 'exampleTag'
            )
        else:
            return ConferenceRedirectCallback(
        )
        """

    def testConferenceRedirectCallback(self):
        """Test ConferenceRedirectCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
