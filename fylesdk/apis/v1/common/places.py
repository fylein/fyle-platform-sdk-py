"""
V1 Admin Places
"""

from typing import Dict

from .role import role
from ..version import version
from ...api_base import ApiBase


class Places(ApiBase):
    """Class for Places APIs."""

    GET_PLACES = '/places'

    def __init__(self):
        super().__init__(version, role)

    def get(self, q, types, location, **kwargs) -> Dict:
        """
        Get Places
        :param q:
        :param types:
        :param location:
        :return: List of Places Objects
        """
        return self.make_get_request(
            api_url=self.GET_PLACES,
            query_params={
                'q': q,
                'types': types,
                'location': location,
                **kwargs
            }
        )
