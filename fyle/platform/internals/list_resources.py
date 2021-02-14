"""
    Defines List resource class.
"""

from typing import Dict

from .api_base import ApiBase


class ListResources:
    """List Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint
        self.api = ApiBase(self.version, self.role)

    def list(self, query_params=None) -> Dict:
        """
        Get Resources
        :param query_params:
        :return: List of Resource Objects
        """
        query_params = {} if query_params is None else query_params
        if query_params.get('offset') or query_params.get('limit'):
            return self.api.make_get_request(
                api_url=self.endpoint,
                query_params=query_params
            )
        else:
            first_response = self.api.make_get_request(
                api_url=self.endpoint,
                query_params=query_params
            )
            count = first_response.get('count')
            limit = len(first_response.get('data')) if first_response.get('data') else 0
            for offset in range(limit, count, limit):
                query_params.update({'offset': offset, 'limit': limit})
                resp = self.api.make_get_request(
                    api_url=self.endpoint,
                    query_params=query_params
                )
                first_response.get('data').extend(resp.get('data'))
            return first_response
