"""
V1 Approver Report Approvals
"""

from typing import Dict

from ...api_base import ApiBase


class ReportApprovals(ApiBase):
    """Class for Report Approvals APIs."""

    POST_REPORT_APPROVALS = '/report_approvals'

    def __init__(self, version, role):
        super().__init__(version, role)

    def post(self, payload) -> Dict:
        """
        Post Report Approvals
        :param payload: List of Objects containing Report ID
        :return: Report Approval Object
        """
        return self.make_post_request(
            api_url=ReportApprovals.POST_REPORT_APPROVALS,
            payload=payload
        )
