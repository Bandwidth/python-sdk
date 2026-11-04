"""
Unit tests for Configuration authentication settings
"""
import unittest
from unittest.mock import patch

from hamcrest import assert_that, calling, raises, equal_to, has_entries

from bandwidth import Configuration


class TestConfiguration(unittest.TestCase):
    """Configuration unit tests"""

    def test_basic_auth_params_rejected(self) -> None:
        assert_that(
            calling(Configuration).with_args(username='username', password='password'),
            raises(TypeError)
        )

    def test_auth_settings_without_credentials(self) -> None:
        configuration = Configuration()

        assert_that(configuration.auth_settings(), equal_to({}))

    def test_auth_settings_with_access_token(self) -> None:
        configuration = Configuration(access_token='abcd1234')
        auth_settings = configuration.auth_settings()

        assert_that(list(auth_settings.keys()), equal_to(['OAuth2']))
        assert_that(auth_settings['OAuth2'], has_entries(
            'type', 'oauth2',
            'in', 'header',
            'key', 'Authorization',
            'value', 'Bearer abcd1234'
        ))

    def test_auth_settings_with_client_credentials(self) -> None:
        configuration = Configuration(client_id='client_id', client_secret='client_secret')

        with patch.object(Configuration, 'get_access_token', return_value='abcd1234') as mock_get_access_token:
            auth_settings = configuration.auth_settings()

        mock_get_access_token.assert_called_once()
        assert_that(list(auth_settings.keys()), equal_to(['OAuth2']))
        assert_that(auth_settings['OAuth2'], has_entries(
            'type', 'oauth2',
            'in', 'header',
            'key', 'Authorization',
            'value', 'Bearer abcd1234'
        ))


if __name__ == '__main__':
    unittest.main()
