"""
V1 Spender Corporate Cards
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class CorporateCardTransactions(ListResources, ListAllResources):
    """Class for Category APIs."""

    CORPORATE_CARD_TRANSACTIONS = '/corporate_card_transactions'

    def __init__(self, version, role):
        super().__init__(version, role, CorporateCardTransactions.CORPORATE_CARD_TRANSACTIONS)
