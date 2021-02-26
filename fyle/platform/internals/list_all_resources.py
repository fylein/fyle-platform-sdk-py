"""
    Defines List resource class.
"""
from typing import Iterable

from .api_base import ApiBase
from .. import exceptions


class ListAllResources:
    """List All Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint
        self.api = ApiBase(self.version, self.role)

    def list_all(self, query_params=None) -> Iterable:
        """
        Get Resources
        :param query_params:
        :return: List of Resource Objects
        """
        query_params = {} if query_params is None else query_params
        if 'offset' in query_params or 'limit' in query_params:
            raise exceptions.WrongParamsError('offset, limit should not be used with list_all')
        if 'order' not in query_params:
            raise exceptions.WrongParamsError('Mandatory query params missing: order is mandatory query param.')
        count = 1
        total_count = 0
        while total_count < count:
            resp = self.api.make_get_request(
                api_url=self.endpoint,
                query_params=query_params
            )
            data_size = len(resp.get('data'))
            total_count = total_count + data_size
            count = resp.get('count')
            query_params.update({'offset': total_count, 'limit': data_size})
            yield resp
