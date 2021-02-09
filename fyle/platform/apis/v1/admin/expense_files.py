"""
V1 Admin Expense Files
"""

from ....internals.post_resources import PostResources


class ExpenseFiles(PostResources):
    """Class for Expense Files APIs."""

    EXPENSE_FILES = '/expense_files'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseFiles.EXPENSE_FILES)
