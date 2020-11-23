"""
V1 Fyler Policy
"""

from typing import Dict

from ...api_base import ApiBase


class Policy(ApiBase):
    """Class for Policy APIs."""

    POST_TEST_POLICY = '/policy_test'

    def __init__(self, version, role):
        super().__init__(version, role)

    def test(self, payload) -> Dict:
        """
        Test's Policy against an expense
        :param payload: Expense Object
        :return: Policy Test Object
        """
        return self.make_post_request(
            api_url=Policy.POST_TEST_POLICY,
            payload=payload
        )
