"""
V1 Admin Projects
"""

from typing import Dict

from ...api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""

    GET_PROJECTS = '/projects'
    POST_PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, display_name=None, only_enabled=None,
        limit=None, offset=None, order=None, **kwargs) -> Dict:
        """
        Get Projects
        :param created_at:
        :param updated_at:
        :param display_name:
        :param only_enabled:
        :param limit: No. of projects to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of project objects
        """
        return self.make_get_request(
            api_url=Projects.GET_PROJECTS,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'display_name': display_name,
                'only_enabled': only_enabled,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def post(self, payload) -> Dict:
        """
        Creates or updates project
        :param payload: Object of project
        :return: Project object
        """
        return self.make_post_request(
            api_url=Projects.POST_PROJECTS,
            payload=payload
        )
