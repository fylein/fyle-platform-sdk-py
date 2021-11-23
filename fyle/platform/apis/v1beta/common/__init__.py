"""
    Initializing Common APIs
"""

from .currencies import Currencies
from .currencies import CurrenciesExchangeRate
from .expense_extract import ExpenseExtract
from .places import Places, PlacesAutocomplete
from ..version import version


role = 'common'

places_autocomplete = PlacesAutocomplete(version, role)
places = Places(version, role)
currencies = Currencies(version, role)
currencies_exchange_rate = CurrenciesExchangeRate(version, role)
expense_extract = ExpenseExtract(version, role)