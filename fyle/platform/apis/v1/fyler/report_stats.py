"""
V1 Fyler Report Stats
"""

from ....internals.get_resources import GetResources


class ReportStats(GetResources):
    """Class for Report Stats APIs."""

    REPORT_STATS = '/report_stats'

    def __init__(self, version, role):
        super().__init__(version, role, ReportStats.REPORT_STATS)
