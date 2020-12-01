"""
V1 Fyler Projects
"""

from typing import Dict

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources


class Projects(ListResources, GetResources):
    """Class for Projects APIs."""

    PROJECTS = '/projects'

    def __init__(self, version, role):
        super().__init__(version, role, Projects.PROJECTS)
