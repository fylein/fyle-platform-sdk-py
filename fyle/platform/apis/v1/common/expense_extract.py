"""
V1 Common Expense Extract
"""

from ....internals.post_resources import PostResources


class ExpenseExtract(PostResources):
    """Class for Expense Extract APIs"""

    EXPENSE_EXTRACT = "/expense_extract/v1"

    def __init__(self, version, role) -> None:
        super().__init__(version, role, ExpenseExtract.EXPENSE_EXTRACT)
