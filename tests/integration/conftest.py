import pytest

from tests.common import fyle_connect, get_admin_schema, get_approver_schema, get_common_schema, get_fyler_schema


@pytest.fixture
def admin_schema():
    return get_admin_schema()


@pytest.fixture
def fyler_schema():
    return get_fyler_schema()


@pytest.fixture
def approver_schema():
    return get_approver_schema()


@pytest.fixture
def common_schema():
    return get_common_schema()


@pytest.fixture(scope='module')
def fyle():
    return fyle_connect()
