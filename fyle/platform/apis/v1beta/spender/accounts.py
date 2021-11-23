"""
V1 Beta Spender Accounts
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Accounts(ListResources, ListAllResources):
    """Class for Merchant APIs."""

    ACCOUNTS = '/accounts'

    def __init__(self, version, role):
        super().__init__(version, role, Accounts.ACCOUNTS)
