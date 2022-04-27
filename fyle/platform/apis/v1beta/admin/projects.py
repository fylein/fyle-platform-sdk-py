"""
V1 Beta Admin Projects
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources
from ....internals.post_bulk_resources import PostBulkResources

class Projects(ListResources, ListAllResources, PostResources, PostBulkResources):
    """Class for Projects APIs."""

    PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)
