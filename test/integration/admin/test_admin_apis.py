import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)


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
      "name": "Engine samp122",
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
    assert dict_compare_keys(employees_generator[0], mock_employees[0]) == [], 'fyle.v1beta.admin.employees.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_employees[0], employees_generator[0]) == [], 'mock_data.employees.get() has stuff that fyle doesnt'