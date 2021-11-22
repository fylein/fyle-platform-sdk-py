"""
V1 Beta Spender Expense Fields
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class ExpenseFields(ListResources, ListAllResources):
    """Class for Expense Field APIs."""

    EXPENSE_FIELDS = '/expense_fields'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFields.EXPENSE_FIELDS)
