"""
    Defines List resource class.
"""

from typing import Dict

from fyle.platform import exceptions
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
        if not str(query_params.get('offset')) or not str(query_params.get('limit')) or not query_params.get('order'):
            raise exceptions.WrongParamsError(
                'Mandatory query params missing: offset, limit and order are mandatory query params.')
        return self.api.make_get_request(
            api_url=self.endpoint,
            query_params=query_params
        )
