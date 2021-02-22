"""
V1 Admin EmployeeApprovers
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class EmployeeApprovers(ListResources, ListAllResources, GetResources):
    """Class for EmployeeApprovers APIs."""

    EMPLOYEE_APPROVERS = '/employee_approvers'

    def __init__(self, version, role):
        super().__init__(version, role, EmployeeApprovers.EMPLOYEE_APPROVERS)
