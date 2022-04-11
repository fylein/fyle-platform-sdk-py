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
  mock_data.profile.get.return_value = mock_data_dict['profile']
  mock_data.files_create.get.return_value = mock_data_dict['files_create']
  mock_data.file_generate_url.get.return_value = mock_data_dict['file_generate_url']
  mock_data.attach_receipt.get.return_value = mock_data_dict['attach_receipt']
  mock_data.create_expense.get.return_value = mock_data_dict['create_expense']

  return mock_data


def get_mock_data():
  return get_mock_data_from_file('fixtures/mock_spender_data.json')