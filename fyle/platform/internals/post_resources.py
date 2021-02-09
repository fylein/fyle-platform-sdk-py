"""
    Defines Post resource class.
"""

from typing import Dict

from .api_base import ApiBase


class PostResources(ApiBase):
    """Post Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint

        api = super().__init__(self.version, self.role)
        self.make_get_request = api.make_get_request

    def post(self, payload: dict) -> Dict:
        """
        Creates or updates expense
        :param payload: Expense object
        :return: expenses Object
        """
        return self.make_post_request(
            api_url=self.endpoint,
            payload=payload
        )
