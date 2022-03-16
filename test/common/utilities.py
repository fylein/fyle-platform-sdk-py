import json
import logging
from os import path
from unittest.mock import Mock

from fyle.platform import Platform
logger = logging.getLogger(__name__)


def get_mock_data_dict(filename):
  basepath = path.dirname(__file__)
  filepath = path.join(basepath, filename)
  mock_data_json = open(filepath, 'r').read()
  mock_data_dict = json.loads(mock_data_json)
  return mock_data_dict


def get_mock_data_from_file(filename):
  mock_data_dict = get_mock_data_dict(filename)
  mock_data = Mock()
  mock_data.accounting_export.get.return_value = mock_data_dict['accounting_export']
  mock_data.categories.get.return_value = mock_data_dict['categories']
  mock_data.employees.get.return_value = mock_data_dict['employees']
  return mock_data


def get_mock_data():
  return get_mock_data_from_file('mock_admin_data.json')


def dict_compare_keys(d1, d2, key_path=''):
  """
  Compare two dicts recursively and see if dict1 has any keys that dict2 does not
  Returns: list of key paths
  """
  res = []
  if not d1:
    return res
  if not isinstance(d1, dict):
    return res
  for k in d1:
    if k not in d2:
      missing_key_path = f'{key_path}->{k}'
      res.append(missing_key_path)
    else:
      if isinstance(d1[k], dict):
        key_path1 = f'{key_path}->{k}'
        res1 = dict_compare_keys(d1[k], d2[k], key_path1)
        res = res + res1
      elif isinstance(d1[k], list):
        key_path1 = f'{key_path}->{k}[0]'
        dv1 = d1[k][0] if len(d1[k]) > 0 else None
        dv2 = d2[k][0] if len(d2[k]) > 0 else None
        res1 = dict_compare_keys(dv1, dv2, key_path1)
        res = res + res1
  return res


def fyle_connect():
  """
    FYLE connector
    :param: db connection
  """
  file = open('test_credentials.json', 'r')
  fyle_config = json.load(file)

  connection = Platform(
    server_url=fyle_config['server_url'],
    token_url=fyle_config['token_url'],
    refresh_token=fyle_config['refresh_token'],
    client_id=fyle_config['client_id'],
    client_secret=fyle_config['client_secret']
  )

  with open('test_credentials.json', 'w') as fp:
    json.dump(fyle_config, fp)
  return connection