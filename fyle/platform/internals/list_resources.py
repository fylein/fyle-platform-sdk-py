"""
    Defines List resource class.
"""

from typing import Dict

from .api_base import ApiBase


class ListResources(ApiBase):
    """List Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = ApiBase(self.version, self.role)
        self.make_get_request = api.make_get_request

    def list(self, query_params=None) -> Dict:
        """
        Get Resources
        :param query_params:
        :return: List of Resource Objects
        """
        query_params = {} if query_params is None else query_params
        return self.make_get_request(
            api_url=self.endpoint,
            query_params=query_params
        )
