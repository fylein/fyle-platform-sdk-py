"""
V1 Beta Admin Corporate Cards
"""

from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class CorporateCards(ListResources, ListAllResources):
    """Class for Corporate Cards APIs."""

    EXPENSE_FIELDS = '/corporate_cards'

    def __init__(self, version, role):
        super().__init__(version, role, CorporateCards.EXPENSE_FIELDS)
