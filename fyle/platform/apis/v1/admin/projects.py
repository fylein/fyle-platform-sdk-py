"""
V1 Admin Projects
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Projects(ListResources, PostResources):
    """Class for Projects APIs."""

    PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)
