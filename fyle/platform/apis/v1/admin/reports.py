"""
V1 Admin Reports
"""

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources
from ....internals.post_resources import PostResources

class Reports(ListResources, GetResources, PostResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
