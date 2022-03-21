import string
import random
import logging
from os import path
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

random_name = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 10))
upload_url = ''
account_export_id = ''

def test_get_accounting_exports(fyle, mock_data):
  """
  Test Fyle admin accounting exports Object
  :param fyle: fyle sdk instance
  :param mock_data: mock instance
  :return: None
  """
  # Get a list of all Admin Accounting_exports in a paginated manner and add to a list
  accounting_export = []
  query_params = {
    'order': 'created_at.desc'
  }

  accounting_exports_generator = fyle.v1beta.admin.accounting_exports.list_all(query_params=query_params)
  mock_accounting_exports = mock_data.accounting_export.get()

  for response in accounting_exports_generator:
    if response.get('data'):
      accounting_export.extend(response['data'])

  if accounting_export:
    assert dict_compare_keys(accounting_export[0], mock_accounting_exports[0]) == [], 'fyle.v1beta.admin.accounting_exports.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_accounting_exports[0], accounting_export[0]) == [], 'mock_data.accounting_export.get() has stuff that fyle doesnt'


def test_create_accounting_exports(fyle, mock_data):
  create_accounting_exports = fyle.v1beta.admin.accounting_exports.create_accounting_exports(payload={
    "data": {
      "file_ids": [
        "fiFqjxHuSwX5"
      ],
      "exported_at": "2020-06-01T13:14:54.804+00:00",
      "name": "Accounting exports tests",
      "description": "Win the trophy",
    }
  })
  mock_accounting_exports = mock_data.accounting_export.get()

  if create_accounting_exports["data"]:
    global account_export_id
    account_export_id = create_accounting_exports["data"]["id"]
    assert dict_compare_keys(create_accounting_exports["data"], mock_accounting_exports[0]) == [], 'response from fyle.v1beta.admin.accounting_export.create_accounting_exports() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_accounting_exports[0], create_accounting_exports["data"]) == [], 'mock_data.accounting_export.get() has stuff that fyle doesnt'


def test_create_accounting_export_lineitems(fyle, mock_data):
  create_accounting_export_lineitems = fyle.v1beta.admin.accounting_exports.create_accounting_export_lineitems(payload={
    "data": {
      "object_id": "sdfd2391",
      "object_type": "REIMBURSEMENT",
      "reference": "string",
      "accounting_export_id": account_export_id
    }
  })
  mock_accounting_exports_lineitems = mock_data.accounting_export.get()

  if create_accounting_export_lineitems["data"]:
    assert dict_compare_keys(create_accounting_export_lineitems["data"], mock_accounting_exports_lineitems[0]) == [], 'response from fyle.v1beta.admin.accounting_export.create_accounting_export_lineitems() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_accounting_exports_lineitems[0], create_accounting_export_lineitems["data"]) == [], 'mock_data.accounting_export.get() has stuff that fyle doesnt'


def test_bulk_create_accounting_export_lineitems(fyle, mock_data):
  create_accounting_exports = fyle.v1beta.admin.accounting_exports.create_accounting_exports(payload={
    "data": {
      "file_ids": [
        "fiFqjxHuSwX5"
      ],
      "exported_at": "2020-06-01T13:14:54.804+00:00",
      "name": "Accounting exports tests",
      "description": "Win the trophy",
    }
  })
  try:
    bulk_create_accounting_export_lineitems = fyle.v1beta.admin.accounting_exports.bulk_create_accounting_export_lineitems(payload={
      "data": [
        {
          "object_id": "sdfd2391",
          "object_type": "ADVANCE_REQUEST",
          "reference": "string",
          "accounting_export_id": create_accounting_exports["data"]["id"]
        }
      ]
    })
  except:
    logger.error("error in api call")


def test_get_categories(fyle, mock_data):
  """
  Test Fyle category Object
  :param fyle: fyle sdk instance
  :param mock_data: mock instance
  :return: None
  """
  # Get a list of all Categories in a paginated manner and add to a list
  categories = []
  query_params = {
    'order': 'created_at.desc'
  }

  categories_generator = fyle.v1beta.admin.categories.list_all(query_params=query_params)
  mock_categories = mock_data.categories.get()

  for response in categories_generator:
    if response.get('data'):
      categories.extend(response['data'])

  if categories:
    assert dict_compare_keys(categories[0], mock_categories[0]) == [], 'fyle.v1beta.admin.categories.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_categories[0], categories[0]) == [], 'mock_data.categories.get() has stuff that fyle doesnt'


