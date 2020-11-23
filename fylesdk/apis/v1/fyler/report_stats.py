"""
V1 Fyler Report Stats
"""

from typing import Dict

from ...api_base import ApiBase


class ReportStats(ApiBase):
    """Class for Report Stats APIs."""

    LIST_REPORT_STATS = '/report_stats'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, state=None, **kwargs) -> Dict:
        """
        Get Report Stats
        :param state:
        :return: Report Stats
        """
        return self.make_get_request(
            api_url=ReportStats.LIST_REPORT_STATS,
            query_params={
                'state': state,
                **kwargs
            }
        )
