"""
	Intializing Admin API's
"""

from .advance_requests_stats import AdvanceRequestsStats
from .advance_requests import AdvanceRequests
from .advances import Advances
from .balance_transfers import BalanceTransfers
from .categories import Categories
from .cost_centers import CostCenters
from .employees import Employees
from .expense_comments import ExpenseComments
from .expense_fields import ExpenseFields
from .expense_stats import ExpenseStats
from .expenses import Expenses
from .policy import Policy
from .projects import Projects
from .refunds import Refunds
from .reimbursements import Reimbursements
from .report_stats import ReportStats
from .reports import Reports
from .report_approvals import ReportApprovals
from .settlements import Settlements
from .trip_requests_stats import TripRequestsStats

from ..version import version

role = 'admin'

advance_requests_stats = AdvanceRequestsStats(version, role)
advance_requests = AdvanceRequests(version, role)
advances = Advances(version, role)
balance_transfers = BalanceTransfers(version, role)
categories = Categories(version, role)
cost_centers = CostCenters(version, role)
employees = Employees(version, role)
expense_comments = ExpenseComments(version, role)
expense_fields = ExpenseFields(version, role)
expense_stats = ExpenseStats(version, role)
expenses = Expenses(version, role)
policy = Policy(version, role)
projects = Projects(version, role)
refunds = Refunds(version, role)
reimbursements = Reimbursements(version, role)
report_stats = ReportStats(version, role)
reports = Reports(version, role)
report_approvals = ReportApprovals(version, role)
settlements = Settlements(version, role)
trip_requests_stats = TripRequestsStats(version, role)