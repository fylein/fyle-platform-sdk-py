"""
V1 Approver Reports
"""

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources


class Reports(ListResources, GetResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
