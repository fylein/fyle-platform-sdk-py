"""
V1 Fyler Trip Requests Stats
"""

from ....internals.get_resources import GetResources


class TripRequestsStats(GetResources):
    """Class for Trip Requests Stats APIs."""

    TRIP_REQUESTS_STATS = '/trip_requests_stats'

    def __init__(self, version, role):
        super().__init__(version, role, TripRequestsStats.TRIP_REQUESTS_STATS)
