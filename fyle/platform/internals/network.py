"""
    Defining Network related operations
"""
# pylint: disable=no-member

import os

import requests

from . import serializers


class Network:
    """Class for making GET, POST requests"""
    HOSTNAME = None
    HEADERS = serializers.deserialize({
        'AUTHORIZATION': 'Authorization',
        'CONTENT_TYPE': 'Content-Type',
        'USER_AGENT': 'User-Agent'
    })

    def __init__(self):
        self.__root_dir = os.path.split(os.getcwd())[1]
        Network.HOSTNAME = os.environ.get('HOSTNAME', self.__root_dir)

    def get_request(self, url, **kwargs):
        """Create a HTTP GET request.

        Parameters:
            url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        kwargs.setdefault('allow_redirects', True)
        return self._http_request('GET', url, **kwargs)

    def post_request(self, url, data=None, headers=None, **kwargs):
        """Create a HTTP post request.

        Parameters:
            url (str): Url for the wanted API.
            data:
            headers:
        Returns:
            A response from the request (dict).
        """

        data, headers = Network._process_data_and_headers(data, headers)
        return self._http_request('POST', url, headers=headers, data=data, **kwargs)

    def delete_request(self, url, **kwargs):
        """Create a HTTP delete request.

        Parameters:
            url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """
        return self._http_request('DELETE', url, **kwargs)

    @staticmethod
    def _http_request(method, url, headers=None, **kwargs):
        headers = requests.structures.CaseInsensitiveDict(headers)
        headers[Network.HEADERS.USER_AGENT] = Network.HOSTNAME

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            **kwargs
        )

        return response

    @classmethod
    def _process_data_and_headers(cls, data, headers):
        headers = requests.structures.CaseInsensitiveDict(headers)

        if isinstance(data, dict):
            data = serializers.serialize(data)
            headers[Network.HEADERS.CONTENT_TYPE] = 'application/json'
        return data, headers
