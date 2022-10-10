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
  mock_data.orgs.list_all.return_value = mock_data_dict['get_orgs']
  mock_data.orgs.list.return_value = mock_data_dict['get_orgs']

  return mock_data


def get_mock_data():
  return get_mock_data_from_file('fixtures/mock_accountant_data.json')
