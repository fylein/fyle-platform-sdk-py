"""
    Initializing Common APIs
"""

from .currencies import Currencies
from ..version import version

role = 'common'

currencies = Currencies(version, role)
