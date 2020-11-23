"""
	Intializing Admin API's
"""

from .advance_requests import AdvanceRequests
from .advances import Advances
from .balance_transfers import BalanceTransfers
from .categories import Categories
from .cost_centers import CostCenters
from .employees import Employees
from .expense_custom_properties import ExpenseCustomProperties
from .expenses import Expenses
from .projects import Projects
from .refunds import Refunds
from .reimbursements import Reimbursements
from .reports import Reports
from .settlements import Settlements

from ..version import version

role = 'admin'

advance_requests = AdvanceRequests(version, role)
advances = Advances(version, role)
balance_transfers = BalanceTransfers(version, role)
categories = Categories(version, role)
cost_centers = CostCenters(version, role)
employees = Employees(version, role)
expense_custom_properties = ExpenseCustomProperties(version, role)
expenses = Expenses(version, role)
projects = Projects(version, role)
refunds = Refunds(version, role)
reimbursements = Reimbursements(version, role)
reports = Reports(version, role)
settlements = Settlements(version, role)
