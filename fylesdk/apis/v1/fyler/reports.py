"""
V1 Fyler Reports
"""

from typing import Dict

from ...api_base import ApiBase


class Reports(ApiBase):
    """Class for Reports APIs."""

    POST_REPORTS = '/reports'

    def __init__(self, version, role):
        super().__init__(version, role)

    def post(self, payload) -> Dict:
        """
        Creates a Report
        :param payload: Report object
        :return: Report Object
        """
        return self.make_post_request(
            api_url=Reports.POST_REPORTS,
            payload=payload
        )
