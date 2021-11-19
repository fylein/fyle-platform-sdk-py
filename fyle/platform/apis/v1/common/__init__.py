"""
    Initializing Common APIs
"""

from .currencies import Currencies
from .places import Places
from .expense_extract import ExpenseExtract
from ..version import version


role = 'common'

places = Places(version, role)
currencies = Currencies(version, role)
expense_extract = ExpenseExtract(version, role)
