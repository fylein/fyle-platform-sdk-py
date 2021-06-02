"""
    Initializing Approver API's
"""

from .reports import Reports
from .subscriptions import Subscriptions
from ..version import version

role = 'approver'

reports = Reports(version, role)
subscriptions = Subscriptions(version, role)
