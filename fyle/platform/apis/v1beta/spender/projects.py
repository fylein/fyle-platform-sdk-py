"""
V1 Beta Spender Projects
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Projects(ListResources, ListAllResources):
    """Class for Project APIs."""

    PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)
