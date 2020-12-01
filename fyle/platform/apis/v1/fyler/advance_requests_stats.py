"""
V1 Fyler Advance Requests Stats
"""

from ....internals.get_resources import GetResources


class AdvanceRequestsStats(GetResources):
    """Class for Advance Requests Stats APIs."""

    ADVANCE_REQUESTS_STATS = '/advance_requests_stats'

    def __init__(self, version, role):
        super().__init__(version, role, AdvanceRequestsStats.ADVANCE_REQUESTS_STATS)
