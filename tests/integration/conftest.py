import os

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


def get_mock_server_url(module):
    server_url = None
    if module == 'integration.test_admin_apis':
        server_url = os.getenv('ADMIN_APIS_URL')
    elif module == 'integration.test_approver_apis':
        server_url = os.getenv('APPROVER_APIS_URL')
    elif module == 'integration.test_fyler_apis':
        server_url = os.getenv('FYLER_APIS_URL')
    elif module == 'integration.test_common_apis':
        server_url = os.getenv('COMMON_APIS_URL')
    print(server_url)
    return server_url


@pytest.fixture(scope='module')
def fyle(request):
    is_mock_server = os.getenv('IS_MOCK_SERVER', 'F')
    if is_mock_server == 'T':
        server_url = get_mock_server_url(request.module.__name__)
    else:
        server_url = os.getenv('SERVER_URL')
    return fyle_connect(server_url)
