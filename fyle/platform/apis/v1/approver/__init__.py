"""
    Initializing Approver API's
"""

from .reports import Reports
from .projects import Projects
from .categories import Categories
from .expenses import Expenses
from ..version import version

role = 'approver'

reports = Reports(version, role)
projects = Projects(version, role)
categories = Categories(version, role)
expenses = Expenses(version, role)
