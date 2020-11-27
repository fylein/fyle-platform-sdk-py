"""
	Initializing Fyler API's
"""

from .advance_requests_stats import AdvanceRequestsStats
from .categories import Categories
from .cost_centers import CostCenters
from .currencies import Currencies
from .employees import Employees
from .exchange_rate import ExchangeRate
from .expense_comments import ExpenseComments
from .expense_custom_properties import ExpenseCustomProperties
from .expense_stats import ExpenseStats
from .expenses import Expenses
from .policy import Policy
from .projects import Projects
from .report_stats import ReportStats
from .reports import Reports
from .trip_requests_stats import TripRequestsStats
from .vendors import Vendors

from ..version import version

role = 'fyler'

advance_requests_stats = AdvanceRequestsStats(version, role)
categories = Categories(version, role)
cost_centers = CostCenters(version, role)
currencies = Currencies(version, role)
# employees = Employees(version, role)
exchange_rate = ExchangeRate(version, role)
expense_comments = ExpenseComments(version, role)
expense_custom_properties = ExpenseCustomProperties(version, role)
expense_stats = ExpenseStats(version, role)
expenses = Expenses(version, role)
policy = Policy(version, role)
projects = Projects(version, role)
report_stats = ReportStats(version, role)
reports = Reports(version, role)
trip_requests_stats = TripRequestsStats(version, role)
vendors = Vendors(version, role)
