"""
V1 Admin Reimbursements
"""

from typing import Dict

from ...api_base import ApiBase


class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""

    GET_REIMBURSEMENTS = '/reimbursements'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Reimbursements
        :param created_at:
        :param updated_at:
        :param limit: No. of Reimbursements to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Reimbursements Objects
        """
        return self.make_get_request(
            api_url=Reimbursements.GET_REIMBURSEMENTS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
