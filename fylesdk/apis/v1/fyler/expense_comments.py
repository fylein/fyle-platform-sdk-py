"""
V1 Admin Expense Comments
"""

from typing import Dict

from .role import role
from ..version import version
from ...api_base import ApiBase


class ExpenseComments(ApiBase):
    """Class for Expense Comments APIs."""

    POST_EXPENSE_COMMENT = '/expense_comment'

    def __init__(self):
        super().__init__(version, role)

    def post(self, payload) -> Dict:
        """
        Post Expense Comment
        :param payload: Expense Comment Object
        :return: Expense Comment Object
        """
        return self.make_post_request(
            api_url=ExpenseComments.POST_EXPENSE_COMMENT,
            payload=payload
        )