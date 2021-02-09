"""
    Defines Auth Class.
"""

import json

from .network import Network
from .. import exceptions
from ..globals.config import config


class Auth(Network):
    """Auth Class"""

    def __init__(self):
        self.__access_token = None
        super(Auth, self).__init__()

    @staticmethod
    def __get_access_token():
        """
        Get the access token using a HTTP post.

        Returns:
            A new access token.
        """

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': config.get('AUTH', 'REFRESH_TOKEN'),
            'client_id': config.get('AUTH', 'CLIENT_ID'),
            'client_secret': config.get('AUTH', 'CLIENT_SECRET')
        }

        token_url = config.get('FYLE', 'TOKEN_URL')
        response = Network().post_request(url=token_url, data=api_data)

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
            raise exceptions.PlatformError(
                'Error: {0}'.format(response.status_code), response.text)

        return access_token

    def update_access_token(self):
        """Update the access token."""

        self.__access_token = self.__get_access_token()
        config.set('AUTH', 'ACCESS_TOKEN', self.__access_token)
