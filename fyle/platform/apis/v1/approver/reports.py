"""
V1 Approver Reports
"""

from ....internals.list_resources import ListResources


class Reports(ListResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
