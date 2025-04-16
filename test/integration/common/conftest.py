import logging
import pytest

from test.common.utilities import fyle_connect
from test.integration.common.utilities import get_mock_data
logger = logging.getLogger(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def mock_data():
  return get_mock_data()

@pytest.fixture(scope='module')
def fyle():
  return fyle_connect()
  