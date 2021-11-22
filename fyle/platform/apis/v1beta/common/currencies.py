"""
V1 Beta Common Currencies
"""

from typing import Dict

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources

class Currencies(ListResources):
    """Class for Currencies APIs."""

    CURRENCIES = "/currency/list"

    def __init__(self, version, role):
        super().__init__(version, role, Currencies.CURRENCIES)

    def list(self):
        """
        To get object of currencies
        :return: currencies object
        """
        return self.api.make_get_request(
            api_url=self.endpoint,
            query_params={}
        )


class CurrenciesExchangeRate(GetResources):
    """Class for Currencies Exchange Rate APIs."""

    CURRENCIES_EXCHANGE_RATE = "/currency/exchange_rate"

    def __init__(self, version, role):
        super().__init__(version, role, CurrenciesExchangeRate.CURRENCIES_EXCHANGE_RATE)

    def get(self, from_, to_, date) -> Dict:
        """
        To get object of currencies exchange rate
        :return: currencies exchange rate
        """
        query_params = {
            'from': from_,
            'to': to_,
            'date': date
        }

        return self.api.make_get_request(
            api_url=self.endpoint,
            query_params=query_params
        )
