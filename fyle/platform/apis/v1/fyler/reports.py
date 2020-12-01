"""
V1 Fyler Reports
"""

from ....internals.post_resources import PostResources


class Reports(PostResources):
    """Class for Reports APIs."""

    REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role, Reports.REPORTS)
