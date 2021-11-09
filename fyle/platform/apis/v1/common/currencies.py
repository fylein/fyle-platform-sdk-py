"""
V1 Common Currencies
"""

from ....internals.list_resources import ListResources


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
