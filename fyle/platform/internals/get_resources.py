"""
    Defines Get resource class.
"""

from typing import Dict

from .api_base import ApiBase


class GetResources(ApiBase):
    """Get Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = super().__init__(self.version, self.role)
        self.make_get_request = api.make_get_request

    def get(self, id_: str = None, query_params=None) -> Dict:
        """
        Get Single Resource object by ID
        :param id_: Resource object ID
        :param query_params:
        :return: Resource Object
        """
        query_params = {} if query_params is None else query_params
        if id_:
            api_url = '{endpoint}/{id}'.format(endpoint=self.endpoint, id=id)
        else:
            api_url = self.endpoint

        return self.make_get_request(
            api_url=api_url,
            query_params=query_params,
        )
