"""
V1 Beta Spender Reports
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class Reports(ListResources, ListAllResources):
    """Class for Report APIs."""

    REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
