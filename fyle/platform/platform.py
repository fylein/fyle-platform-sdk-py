"""
    Fyle Platform SDK Class
"""

from .apis import v1beta
from .globals.config import config
from .internals.auth import Auth


class Platform(Auth):
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

        self.v1beta = v1beta

        # get the access token
        self.set_server_url()
        self.set_token_url()
        self.set_client_id()
        self.set_client_secret()
        self.set_refresh_token()
        self.update_access_token()

    def set_server_url(self):
        """Set the Server URL in all API objects."""

        config.set('FYLE', 'SERVER_URL', self.__server_url)

    def set_token_url(self):
        """Set the Token URL in all API objects."""

        config.set('FYLE', 'TOKEN_URL', self.__token_url)

    def set_client_id(self):
        """Set the Client ID."""

        config.set('AUTH', 'CLIENT_ID', self.__client_id)

    def set_client_secret(self):
        """Set the Client Secret."""

        config.set('AUTH', 'CLIENT_SECRET', self.__client_secret)

    def set_refresh_token(self):
        """Set the Refresh token."""

        config.set('AUTH', 'REFRESH_TOKEN', self.__refresh_token)
