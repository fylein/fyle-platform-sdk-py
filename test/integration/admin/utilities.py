import json
from os import path
from unittest.mock import Mock

def get_mock_data_dict(filename):
  basepath = path.dirname(__file__)
  filepath = path.join(basepath, filename)
  mock_data_json = open(filepath, 'r').read()
  mock_data_dict = json.loads(mock_data_json)
  return mock_data_dict


def get_mock_data_from_file(filename):
  mock_data_dict = get_mock_data_dict(filename)
  mock_data = Mock()
  mock_data.created_accounting_export.get.return_value = mock_data_dict['created_accounting_export']
  mock_data.accounting_export.get.return_value = mock_data_dict['accounting_export']
  mock_data.accounting_export_lineitems.get.return_value = mock_data_dict['accounting_export_lineitems']
  mock_data.categories.get.return_value = mock_data_dict['categories']
  mock_data.employees.get.return_value = mock_data_dict['employees']
  mock_data.files_create.get.return_value = mock_data_dict['file_create']
  mock_data.file_generate_url.get.return_value = mock_data_dict['file_generate_url']
  mock_data.tax_groups.get.return_value = mock_data_dict['tax_groups']
  mock_data.departments.get.return_value = mock_data_dict['departments']

  return mock_data


def get_mock_data():
  return get_mock_data_from_file('fixtures/mock_admin_data.json')