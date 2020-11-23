"""
V1 Fyler Categories
"""

from typing import Dict

from ...api_base import ApiBase


class Categories(ApiBase):
    """Class for Categories APIs."""

    LIST_CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, only_enabled=None,
             limit=None, offset=None, **kwargs) -> Dict:
        """
        Get Categories
        :param created_at:
        :param updated_at:
        :param only_enabled:
        :param limit: No. of Categories to be fetched
        :param offset: Pagination offset
        :return: List of Categories Objects
        """
        return self.make_get_request(
            api_url=Categories.LIST_CATEGORIES,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'only_enabled': only_enabled,
                'limit': limit,
                'offset': offset,
                **kwargs
            }
        )