def test_post_categories(fyle, mock_data):
  add_category = fyle.v1beta.admin.categories.post(payload = {
    "data": {
      "name": random_name,
      "sub_category": "Turbo charged",
      "is_enabled": True,
      "system_category": "Others",
      "code": "C1234",
      "restricted_project_ids": [
        247690, 247593
      ]
    }
  })
  mock_categories = mock_data.categories.get()

  if add_category["data"]:
    assert dict_compare_keys(add_category["data"], mock_categories[0]) == [], 'response from fyle.v1beta.admin.categories.post() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_categories[0], add_category["data"]) == [], 'mock_data.categories.get() has stuff that fyle doesnt'


def test_list_employees(fyle, mock_data):
  employees = []
  query_params = {
    'order': 'created_at.desc'
  }

  employees_generator = fyle.v1beta.admin.employees.list_all(query_params=query_params)
  mock_employees = mock_data.employees.get()

  for response in employees_generator:
    if response.get('data'):
      employees.extend(response['data'])

  if employees:
    assert dict_compare_keys(employees[0], mock_employees[0]) == [], 'fyle.v1beta.admin.employees.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_employees[0], employees[0]) == [], 'mock_data.employees.get() has stuff that fyle doesnt'


def test_bulk_upload_employees(fyle, mock_data):
  employees_generator = fyle.v1beta.admin.employees.invite_bulk(payload = {
    "data": [{
      "user_email": "mikasa@fyle.in",
      "user_full_name": "mikasa",
      "business_unit": "Finance ops",
      "code": "E84122",
      "department_name": "",
      "sub_department": "",
      "is_enabled": True,
      "joined_at": "2020-06-01T01:18:19.292-08:00",
      "level": "",
      "location": "",
      "title": "",
      "custom_fields": [],
      "approver_emails": [],
      "project_names": [],
      "cost_center_names": [],
      "per_diem_rate_names": [],
      "vehicle_types": []
    }]
  })

  mock_employees = mock_data.employees.get()

  if employees_generator:
    assert dict_compare_keys(employees_generator[0], mock_employees[0]) == [], 'fyle.v1beta.admin.employees.invite_bulk() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_employees[0], employees_generator[0]) == [], 'mock_data.employees.get() has stuff that fyle doesnt'


def test_create_file(fyle, mock_data):
  create_fyle = fyle.v1beta.admin.files.create_file(payload = {
    "data": {
      "name": "uber_expenses_2.pdf",
      "type": "RECEIPT",
      "user_id": "usqywo0f3nBY"
    }
  })
  mock_files = mock_data.files_create.get()

  if create_fyle["data"]:
    assert dict_compare_keys(create_fyle["data"], mock_files[0]) == [], 'response from fyle.v1beta.admin.files.create_file() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files[0], create_fyle["data"]) == [], 'mock_data.files_create.get() has stuff that fyle doesnt'


def test_bulk_generate_file_urls(fyle, mock_data):
  bulk_generate_file = fyle.v1beta.admin.files.bulk_generate_file_urls(payload = {
    "data": [
      {
        "id": "fihHuRIiQ9XE"
      },
      {
        "id": "fiGfMnIHDK2L"
      }
    ]
  })
  mock_files = mock_data.file_generate_url.get()

  if bulk_generate_file["data"]:
    global upload_url
    upload_url = bulk_generate_file["data"][0]["upload_url"]
    assert dict_compare_keys(bulk_generate_file["data"][0], mock_files[0]) == [], 'response from fyle.v1beta.admin.files.create_file() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files[0], bulk_generate_file["data"][0]) == [], 'mock_data.file_generate_url.get() has stuff that fyle doesnt'
  

