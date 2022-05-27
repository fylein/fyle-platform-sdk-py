import base64
from distutils.ccompiler import gen_lib_options
import logging
from os import path
from test.common.utilities import dict_compare_keys, get_sample_file_path

logger = logging.getLogger(__name__)
upload_url = ''
file_id = ''
expense_id = ''

def test_get_profile(fyle, mock_data):
  profile = fyle.v1beta.spender.my_profile.get()
  mock_profile = mock_data.profile.get()

  if profile:
    assert dict_compare_keys(profile["data"], mock_profile) == [], 'fyle.v1beta.spender.profile.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_profile, profile["data"]) == [], 'mock_data.profile.get() has stuff that fyle doesnt'


def test_get_by_id_profile(fyle, mock_data):
  try:
    profile = fyle.v1beta.spender.my_profile.get_by_id(id_="123456")
  except:
    logger.error("Api Not implemented")  


def test_create_file(fyle, mock_data):
  create_file = fyle.v1beta.spender.files.create_file(payload = {
    "data": {
      "name": "sample.jpg",
      "type": "RECEIPT",
      "user_id": "usqywo0f3nBY"
    }
  })
  mock_files = mock_data.files_create.get()
  if create_file["data"]: 
    global file_id
    file_id = create_file["data"]["id"]
    assert dict_compare_keys(create_file["data"], mock_files) == [], 'response from fyle.v1beta.spender.files.create_file() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files, create_file["data"]) == [], 'mock_data.files_create.get() has stuff that fyle doesnt'


def test_generate_file_urls(fyle, mock_data):
  generate_file_urls = fyle.v1beta.spender.files.generate_file_urls(payload = {
    "data": {
        "id": file_id
      }
  })
  mock_files = mock_data.file_generate_url.get()
  if generate_file_urls["data"]:
    global upload_url
    upload_url = generate_file_urls["data"]["upload_url"]
    assert dict_compare_keys(generate_file_urls["data"], mock_files) == [], 'response from fyle.v1beta.spender.files.create_file() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files, generate_file_urls["data"]) == [], 'mock_data.file_generate_url.get() has stuff that fyle doesnt'

def test_put_file_to_url(fyle):
  basepath = get_sample_file_path()
  file_path = path.join(basepath, 'sample.jpg')
  with open(file_path, "rb") as image_file:
    file_data = base64.b64encode(image_file.read())

  put_file_to_url = fyle.v1beta.spender.files.put_file_to_url(
    content_type="image/jpeg", url=upload_url,
    data=file_data
  )
  assert put_file_to_url == True


def test_put_file_to_url_invalid_file(fyle):
  basepath = get_sample_file_path()
  file_path = path.join(basepath, 'uber_expenses_2.txt')
  file_data = open(file_path, 'rb')

  try:
    put_file_to_url = fyle.v1beta.spender.files.put_file_to_url(
      content_type="image/jpeg", url=upload_url,
      data=file_data
    )
  except:
    logger.error("Api did not return a response")
  

def test_create_expense(fyle, mock_data):
  create_expense = fyle.v1beta.spender.expenses.create_expense(payload = {
    "data": {
      "spent_at": "2020-06-01T01:18:19.292-08:00",
      "claim_amount": "100",
      "user_id": "usqywo0f3nBY"
    }
  })
  mock_files = mock_data.create_expense.get()
  if create_expense["data"]:
    global expense_id
    expense_id = create_expense["data"]["id"]
    print(create_expense["data"])
    assert dict_compare_keys(create_expense["data"], mock_files) == [], 'response from fyle.v1beta.spender.expenses.create_expense() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files, create_expense["data"]) == [], 'mock_data.create_expense.get() has stuff that fyle doesnt'


def test_attach_receipt(fyle, mock_data):
  attach_receipt = fyle.v1beta.spender.expenses.attach_receipt(payload = {
    "data": {
      "id": expense_id,
      "file_id": file_id
    }
  })
  mock_files = mock_data.attach_receipt.get()

  if attach_receipt["data"]:
    assert dict_compare_keys(attach_receipt["data"], mock_files) == [], 'response from fyle.v1beta.spender.expenses.attach_receipt() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files, attach_receipt["data"]) == [], 'mock_data.attach_receipt.get() has stuff that fyle doesnt'
