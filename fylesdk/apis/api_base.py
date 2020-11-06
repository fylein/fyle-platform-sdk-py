"""
    Define ApiBase class implementing API helper methods.
"""

import json

from ..globals.configs import sdk
from ..internals.network import Network


class ApiBase(Network):
    """The base class for all API classes."""

    def __init__(self, version=None, role=None):
        super().__init__()

        self.version = version
        self.role = role

    def _format_api_url(self, endpoint):
        return '{base_url}/{version}/{role}{endpoint}'.format(
            base_url=sdk.config['SERVER_URL'],
            version=self.version,
            role=self.role,
            endpoint=endpoint
        )

    # def get_all(self):
    #     """
    #     Get all the Objects based on paginated call
    #     """

    #     count = self.count()['count']
    #     objects = []
    #     page_size = 200
    #     for i in range(0, count, page_size):
    #         segment = self.get(offset=i, limit=page_size)
    #         objects = objects + segment['data']
    #     return objects

    def make_get_request(self, api_url, query_params):
        """Create a HTTP GET request.

        Parameters:
            query_params (dict): HTTP GET parameters for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {'Authorization': 'Bearer {0}'.format(sdk.config['ACCESS_TOKEN'])}
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

        self._assert_response(response)

        return None

    def make_post_request(self, api_url, payload):
        """Create a HTTP post request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {'Authorization': 'Bearer {0}'.format(sdk.config['ACCESS_TOKEN'])}

        response = self.post_request(
            url='{0}{1}'.format(sdk.config['SERVER_URL'], api_url),
            headers=api_headers,
            json=payload
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

        self._assert_response(response)

        return None
