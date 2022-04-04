"""
V1 Beta Spender Expenses
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Expenses(ListResources, ListAllResources, PostResources):
    """Class for Expense APIs."""

    EXPENSES = '/expenses'
    ATTACH_RECEIPT = '/expenses/attach_receipt'

    def attach_receipt(self, payload):
        return self.api.make_post_request(
            api_url=Expenses.ATTACH_RECEIPT,
            payload=payload
        )

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)

    def create_expense(self, payload):
        return self.api.make_post_request(
            api_url=Expenses.EXPENSES,
            payload=payload
        )
