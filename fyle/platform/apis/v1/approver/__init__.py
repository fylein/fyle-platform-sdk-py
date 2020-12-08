"""
	Initializing Approver API's
"""

from .report_approvals import ReportApprovals
from .reports import Reports

from ..version import version

role = 'approver'

report_approvals = ReportApprovals(version, role)
reports = Reports(version, role)