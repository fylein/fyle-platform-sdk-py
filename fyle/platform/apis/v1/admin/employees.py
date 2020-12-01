"""
V1 Admin Employees
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Employees(ListResources, PostResources):
    """Class for Employees APIs."""

    EMPLOYEES = '/employees'

    def __init__(self, version, role):
        super().__init__(version, role, Employees.EMPLOYEES)
