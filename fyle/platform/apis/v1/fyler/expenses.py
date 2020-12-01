"""
V1 Fyler Expenses
"""

from ....internals.delete_resources import DeleteResources
from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Expenses(ListResources, GetResources, PostResources, DeleteResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
