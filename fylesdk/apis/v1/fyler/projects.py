"""
V1 Fyler Projects
"""

from typing import Dict

from ...api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""

    LIST_PROJECTS = '/projects'
    GET_PROJECTS = '/projects/{id}'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, only_enabled=None,
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
            api_url=Projects.LIST_PROJECTS,
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

    def get(self, id) -> Dict:
        """
        Get Single Project by ID
        :param id: Project ID
        :return: Project Object
        """
        return self.make_get_request(
            api_url=Projects.GET_PROJECTS.format(id)
        )
