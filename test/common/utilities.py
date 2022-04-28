import json
import os
import logging
from os import path
from unittest.mock import Mock

from fyle.platform import Platform
logger = logging.getLogger(__name__)


def dict_compare_keys(d1, d2, key_path=''):
  """
  Compare two dicts recursively and see if dict1 has any keys that dict2 does not
  Returns: list of key paths
  """
  res = []
  if not d1 or not d2:
    return res
  if not isinstance(d1, dict) or not isinstance(d2, dict):
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
      elif isinstance(d1[k], list) and isinstance(d2[k], list):
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
  connection = Platform(
    server_url=os.environ.get('SERVER_URL'),
    token_url=os.environ.get('TOKEN_URL'),
    refresh_token=os.environ.get('REFRESH_TOKEN'),
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET')
  )
  return connection


def get_sample_file_path():
  basepath = path.dirname(__file__)
  file_path = path.join(basepath, 'fixtures/sample_files/')

  return file_path