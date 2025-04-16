"""
V1 Admin Expenses
"""
from typing import Dict

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Expenses(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'
    ACCOUNTING_EXPORT_SUMMARY_BULK = '/expenses/accounting_export_summary/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)

    def post_bulk_accounting_export_summary(self, payload: dict) -> Dict:
        return self.api.make_post_request(
            api_url=self.ACCOUNTING_EXPORT_SUMMARY_BULK,
            payload=payload
        )
