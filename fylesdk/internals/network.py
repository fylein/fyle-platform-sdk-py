"""
    Defining Network related operations
"""

import os

import requests

from . import serializers
from .. import exceptions

class Network:
    """Class for making GET, POST requests"""
    HOSTNAME = None
    HEADERS = serializers.deserialize({
            'USER_DETAILS': 'X-User-Details',
            'AUTHORIZATION': 'Authorization',
            'CONTENT_TYPE': 'Content-Type',
            'USER_AGENT': 'User-Agent',
            'FYLE_SIGNATURE': 'X-Fyle-Signature',
            'S3_SIGNATURE': 'X-Amz-Signature'
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

        return self._get(url, **kwargs)


    def post_request(self, url, **kwargs):
        """Create a HTTP post request.

        Parameters:
            url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """
        return self._post(url, **kwargs)


    def delete_request(self, url, **kwargs):
        """Create a HTTP delete request.

        Parameters:
            url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """
        return self._delete(url, **kwargs)


    def _assert_response(self, response):
        if response.status_code == 400:
            raise exceptions.WrongParamsError(
                'Some of the parameters are wrong', response.text)
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
        raise exceptions.FylePlatformSDKError(
            'Error: {0}'.format(response.status_code), response.text)


    def _get(self, url, **kwargs):
        # https://2.python-requests.org/en/master/_modules/requests/api/#get
        kwargs.setdefault('allow_redirects', True)
        return self._http_request('GET', url, **kwargs)


    def _post(self, url, data=None, headers=None, **kwargs):
        data, headers = self._process_data_and_headers(data, headers)
        return self._http_request('POST', url, headers=headers, data=data, **kwargs)


    def _delete(self, url, **kwargs):
        return self._http_request('DELETE', url, **kwargs)


    def _http_request(self, method, url, headers=None, **kwargs):
        headers = requests.structures.CaseInsensitiveDict(headers)
        headers[Network.HEADERS.USER_AGENT] = Network.HOSTNAME

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            **kwargs
        )

        return response


    def _process_data_and_headers(self, data, headers):
        headers = requests.structures.CaseInsensitiveDict(headers)

        if isinstance(data, dict):
            data = serializers.serialize(data)
            headers[Network.HEADERS.CONTENT_TYPE] = 'application/json'
        return data, headers
