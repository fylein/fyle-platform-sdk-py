"""
V1 Admin Expenses
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources
from ....internals.delete_resources import DeleteResources
from ....internals.get_resources import GetResources


class Expenses(ListResources, PostResources, GetResources, DeleteResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
