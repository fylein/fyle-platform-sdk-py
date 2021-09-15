"""
    Initializing Fyler API's
"""

from .my_profile import MyProfile
from .cost_centers import CostCenters
from .projects import Projects
from .categories import Categories
from .expense_fields import ExpenseFields
from ..version import version

role = 'fyler'

my_profile = MyProfile(version, role)
cost_centers = CostCenters(version, role)
categories = Categories(version, role)
projects = Projects(version, role)
expense_fields = ExpenseFields(version, role)
