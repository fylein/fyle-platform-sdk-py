"""
V1 Admin Advances
"""

from typing import Dict

from ...api_base import ApiBase


class Advances(ApiBase):
    """Class for Advances APIs."""

    LIST_ADVANCES = '/advances'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, approved_at=None, settled_at=None,
        limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Advances
        :param created_at:
        :param updated_at:
        :param approved_at:
        :param settled_at:
        :param limit: No. of Advances to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Advances Objects
        """
        return self.make_get_request(
            api_url=Advances.LIST_ADVANCES,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'approved_at': approved_at,
                'settled_at': settled_at,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
