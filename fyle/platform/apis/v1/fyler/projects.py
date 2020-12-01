"""
V1 Fyler Projects
"""

from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources


class Projects(ListResources, GetResources):
    """Class for Projects APIs."""

    PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)
