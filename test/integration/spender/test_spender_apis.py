import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

def test_get_profile(fyle, mock_data):
  profile = fyle.v1beta.spender.my_profile.get()
  mock_profile = mock_data.profile.get()

  if profile:
    assert dict_compare_keys(profile["data"], mock_profile) == [], 'fyle.v1beta.admin.profile.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_profile, profile["data"]) == [], 'mock_data.profile.get() has stuff that fyle doesnt'


def test_get_by_id_profile(fyle, mock_data):
  try:
    profile = fyle.v1beta.spender.my_profile.get_by_id(id_="123456")
  except:
    logger.error("Api Not implemented")  