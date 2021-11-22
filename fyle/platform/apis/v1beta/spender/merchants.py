"""
V1 Beta Spender Merchants
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Merchants(ListResources, ListAllResources):
    """Class for Merchant APIs."""

    MERCHANTS = '/merchants'

    def __init__(self, version, role):
        super().__init__(version, role, Merchants.MERCHANTS)
