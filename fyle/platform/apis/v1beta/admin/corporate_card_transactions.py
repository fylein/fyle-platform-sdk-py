"""
V1 Beta Admin Corporate Card Transactions
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class CorporateCardTransactions(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Corporate Card Transactions APIs."""

    CORPORATE_CARD_TRANSACTIONS = '/corporate_card_transactions'

    def __init__(self, version, role):
        super().__init__(version, role, CorporateCardTransactions.CORPORATE_CARD_TRANSACTIONS)
