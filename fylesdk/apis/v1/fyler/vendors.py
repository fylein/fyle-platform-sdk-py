"""
V1 Fyler Vendors
"""

from typing import Dict

from ...api_base import ApiBase


class Vendors(ApiBase):
    """Class for Vendors APIs."""

    LIST_VENDORS = '/vendors'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, q=None,
             limit=None, offset=None, **kwargs) -> Dict:
        """
        Get Vendors
        :param created_at:
        :param updated_at:
        :param q: Query
        :param limit: No. of Vendors to be fetched
        :param offset: Pagination offset
        :return: List of Vendors Objects
        """
        return self.make_get_request(
            api_url=Vendors.LIST_VENDORS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'q': q,
                'limit': limit,
                'offset': offset,
                **kwargs
            }
        )
