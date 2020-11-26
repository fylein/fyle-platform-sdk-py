"""
    Defines List resource class.
"""

from typing import Dict

from .api_base import ApiBase


class ListResources(ApiBase):

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = ApiBase(self.version, self.role)
        self.make_get_request = api.make_get_request

    def list(self, query_params: dict = {}) -> Dict:
        """
        Get Resources
        :param query_params:
        :return: List of Resource Objects
        """
        return self.make_get_request(
            api_url=self.endpoint,
            query_params=query_params
        )