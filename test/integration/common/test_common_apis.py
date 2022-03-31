import base64
import logging
from os import path
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

def test_list_currencies(fyle, mock_data):
  list_currencies = fyle.v1beta.common.currencies.list()
  mock_currencies = mock_data.currencies.get()

  if list_currencies["data"]:
    assert dict_compare_keys(list_currencies["data"], mock_currencies) == [], 'response from fyle.v1beta.common.currencies.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_currencies, list_currencies["data"]) == [], 'mock_data.currencies.get() has stuff that fyle doesnt'


def test_get_exchange_rate(fyle, mock_data):
  exchange_rate = fyle.v1beta.common.currencies_exchange_rate.get(from_="INR", to_="USD", date="2021-11-18")
  mock_exchange_rate = mock_data.exchange_rate.get()

  if exchange_rate["data"]:
    assert dict_compare_keys(exchange_rate["data"], mock_exchange_rate) == [], 'response from fyle.v1beta.common.currencies_exchange_rate.get() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_exchange_rate, exchange_rate["data"]) == [], 'mock_data.exchange_rate.get() has stuff that fyle doesnt'


def test_extract_expense_missing_file_name_b64(fyle, mock_data):
  try:
    extract_expense = fyle.v1beta.common.expense_extract.extract(file_name="", b64_content="")
  except:
    logger.error("File name and cntent is required")


def test_extract_expense_invalid_file_name(fyle, mock_data):
  try:
    extract_expense = fyle.v1beta.common.expense_extract.extract(file_name="sample", b64_content="asdfghj")
  except:
    logger.error("File name is invalid")


def test_list_places_autocomplete(fyle, mock_data):
  places_autocomplete = fyle.v1beta.common.places_autocomplete.list(q="bang", types="(cities)", location="26.595889,85.4891037")
  mock_places_autocomplete = mock_data.places_autocomplete.get()

  if places_autocomplete["data"]:
    assert dict_compare_keys(places_autocomplete["data"][0], mock_places_autocomplete[0]) == [], 'response from fyle.v1beta.common.places_autocomplete.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_places_autocomplete[0], places_autocomplete["data"][0]) == [], 'mock_data.places_autocomplete.get() has stuff that fyle doesnt'


def test_list_places_autocomplete_missing_q(fyle, mock_data):
  try:
    places_autocomplete = fyle.v1beta.common.places_autocomplete.list(q="")
  except:
    logger.error("q is required parameter")

def test_get_by_id_places(fyle, mock_data):
  place_by_id = fyle.v1beta.common.places.get_by_id(id_="ChIJbU60yXAWrjsR4E9-UejD3_g")
  mock_places = mock_data.place_by_id.get()

  if place_by_id:
    assert dict_compare_keys(place_by_id, mock_places[0]) == [], 'response from fyle.v1beta.common.places.get_by_id() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_places[0], place_by_id) == [], 'mock_data.place_by_id.get() has stuff that fyle doesnt'


def test_get_by_id_places_missing_id(fyle, mock_data):
  try:
    place_by_id = fyle.v1beta.common.places.get_by_id(id_="")
  except:
    logger.error("id is required parameter")


def test_get_by_id_places_invalid_id(fyle, mock_data):
  try:
    place_by_id = fyle.v1beta.common.places.get_by_id(id_="123")
  except:
    logger.error("id should be valid")