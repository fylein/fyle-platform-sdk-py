import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

def test_list_currencies(fyle, mock_data):
  list_currencies = fyle.v1beta.common.currencies.list()
  mock_currencies = mock_data.currencies.get()

  if list_currencies["data"]:
    assert dict_compare_keys(list_currencies["data"], mock_currencies) == [], 'response from fyle.v1beta.common.currencies.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_currencies, list_currencies["data"]) == [], 'mock_data.currencies.get() has stuff that fyle doesnt'


def test_get_exchange_rate(fyle, mock_data):
  exchange_rate = fyle.v1beta.common.currencies.CurrenciesExchangeRate.get(from_="INR", to_="USD", date="2021-11-18")
  mock_currencies = mock_data.currencies.get()

  if exchange_rate["data"]:
    assert dict_compare_keys(exchange_rate["data"], mock_currencies) == [], 'response from fyle.v1beta.common.currencies.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_currencies, exchange_rate["data"]) == [], 'mock_data.currencies.get() has stuff that fyle doesnt'

