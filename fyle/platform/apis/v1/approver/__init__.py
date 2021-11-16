"""
    Initializing Approver API's
"""

from .reports import Reports
from .projects import Projects
from ..version import version

role = 'approver'

reports = Reports(version, role)
projects = Projects(version, role)
