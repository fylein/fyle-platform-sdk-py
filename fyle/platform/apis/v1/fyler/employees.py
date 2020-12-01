"""
V1 Admin Employees
"""

from ....internals.get_resources import GetResources


class Employees(GetResources):
    """Class for Employees APIs."""

    EMPLOYEES = ''

    def __init__(self, version, role):
        super().__init__(version, role, Employees.EMPLOYEES)
