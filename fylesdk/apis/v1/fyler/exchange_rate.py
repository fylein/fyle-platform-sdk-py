"""
V1 Fyler Exchange Rate
"""

from typing import Dict

from ...api_base import ApiBase


class ExchangeRate(ApiBase):
    """Class for Exchange Rate APIs."""

    LIST_EXCHANGE_RATE = '/exchange_rate'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, from_currency=None, to_currency=None, date=None, **kwargs) -> Dict:
        """
        Get Exchange Rate
        :param from_currency:
        :param to_currency:
        :param date:
        :return: Exchange Rate
        """
        return self.make_get_request(
            api_url=ExchangeRate.LIST_EXCHANGE_RATE,
            query_params={
                'from_currency': from_currency,
                'to_currency': to_currency,
                'date': date,
                **kwargs
            }
        )
