"""
V1 Fyler Expenses
"""

from typing import Dict

from ...api_base import ApiBase


class Expenses(ApiBase):
    """Class for Expenses APIs."""

    LIST_EXPENSES = '/expenses'
    GET_EXPENSES = '/expenses/{id}'
    POST_EXPENSES = '/expenses'
    DELETE_EXPENSES = '/expenses/{id}'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, invoice_number=None, source_account_type=None,
             limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Expenses
        :param created_at:
        :param invoice_number:
        :param source_account_type:
        :param limit: No. of employees to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Expense Objects
        """
        return self.make_get_request(
            api_url=Expenses.LIST_EXPENSES,
            query_params={
                'created_at': created_at,
                'invoice_number': invoice_number,
                'source_account.type': source_account_type,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def get(self, id) -> Dict:
        """
        Get Single Expense by ID
        :param id: Expense ID
        :return: Expense Object
        """
        return self.make_get_request(
            api_url=Expenses.GET_EXPENSES.format(id)
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

    def delete(self, id):
        """
        Deletes the expense
        :param id: Expense id
        :return: Status
        """
        return self.make_delete_request(
            api_url=Expenses.DELETE_EXPENSES.format(id)
        )
