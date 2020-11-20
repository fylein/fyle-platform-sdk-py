"""
V1 Fyler Advance Requests Stats
"""

from typing import Dict

from ...api_base import ApiBase


class AdvanceRequestsStats(ApiBase):
    """Class for Advance Requests Stats APIs."""

    LIST_ADVANCE_REQUESTS_STATS = '/advance_requests_stats'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, sent_back=None, state=None, **kwargs) -> Dict:
        """
        Get Advance Requests Stats
        :param sent_back:
        :param state:
        :return: Advance Requests Stats
        """
        return self.make_get_request(
            api_url=AdvanceRequestsStats.LIST_ADVANCE_REQUESTS_STATS,
            query_params={
                'sent_back': sent_back,
                'state': state,
                **kwargs
            }
        )
