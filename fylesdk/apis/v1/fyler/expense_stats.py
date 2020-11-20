"""
V1 Fyler Expense Stats
"""

from typing import Dict

from ...api_base import ApiBase


class ExpenseStats(ApiBase):
    """Class for Expense Stats APIs."""

    LIST_EXPENSE_STATS = '/expense_stats'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, policy_amount=None, policy_flag=None, state=None, **kwargs) -> Dict:
        """
        Get Expense Stats
        :param policy_amount:
        :param policy_flag:
        :param state:
        :return: Expense Stats
        """
        return self.make_get_request(
            api_url=ExpenseStats.LIST_EXPENSE_STATS,
            query_params={
                'policy_amount': policy_amount,
                'policy_flag': policy_flag,
                'state': state,
                **kwargs
            }
        )
