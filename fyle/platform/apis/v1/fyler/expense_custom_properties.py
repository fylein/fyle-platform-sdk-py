"""
V1 Fyler Expense Custom Properties
"""

from typing import Dict

from ....internals.list_resources import ListResources


class ExpenseCustomProperties(ListResources):
    """Class for Expense Custom Properties APIs."""

    EXPENSE_CUSTOM_PROPERTIES = '/expense_custom_properties'

    def __init__(self, version, role):
        super().__init__(version, role, ExpenseCustomProperties.EXPENSE_CUSTOM_PROPERTIES)
