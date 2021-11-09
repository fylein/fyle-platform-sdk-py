"""
V1 Common Currencies
"""

from ....internals.list_resources import ListResources


class Currencies(ListResources):
    """Class for Currencies APIs."""

    CURRENCIES = "/currency/list"

    def __init__(self, version, role):
        super().__init__(version, role, Currencies.CURRENCIES)
