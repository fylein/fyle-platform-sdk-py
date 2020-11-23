"""
V1 Admin Refunds
"""

from typing import Dict

from ...api_base import ApiBase


class Refunds(ApiBase):
    """Class for Refunds APIs."""

    LIST_REFUNDS = '/refunds'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, limit=None,
             offset=None, order=None, **kwargs) -> Dict:
        """
        Get Refunds
        :param created_at:
        :param updated_at:
        :param limit: No. of Refunds to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Refunds Objects
        """
        return self.make_get_request(
            api_url=Refunds.LIST_REFUNDS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
