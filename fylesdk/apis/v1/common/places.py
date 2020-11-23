"""
V1 Common Places
"""

from typing import Dict

from ...api_base import ApiBase


class Places(ApiBase):
    """Class for Places APIs."""

    LIST_PLACES = '/places'
    GET_PLACES = '/places/{id}'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, q, types, location=None, **kwargs) -> Dict:
        """
        Get Places
        :param q:
        :param types:
        :param location:
        :return: List of Places Objects
        """
        return self.make_get_request(
            api_url=Places.LIST_PLACES,
            query_params={
                'q': q,
                'types': types,
                'location': location,
                **kwargs
            }
        )

    def get(self, id) -> Dict:
        """
        Get Place details
        :param id: Place ID
        :return: Place Object
        """
        return self.make_get_request(
            api_url=Places.GET_PLACES.format(id)
        )
