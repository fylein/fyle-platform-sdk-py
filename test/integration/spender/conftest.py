import logging
import pytest

from test.common.utilities import fyle_connect
from test.integration.spender.utilities import get_mock_data
logger = logging.getLogger(__name__)


@pytest.fixture
def mock_data():
  return get_mock_data()

@pytest.fixture(scope='module')
def fyle():
  return fyle_connect()