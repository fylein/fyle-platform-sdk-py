"""
V1 Beta Spender Employees
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Employees(ListResources, ListAllResources):
    """Class for Employees APIs."""

    EMPLOYEES = '/employees'

    def __init__(self, version, role):
        super().__init__(version, role, Employees.EMPLOYEES)
