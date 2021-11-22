"""
V1 Beta Admin Expenses
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Expenses(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
