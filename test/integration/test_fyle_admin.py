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


  assert dict_compare_keys(categories[0], mock_categories[0]) == [], 'fyle.v1beta.admin.categories.list_all() has stuff that mock_data doesnt'
  assert dict_compare_keys(mock_categories[0], categories[0]) == [], 'mock_data.categories.get() has stuff that fyle doesnt'


def test_post_categories(fyle, mock_data):
  add_category = fyle.v1beta.admin.categories.post(payload = {
    "data": {
      "name": "Engine samp11",
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
  print(add_category)

  assert dict_compare_keys(add_category["data"], mock_categories[0]) == [], 'fyle.v1beta.admin.categories.list_all() has stuff that mock_data doesnt'
  assert dict_compare_keys(mock_categories[0], add_category["data"]) == [], 'mock_data.categories.get() has stuff that fyle doesnt'