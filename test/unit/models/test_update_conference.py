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

from bandwidth.models.update_conference import UpdateConference

class TestUpdateConference(unittest.TestCase):
    """UpdateConference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateConference:
        """Test UpdateConference
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return UpdateConference(
                status = 'active',
                redirect_url = 'https://myServer.example/bandwidth/webhooks/conferenceRedirect',
                redirect_method = 'POST',
                username = 'mySecretUsername',
                password = 'mySecretPassword1!',
                redirect_fallback_url = 'https://myFallbackServer.example/bandwidth/webhooks/conferenceRedirect',
                redirect_fallback_method = 'POST',
                fallback_username = 'mySecretUsername',
                fallback_password = 'mySecretPassword1!'
            )
        else:
            return UpdateConference(
        )

    def testUpdateConference(self):
        """Test UpdateConference"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, UpdateConference)
        assert instance.status == 'active'
        assert instance.redirect_url == 'https://myServer.example/bandwidth/webhooks/conferenceRedirect'
        assert instance.redirect_method == 'POST'
        assert instance.username == 'mySecretUsername'
        assert instance.password == 'mySecretPassword1!'
        assert instance.redirect_fallback_url == 'https://myFallbackServer.example/bandwidth/webhooks/conferenceRedirect'
        assert instance.redirect_fallback_method == 'POST'
        assert instance.fallback_username == 'mySecretUsername'
        assert instance.fallback_password == 'mySecretPassword1!'

if __name__ == '__main__':
    unittest.main()
