"""
V1 Fyler Expenses
"""

from typing import Dict

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources
from ....internals.post_resources import PostResources
from ....internals.delete_resources import DeleteResources


class Expenses(ListResources, GetResources, PostResources, DeleteResources):
    """Class for Expenses APIs."""

    EXPENSES = '/expenses'

    def __init__(self, version, role):
        super().__init__(version, role, Expenses.EXPENSES)
