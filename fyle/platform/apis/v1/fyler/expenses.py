"""
V1 Beta Spender Expenses
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Expenses(ListResources, ListAllResources):
    """Class for Expense APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
