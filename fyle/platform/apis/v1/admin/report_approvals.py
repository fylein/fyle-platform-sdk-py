"""
V1 Admin Report Approvals
"""

from ....internals.post_resources import PostResources
from ....internals.list_resources import ListResources


class ReportApprovals(PostResources, ListResources):
    """Class for Report Approvals APIs."""

    REPORT_APPROVALS = '/report_approvals'

    def __init__(self, version, role):
        super().__init__(version, role, ReportApprovals.REPORT_APPROVALS)
