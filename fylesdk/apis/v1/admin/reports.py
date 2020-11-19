"""
V1 Admin Reports
"""

from typing import Dict

from ...api_base import ApiBase


class Reports(ApiBase):
    """Class for Reports APIs."""

    GET_REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, approved_at=None, 
        settled_at=None, reimbursed_at=None, state=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Reports
        :param created_at:
        :param updated_at:
        :param approved_at:
        :param settled_at:
        :param reimbursed_at:
        :param state:
        :param limit: No. of Reports to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Reports Objects
        """
        return self.make_get_request(
            api_url=Reports.GET_REPORTS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'approved_at': approved_at,
                'settled_at': settled_at,
                'reimbursed_at': reimbursed_at,
                'state': state,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
