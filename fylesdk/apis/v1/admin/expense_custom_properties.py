"""
V1 Admin Expense Custom Properties
"""

from typing import Dict

from ...api_base import ApiBase


class ExpenseCustomProperties(ApiBase):
    """Class for Expense Custom Properties APIs."""

    LIST_EXPENSE_CUSTOM_PROPERTIES = '/expense_custom_properties'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, name=None, only_enabled=None,
             limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Expense Custom Properties
        :param created_at:
        :param updated_at:
        :param name:
        :param only_enabled:
        :param limit: No. of Expense Custom Properties to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Expense Custom Properties object
        """
        return self.make_get_request(
            api_url=ExpenseCustomProperties.LIST_EXPENSE_CUSTOM_PROPERTIES,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'name': name,
                'only_enabled': only_enabled,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )
