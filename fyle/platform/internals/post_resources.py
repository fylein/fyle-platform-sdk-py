"""
    Defines Post resource class.
"""

from typing import Dict

from .api_base import ApiBase


class PostResources:
    """Post Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint
        self.api = ApiBase(self.version, self.role)

    def post(self, payload: dict) -> Dict:
        """
        Creates or updates expense
        :param payload: Expense object
        :return: expenses Object
        """
        return self.api.make_post_request(
            api_url=self.endpoint,
            payload=payload
        )
