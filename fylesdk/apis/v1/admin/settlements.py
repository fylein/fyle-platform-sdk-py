"""
V1 Admin Settlements
"""

from typing import Dict

from ...api_base import ApiBase


class Settlements(ApiBase):
    """Class for Settlements APIs."""

    LIST_SETTLEMENTS = '/settlements'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Settlements
        :param created_at:
        :param updated_at:
        :param limit: No. of Settlements to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Settlements Objects
        """
        return self.make_get_request(
            api_url=Settlements.LIST_SETTLEMENTS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
