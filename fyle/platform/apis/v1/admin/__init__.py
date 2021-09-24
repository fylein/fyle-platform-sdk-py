"""
    Initializing Admin API's
"""

from .categories import Categories
from .cost_centers import CostCenters
from .employees import Employees
from .expenses import Expenses
from .tax_groups import TaxGroups
from .reimbursements import Reimbursements
from .settlements import Settlements
from .projects import Projects
from .advance_requests import AdvanceRequests
from .files import Files
from .accounting_exports import AccountingExports
from ..version import version

role = 'admin'

categories = Categories(version, role)
cost_centers = CostCenters(version, role)
employees = Employees(version, role)
projects = Projects(version, role)
expenses = Expenses(version, role)
tax_groups = TaxGroups(version, role)
reimbursements = Reimbursements(version, role)
settlements = Settlements(version, role)
advance_requests = AdvanceRequests(version, role)
files = Files(version, role)
accounting_exports = AccountingExports(version, role)
