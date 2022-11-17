"""
V1 Beta Admin Departments
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources
from ....internals.post_resources import PostResources
from ....internals.get_resources import GetResources

class Departments(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Departments APIs."""

    DEPARTMENTS = '/departments'

    def __init__(self, version, role):
        super().__init__(version, role, Departments.DEPARTMENTS)
