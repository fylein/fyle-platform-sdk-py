"""
V1 Admin Balance Transfers
"""

from ....internals.list_resources import ListResources


class BalanceTransfers(ListResources):
    """Class for Balance Transfers APIs."""

    BALANCE_TRANSFERS = '/balance_transfers'

    def __init__(self, version, role):
        super().__init__(version, role, BalanceTransfers.BALANCE_TRANSFERS)
