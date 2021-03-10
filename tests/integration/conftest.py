import pytest

from tests.common import fyle_connect


@pytest.fixture(scope='module')
def fyle():
    return fyle_connect()
