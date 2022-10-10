import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

def test_list_all_orgs(fyle, mock_data):
  """
  Test Fyle accountant list orgs
  :param fyle: fyle sdk instance
  :param mock_data: mock instance
  :return: None
  """
  # Get a list of all Accountant Orgs in a paginated manner and add to a list
  orgs = []
  query_params = {
    'order': 'created_at.desc'
  }

  orgs_generator = fyle.v1beta.accountant.orgs.list_all(query_params=query_params)
  mock_orgs = mock_data.orgs.list_all()

  for response in orgs_generator:
    if response.get('data'):
      orgs.extend(response['data'])
  if orgs:
    assert dict_compare_keys(orgs[0], mock_orgs[0]) == [], 'fyle.v1beta.accountant.orgs.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_orgs[0], orgs[0]) == [], 'mock_data.orgs.list_all() has stuff that fyle doesnt'

def test_list_orgs(fyle, mock_data):
  query_params = {
    'offset': 1,
    'limit': 1,
    'order': 'created_at.desc'
  }

  orgs = fyle.v1beta.accountant.orgs.list(query_params=query_params)
  mock_orgs = mock_data.orgs.list()

  if orgs["data"]:
    assert dict_compare_keys(orgs["data"][0], mock_orgs[0]) == [], 'fyle.v1beta.accountant.orgs.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_orgs[0], orgs["data"][0]) == [], 'mock_data.orgs.list() has stuff that fyle doesnt'
