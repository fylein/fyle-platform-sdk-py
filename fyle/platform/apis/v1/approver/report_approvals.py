"""
V1 Approver Report Approvals
"""

from ....internals.post_resources import PostResources


class ReportApprovals(PostResources):
    """Class for Report Approvals APIs."""

    REPORT_APPROVALS = '/report_approvals'

    def __init__(self, version, role):
        super().__init__(version, role, ReportApprovals.REPORT_APPROVALS)
