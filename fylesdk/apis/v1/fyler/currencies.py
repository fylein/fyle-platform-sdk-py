"""
V1 Fyler Currencies
"""

from typing import Dict

from ...api_base import ApiBase


class Currencies(ApiBase):
    """Class for Currencies APIs."""

    LIST_CURRENCIES = '/currencies'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, **kwargs) -> Dict:
        """
        Get Currencies
        :return: List of Currencies
        """
        return self.make_get_request(
            api_url=Currencies.LIST_CURRENCIES,
            query_params={
                **kwargs
            }
        )
