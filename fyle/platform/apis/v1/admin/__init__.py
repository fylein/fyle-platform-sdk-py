"""
    Initializing Admin API's
"""
from .reports import Reports
from .categories import Categories
from .cost_centers import CostCenters
from .employees import Employees
from .expenses import Expenses
from .tax_groups import TaxGroups
from .reimbursements import Reimbursements
from .projects import Projects
from .expense_fields import ExpenseFields
from .dependent_expense_field_values import DependentExpenseFieldValues
from .advance_requests import AdvanceRequests
from .files import Files
from .accounting_exports import AccountingExports
from .corporate_cards import CorporateCards
from .corporate_card_transactions import CorporateCardTransactions
from .departments import Departments
from .subscriptions import Subscriptions
from .scheduled_callbacks import ScheduledCallbacks
from .org_settings import OrgSettings
from ..version import version

role = 'admin'

categories = Categories(version, role)
cost_centers = CostCenters(version, role)
employees = Employees(version, role)
projects = Projects(version, role)
expense_fields = ExpenseFields(version, role)
dependent_expense_field_values = DependentExpenseFieldValues(version, role)
expenses = Expenses(version, role)
tax_groups = TaxGroups(version, role)
reimbursements = Reimbursements(version, role)
advance_requests = AdvanceRequests(version, role)
files = Files(version, role)
accounting_exports = AccountingExports(version, role)
corporate_cards = CorporateCards(version, role)
corporate_card_transactions = CorporateCardTransactions(version, role)
departments = Departments(version, role)
subscriptions = Subscriptions(version, role)
scheduled_callbacks = ScheduledCallbacks(version, role)
reports = Reports(version, role)
org_settings = OrgSettings(version, role)
