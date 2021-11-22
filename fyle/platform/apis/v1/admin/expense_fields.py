"""
V1 Beta Admin Expense Fields
"""

from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class ExpenseFields(ListResources, ListAllResources, PostResources):
    """Class for Expense Fields APIs."""

    EXPENSE_FIELDS = '/expense_fields'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFields.EXPENSE_FIELDS)
