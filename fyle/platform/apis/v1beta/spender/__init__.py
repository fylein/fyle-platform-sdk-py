"""
    Initializing Spender API's
"""
from .accounts import Accounts
from .my_profile import MyProfile
from .cost_centers import CostCenters
from .projects import Projects
from .categories import Categories
from .expense_fields import ExpenseFields
from .expenses import Expenses
from .reports import Reports
from .merchants import Merchants
from .employees import Employees
from .tax_groups import TaxGroups
from .files import Files
from ..version import version

role = 'spender'

my_profile = MyProfile(version, role)
accounts = Accounts(version, role)
cost_centers = CostCenters(version, role)
categories = Categories(version, role)
projects = Projects(version, role)
expense_fields = ExpenseFields(version, role)
expenses = Expenses(version, role)
reports = Reports(version, role)
merchants = Merchants(version, role)
employees = Employees(version, role)
tax_groups = TaxGroups(version, role)
files = Files(version, role)
