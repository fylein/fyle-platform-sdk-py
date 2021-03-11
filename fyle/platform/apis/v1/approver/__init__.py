"""
    Initializing Approver API's
"""

from .reports import Reports
from ..version import version

role = 'approver'

reports = Reports(version, role)
