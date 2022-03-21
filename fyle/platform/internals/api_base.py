"""
    Define ApiBase class implementing API helper methods.
"""

import json

from .decorators import retry
from .network import Network
from .. import exceptions
from ..globals.config import config


class ApiBase(Network):
    """The base class for all API classes."""

    def __init__(self, version=None, role=None):
        super().__init__()

        self.version = version
        self.role = role

    def _format_api_url(self, endpoint):
        return '{base_url}/{role}{endpoint}'.format(
            base_url=config.get('FYLE', 'SERVER_URL'),
            role=self.role,
            endpoint=endpoint
        )

    @retry(n=3, backoff=5, exceptions=exceptions.InvalidTokenError)
    def make_get_request(self, api_url, query_params=None):
        """Create a HTTP GET request.
        Parameters:
            query_params (dict): HTTP GET parameters for the wanted API.
            api_url (str): Url for the wanted API.
        Returns:
            A response from the request (dict).
        """

        api_headers = {'Authorization': 'Bearer {0}'.format(config.get('AUTH', 'ACCESS_TOKEN'))}
        api_query_params = {}

        for param in query_params:
            # ignore all unused params
            if not query_params[param] is None:
                value = query_params[param]

                # convert boolean to lowercase string
                if isinstance(value, bool):
                    value = str(value).lower()

                api_query_params[param] = value

        response = self.get_request(
            url=self._format_api_url(api_url),
            headers=api_headers,
            params=api_query_params
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

        ApiBase._assert_response(response)

    @retry(n=3, backoff=5, exceptions=exceptions.InvalidTokenError)
    def make_post_request(self, api_url, payload):
        """Create a HTTP post request.

        Parameters:
            payload (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {'Authorization': 'Bearer {0}'.format(config.get('AUTH', 'ACCESS_TOKEN')),
                       'Content-Type': 'application/json'}

        response = self.post_request(
            url=self._format_api_url(api_url),
            headers=api_headers,
            data=payload
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

        ApiBase._assert_response(response)

    @retry(n=3, backoff=5, exceptions=exceptions.InvalidTokenError)
    def make_delete_request(self, api_url):
        """Create a HTTP delete request.

        Parameters:
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request
        """

        api_headers = {'Authorization': 'Bearer {0}'.format(config.get('AUTH', 'ACCESS_TOKEN'))}

        response = self.delete_request(
            url=self._format_api_url(api_url),
            headers=api_headers
        )

        if response.status_code == 204:
            return None

        ApiBase._assert_response(response)

    @staticmethod
    def _assert_response(response):
        if response.status_code == 400:
            raise exceptions.WrongParamsError(
                'Some of the parameters are wrong', json.loads(response.text))
        if response.status_code == 401:
            raise exceptions.InvalidTokenError(
                'Invalid token, try to refresh it', response.text)
        if response.status_code == 403:
            raise exceptions.NoPrivilegeError(
                'Forbidden, the user has insufficient privilege', response.text)
        if response.status_code == 404:
            raise exceptions.NotFoundItemError(
                'Not found item with ID', response.text)
        if response.status_code == 498:
            raise exceptions.ExpiredTokenError(
                'Expired token, try to refresh it', response.text)
        if response.status_code == 500:
            raise exceptions.InternalServerError(
                'Internal server error', response.text)
        raise exceptions.PlatformError(
            'Error: {0}'.format(response.status_code), response.text)
