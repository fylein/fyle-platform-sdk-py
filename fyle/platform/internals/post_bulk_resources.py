"""
    Defines Bulk Post resource class.
"""

from typing import Dict

from .api_base import ApiBase


class PostBulkResources:
    """Bulk Post Resource Class"""

    def __init__(self, version, role, endpoint):
        self.version = version
        self.role = role
        self.endpoint = endpoint
        self.api = ApiBase(self.version, self.role)

    def post_bulk(self, payload: dict) -> Dict:
        """
        Creates or updates resources in bulk.
        :param payload: top-level object containing data which is a array of objects.
            example: {"data": [{object 1}, {object 2}]}
        :return: empty response
        """
        return self.api.make_post_request(
            api_url='{}/bulk'.format(self.endpoint),
            payload=payload
        )
