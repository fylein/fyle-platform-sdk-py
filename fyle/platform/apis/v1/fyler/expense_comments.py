"""
V1 Admin Expense Comments
"""

from typing import Dict

from ....internals.list_resources import ListResources


class ExpenseComments(ListResources):
    """Class for Expense Comments APIs."""

    EXPENSE_COMMENT = '/expense_comments'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseComments.EXPENSE_COMMENT)
