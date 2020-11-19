"""
V1 Admin Expenses
"""

from typing import Dict

from ...api_base import ApiBase


class Expenses(ApiBase):
    """Class for Expenses APIs."""

    GET_EXPENSES = '/expenses'
    POST_EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, approved_at=None, created_at=None, updated_at=None,
        employee_email=None, state=None, verified=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Expenses
        :param approved_at:
        :param created_at:
        :param updated_at:
        :param employee_email:
        :param state:
        :param verified:
        :param limit: No. of employees to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Expense Objects
        """
        return self.make_get_request(
            api_url=Expenses.GET_EXPENSES,
            query_params={
                'approved_at': approved_at,
                'created_at': created_at,
                'updated_at': updated_at,
                'employee.email': employee_email,
                'state': state,
                'verified': verified,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def post(self, payload) -> Dict:
        """
        Creates or updates expense
        :param payload: Expense object
        :return: expenses Object
        """
        return self.make_post_request(
            api_url=Expenses.POST_EXPENSES,
            payload=payload
        )
