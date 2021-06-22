"""
    Defines Get resource class.
"""

from typing import Dict
from .. import exceptions
from .api_base import ApiBase


class GetResources:
    """Get Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        self.api = ApiBase(self.version, self.role)

    def get(self, id_: str = None, query_params=None) -> Dict:
        """
        Get Single Resource object by ID
        :param id_: Resource object ID
        :param query_params:
        :return: Resource Object
        """
        query_params = {} if query_params is None else query_params
        api_url = self.endpoint

        if id_:
            query_params['id'] = 'eq.{}'.format(id_)

        response = self.api.make_get_request(
            api_url=api_url,
            query_params=query_params,
        )

        if id_ and response['count'] < 1:
            raise exceptions.NotFoundItemError('Not found item with ID')
        elif id_ and response['count'] > 1:
            raise exceptions.MultipleObjectReturned('Multiple Objects returned')

        return response
