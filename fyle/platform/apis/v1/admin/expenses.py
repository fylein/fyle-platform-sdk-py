"""
V1 Admin Expenses
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Expenses(ListResources, PostResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
