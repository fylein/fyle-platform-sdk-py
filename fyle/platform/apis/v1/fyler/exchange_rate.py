"""
V1 Fyler Exchange Rate
"""

from typing import Dict

from ....internals.get_resources import GetResources


class ExchangeRate(GetResources):
    """Class for Exchange Rate APIs."""

    EXCHANGE_RATE = '/exchange_rate'

    def __init__(self, version, role):
        super().__init__(version, role, ExchangeRate.EXCHANGE_RATE)

    def get(self, query_params: Dict) -> Dict:
        """
        Get Expense Stats
        :param id: 
        :return: Resource Object
        """
        return self.make_get_request(
            api_url=ExchangeRate.EXCHANGE_RATE,
            query_params=query_params
        )
