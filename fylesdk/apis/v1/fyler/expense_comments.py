"""
V1 Admin Expense Comments
"""

from typing import Dict

from ...api_base import ApiBase


class ExpenseComments(ApiBase):
    """Class for Expense Comments APIs."""

    POST_EXPENSE_COMMENT = '/expense_comments'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, payload) -> Dict:
        """
        Post Expense Comment
        :param payload: Expense Comment Object
        :return: Expense Comment Object
        """
        return self.make_post_request(
            api_url=ExpenseComments.POST_EXPENSE_COMMENT,
            payload=payload
        )
