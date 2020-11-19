"""
V1 Admin Categories
"""

from typing import Dict

from ...api_base import ApiBase


class Categories(ApiBase):
    """Class for Categories APIs."""

    GET_CATEGORIES = '/categories'
    POST_CATEGORIES = '/categories'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, email=None,
        limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Categories
        :param created_at:
        :param updated_at:
        :param email:
        :param limit: No. of Categories to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Categories Objects
        """
        return self.make_get_request(
            api_url=Categories.GET_CATEGORIES,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'email': email,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def post(self, payload) -> Dict:
        """
        Creates or updates Categories
        :param payload: Categories object
        :return: Categories object
        """
        return self.make_post_request(
            api_url=Categories.POST_CATEGORIES,
            payload=payload
        )
