"""
V1 Fyler Expense Stats
"""

from typing import Dict

from ....internals.get_resources import GetResources


class ExpenseStats(GetResources):
    """Class for Expense Stats APIs."""

    EXPENSE_STATS = '/expense_stats'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseStats.EXPENSE_STATS)
