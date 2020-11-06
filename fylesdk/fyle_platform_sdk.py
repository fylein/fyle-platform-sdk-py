import json

from . import exceptions
from .apis import v1
from .globals.configs import sdk
from .internals.network import Network


class FylePlatformSDK(Network):
    """The main class which creates a connection with Fyle APIs using OAuth2 authentication (refresh token grant type).

    Parameters:
        client_id (str): Client ID for Fyle API.
        client_secret (str): Client secret for Fyle API.
        refresh_token (str): Refresh token for Fyle API.
    """

    TOKEN_URL = '{}/api/oauth/token'

    def __init__(self, base_url, client_id, client_secret, refresh_token):
        # store the credentials
        self.__base_url = base_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token

        self.v1 = v1
        
        # get the access token
        self.update_access_token()
        self.set_server_url()

    def update_access_token(self):
        """Update the access token."""

        self.__get_access_token()
    

    def set_server_url(self):
        """Set the Base URL in all API objects."""

        sdk.config['SERVER_URL'] = self.__base_url


    def __get_access_token(self):
        """
        Get the access token using a HTTP post.
        
        Returns:
            A new access token.
        """

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }

        token_url = FylePlatformSDK.TOKEN_URL.format(self.__base_url)
        response = self.post_request(url=token_url, data=api_data)

        if response.status_code == 200:
            access_token = json.loads(response.text)['access_token']
            self.access_token = access_token
            sdk.config['ACCESS_TOKEN'] = access_token
            return access_token
        elif response.status_code == 401:
            raise exceptions.InvalidTokenError('Wrong client secret or/and refresh token', response.text)
        elif response.status_code == 404:
            raise exceptions.NotFoundItemError('Client ID doesn\'t exist', response.text)
        elif response.status_code == 500:
            raise exceptions.InternalServerError('Internal server error', response.text)
        else:
            raise exceptions.FylePlatformSDKError('Error: {0}'.format(response.status_code), response.text)
