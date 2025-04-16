"""
    Initializing Accountant APIs
"""

from .orgs import Orgs
from ..version import version


role = 'accountant'

orgs = Orgs(version, role)
