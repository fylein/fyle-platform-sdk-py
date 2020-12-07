"""
V1 Admin Expense Comments
"""

from ....internals.post_resources import PostResources


class ExpenseComments(PostResources):
    """Class for Expense Comments APIs."""

    EXPENSE_COMMENT = '/expense_comments'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseComments.EXPENSE_COMMENT)
