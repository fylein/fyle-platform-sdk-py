"""
    Fyle Platform SDK Class
"""

import json

from . import exceptions
from .apis import v1
from .globals.config import config
from .internals.network import Network


class FylePlatformSDK(Network):
    """The main class which creates a connection with
    Fyle APIs using OAuth2 authentication (refresh token grant type).

    Parameters:
        client_id (str): Client ID for Fyle API.
        client_secret (str): Client secret for Fyle API.
        refresh_token (str): Refresh token for Fyle API.
    """

    def __init__(self, server_url, token_url, client_id, client_secret, refresh_token):
        super().__init__()

        # store the credentials
        self.__server_url = server_url
        self.__token_url = token_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token
        self.__access_token = None

        self.v1 = v1

        # get the access token
        self.set_server_url()
        self.set_token_url()
        self.set_refresh_token()
        self.update_access_token()

    def update_access_token(self):
        """Update the access token."""
        self.__get_access_token()
        self.__access_token = self.__get_access_token()
        config.set('AUTH', 'ACCESS_TOKEN', self.__access_token)

    def set_server_url(self):
        """Set the Server URL in all API objects."""

        config.set('FYLE', 'SERVER_URL', self.__server_url)

    def set_token_url(self):
        """Set the Token URL in all API objects."""

        config.set('FYLE', 'TOKEN_URL', self.__token_url)

    def set_refresh_token(self):
        """Set the Refresh token."""

        config.set('AUTH', 'REFRESH_TOKEN', self.__refresh_token)

    def __get_access_token(self):
        """
        Get the access token using a HTTP post.

        Returns:
            A new access token.
        """

        access_token = None

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': config.get('AUTH', 'REFRESH_TOKEN'),
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }

        token_url = config.get('FYLE', 'TOKEN_URL')
        response = self.post_request(url=token_url, data=api_data)

        if response.status_code == 200:
            access_token = json.loads(response.text)['access_token']
        elif response.status_code == 401:
            raise exceptions.InvalidTokenError(
                'Wrong client secret or/and refresh token', response.text)
        elif response.status_code == 404:
            raise exceptions.NotFoundItemError('Client ID doesn\'t exist', response.text)
        elif response.status_code == 500:
            raise exceptions.InternalServerError('Internal server error', response.text)
        else:
            raise exceptions.FylePlatformSDKError(
                'Error: {0}'.format(response.status_code), response.text)

        return access_token
