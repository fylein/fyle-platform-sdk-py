"""
    Initializing Common APIs
"""

from .currencies import Currencies
from .expense_extract import ExpenseExtract
from ..version import version


role = 'common'

currencies = Currencies(version, role)
expense_extract = ExpenseExtract(version, role)