def test_upload_file_to_aws(fyle, mock_data):
  basepath = path.dirname(__file__)
  file_path = path.join(basepath, 'fixtures/sample_files/uber_expenses_2.txt')
  file_data = open(file_path, 'rb')

  try:
    upload_file_to_aws = fyle.v1beta.admin.files.upload_file_to_aws(
      content_type="text/csv", url=upload_url,
      data=file_data
    )
  except:
    logger.error("Api did not return a response")
  

def test_list_all_tax_groups(fyle, mock_data):
  tax_groups = []
  query_params = {
    'order': 'created_at.desc'
  }

  tax_groups_generator = fyle.v1beta.admin.tax_groups.list_all(query_params=query_params)
  mock_tax_groups = mock_data.tax_groups.get()

  for response in tax_groups_generator:
    if response.get('data'):
      tax_groups.extend(response['data'])

  if tax_groups:
    assert dict_compare_keys(tax_groups[0], mock_tax_groups[0]) == [], 'fyle.v1beta.admin.tax_groups.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_tax_groups[0], tax_groups[0]) == [], 'mock_data.tax_groups.get() has stuff that fyle doesnt'


def test_list_all_tax_groups_offset_limit(fyle, mock_data):
  query_params = {
    'offset': 1,
    'limit': 1
  }
  try:
    tax_groups_generator = fyle.v1beta.admin.tax_groups.list_all(query_params=query_params)
    logger.info(tax_groups_generator)
  except:
    logger.error("Offset and limit should not be passed for list_all")


def test_list_all_tax_groups_missing_order(fyle, mock_data):
  try:
    tax_groups_generator = fyle.v1beta.admin.tax_groups.list_all()
  except:
    logger.error("Mandatory query params order is missing")


def test_list_tax_groups(fyle, mock_data):
  query_params = {
    'offset': 1,
    'limit': 1,
    'order': 'created_at.desc'
  }

  tax_groups_generator = fyle.v1beta.admin.tax_groups.list(query_params=query_params)
  mock_tax_groups = mock_data.tax_groups.get()

  if tax_groups_generator["data"]:
    assert dict_compare_keys(tax_groups_generator["data"][0], mock_tax_groups[0]) == [], 'fyle.v1beta.admin.tax_groups.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_tax_groups[0], tax_groups_generator["data"][0]) == [], 'mock_data.tax_groups.get() has stuff that fyle doesnt'


def test_list_tax_groups_missing_order(fyle, mock_data):
  query_params = {
    'offset': 1,
    'limit': 1
  }
  try:
    tax_groups_generator = fyle.v1beta.admin.tax_groups.list(query_params=query_params)
  except:
    logger.error("Mandatory query params order is missing")


def test_post_bulk_tax_groups(fyle):
  try:
    post_bulk = fyle.v1beta.admin.tax_groups.post_bulk(payload={
      "data": [
        {
          "is_enabled":True,
          "name":random_name,
          "org_id":"or79Cob97KSh",
          "percentage":0.18,
        }
      ]
    })
    logger.info(post_bulk)
  except:
    logger.error("Error while uploading data")


def test_get_by_id_tax_groups(fyle, mock_data):
  get_by_id = fyle.v1beta.admin.tax_groups.get_by_id(id_="tgXueCemFa6Q")
  mock_files = mock_data.tax_groups.get()

  if get_by_id["data"]:
    assert dict_compare_keys(get_by_id["data"], mock_files[0]) == [], 'response from fyle.v1beta.admin.tax_groups.post_bulk() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_files[0], get_by_id["data"]) == [], 'mock_data.tax_groups.get() has stuff that fyle doesnt'


def test_get_by_id_tax_groups_wrong_id(fyle, mock_data):
  try:
    get_by_id = fyle.v1beta.admin.tax_groups.get_by_id(id_="tgXuQ")
  except:
    logger.error("Error in api, should not accept wrong id")
    

def test_get_by_id_tax_groups_empty_id(fyle, mock_data):
  try:
    get_by_id = fyle.v1beta.admin.tax_groups.get_by_id(id_="")
  except:
    logger.error("Empty id is not be accepted by the api")

  
def test_get_by_id_tax_groups_missing_id(fyle, mock_data):
  try:
    get_by_id = fyle.v1beta.admin.tax_groups.get_by_id()
  except:
    logger.error("id is a requied parameter")
