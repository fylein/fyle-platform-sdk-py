"""
V1 Admin Projects
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources
from ....internals.post_bulk_resources import PostBulkResources

class Projects(ListResources, ListAllResources, PostResources, PostBulkResources):
    """Class for Projects APIs."""

    PROJECTS = '/projects'
    PROJECTS_DELETE_BULK = '/projects/delete/bulk'
    PROJECTS_DELETE_SUMMARY_BULK = '/projects/delete_summary/bulk'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)

    def delete_summary_bulk(self, data):
        return self.post(Projects.PROJECTS_DELETE_SUMMARY_BULK, data)

    def delete_bulk(self, data):
        return self.post(Projects.PROJECTS_DELETE_BULK, data)
