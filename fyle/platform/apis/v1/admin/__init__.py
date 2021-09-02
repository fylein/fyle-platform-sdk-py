"""
    Initializing Admin API's
"""

from .categories import Categories
from .cost_centers import CostCenters
from .employees import Employees
from .expenses import Expenses
from .tax_groups import TaxGroups
from .invitations import Invitations
from .projects import Projects
from ..version import version

role = 'admin'

categories = Categories(version, role)
cost_centers = CostCenters(version, role)
employees = Employees(version, role)
projects = Projects(version, role)
invitations = Invitations(version, role)
expenses = Expenses(version, role)
tax_groups = TaxGroups(version, role)