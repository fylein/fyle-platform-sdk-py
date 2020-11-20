"""
V1 Fyler Trip Requests Stats
"""

from typing import Dict

from ...api_base import ApiBase


class TripRequestsStats(ApiBase):
    """Class for Trip Requests Stats APIs."""

    LIST_TRIP_REQUESTS_STATS = '/trip_requests_stats'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, sent_back=None, state=None, **kwargs) -> Dict:
        """
        Get Trip Requests Stats
        :param sent_back:
        :param state:
        :return: Trip Requests Stats
        """
        return self.make_get_request(
            api_url=TripRequestsStats.LIST_TRIP_REQUESTS_STATS,
            query_params={
                'sent_back': sent_back,
                'state': state,
                **kwargs
            }
        )
