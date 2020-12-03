"""
V1 Admin Expense Custom Properties
"""

from ....internals.list_resources import ListResources


class ExpenseFields(ListResources):
    """Class for Expense Custom Properties APIs."""

    Expense_Fields = '/expense_fields'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFields.Expense_Fields)
