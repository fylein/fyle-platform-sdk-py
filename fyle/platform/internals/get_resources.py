"""
    Defines Get resource class.
"""

from typing import Dict

from .api_base import ApiBase


class GetResources():

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = ApiBase(self.version, self.role)
        self.make_get_request = api.make_get_request

    def get(self, id: str = None, query_params: dict = {}) -> Dict:
        """
        Get Single Resource object by ID
        :param id: Resource object ID
        :return: Resource Object
        """
        if id:
            api_url = '{endpoint}/{id}'.format(endpoint=self.endpoint, id=id)
        else:
            api_url = self.endpoint

        return self.make_get_request(
            api_url=api_url,
            query_params=query_params,
        )