import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)

global report_id

def test_list_all_categories(fyle, mock_data):
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

  categories_generator = fyle.v1beta.approver.categories.list_all(query_params=query_params)
  mock_categories = mock_data.categories.get()

  for response in categories_generator:
    if response.get('data'):
      categories.extend(response['data'])

  if categories:
    assert dict_compare_keys(categories[0], mock_categories[0]) == [], 'fyle.v1beta.approver.categories.list_all() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_categories[0], categories[0]) == [], 'mock_data.categories.get() has stuff that fyle doesnt'


def test_list_reports(fyle, mock_data):
  """
  Test Fyle category Object
  :param fyle: fyle sdk instance
  :param mock_data: mock instance
  :return: None
  """
  query_params = {
    'order': 'created_at.desc',
    'limit': 500,
    'offset': 823
  }

  reports_generator = fyle.v1beta.approver.reports.list(query_params=query_params)
  mock_reports = mock_data.reports.get()

  if reports_generator:
    assert dict_compare_keys(reports_generator["data"][0], mock_reports[0]) == [], 'fyle.v1beta.approver.reports.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_reports[0], reports_generator["data"][0]) == [], 'mock_data.reports.get() has stuff that fyle doesnt'


def test_approve_report(fyle, mock_data):
  approve_report = {}
  try:
    approve_report = fyle.v1beta.approver.reports.approve(id_="rpbHgskxt0cD")
    mock_reports = mock_data.reports.get()
  except:
    logger.error("report is not in APPROVER_PENDING state")
  if approve_report:
    assert dict_compare_keys(approve_report["data"], mock_reports[0]) == [], 'fyle.v1beta.approver.reports.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_reports[0], approve_report["data"]) == [], 'mock_data.reports.get() has stuff that fyle doesnt'


def test_get_by_id(fyle, mock_data):
  reports_generator = fyle.v1beta.approver.reports.get_by_id(id_="rp6yFhpzfEhc")
  mock_reports = mock_data.reports.get()

  if reports_generator:
    assert dict_compare_keys(reports_generator["data"], mock_reports[0]) == [], 'fyle.v1beta.approver.reports.list() has stuff that mock_data doesnt'
    assert dict_compare_keys(mock_reports[0], reports_generator["data"]) == [], 'mock_data.reports.get() has stuff that fyle doesnt'
