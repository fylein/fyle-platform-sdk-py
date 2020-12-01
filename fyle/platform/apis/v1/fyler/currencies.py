"""
V1 Fyler Currencies
"""

from ....internals.list_resources import ListResources


class Currencies(ListResources):
    """Class for Currencies APIs."""

    CURRENCIES = '/currencies'

    def __init__(self, version, role):
        super().__init__(version, role, Currencies.CURRENCIES)
