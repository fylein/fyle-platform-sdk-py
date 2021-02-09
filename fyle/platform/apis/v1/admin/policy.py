"""
V1 Admin Policy
"""

from typing import Dict

from ....internals.api_base import ApiBase


class Policy:
    """Class for Policy APIs."""

    TEST_POLICY = '/policy_test'

    def __init__(self, version, role):
        self.version = version
        self.role = role

    def test(self, payload) -> Dict:
        """
        Test's Policy against an expense
        :param payload: Expense Object
        :return: Policy Test Object
        """
        api = ApiBase(self.version, self.role)

        return api.make_post_request(
            api_url=Policy.TEST_POLICY,
            payload=payload
        )
