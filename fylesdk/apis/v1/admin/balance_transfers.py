"""
V1 Admin Balance Transfers
"""

from typing import Dict

from ...api_base import ApiBase


class BalanceTransfers(ApiBase):
    """Class for Balance Transfers APIs."""

    GET_BALANCE_TRANSFERS = '/balance_transfers'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Balance Transfers
        :param created_at:
        :param updated_at:
        :param limit: No. of Balance Transfers to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Balance Transfers Objects
        """
        return self.make_get_request(
            api_url=BalanceTransfers.GET_BALANCE_TRANSFERS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
