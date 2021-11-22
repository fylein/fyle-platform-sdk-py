"""
    Initializing Common APIs
"""

from .currencies import Currencies
from .currencies import CurrenciesExchangeRate
from .expense_extract import ExpenseExtract
from ..version import version


role = 'common'

currencies = Currencies(version, role)
currencies_exchange_rate = CurrenciesExchangeRate(version, role)
expense_extract = ExpenseExtract(version, role)