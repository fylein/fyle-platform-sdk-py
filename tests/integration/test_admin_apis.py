import logging

import jsonschema
import pytest

logger = logging.getLogger(__name__)


def test_get_employees(fyle, admin_schema):
    """
    Test Fyle employees get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    print(fyle.v1.admin.employees)
    employees = fyle.v1.admin.employees.list()
    url = employees.get('url')

    employees_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=employees, schema=employees_schema)


@pytest.mark.xfail
def test_get_employees_invalid(fyle, admin_schema):
    """
    Test Fyle employees get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    employees = fyle.v1.admin.employees.list()
    url = employees.get('url')

    employees_schema = admin_schema[url]['get']['responses']['200']
    employees['data'][0]['mileage_rate_labels'].append('invalid')
    jsonschema.validate(instance=employees, schema=employees_schema)


def test_get_expenses(fyle, admin_schema):
    """
    Test Fyle expenses get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    expenses = fyle.v1.admin.expenses.list()
    url = expenses.get('url')
    print(expenses)

    expenses_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=expenses, schema=expenses_schema)


def test_get_reports(fyle, admin_schema):
    """
    Test Fyle reports get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    reports = fyle.v1.admin.reports.list()
    url = reports.get('url')
    print(reports)

    reports_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=reports, schema=reports_schema)


def test_get_balance_transfers(fyle, admin_schema):
    """
    Test Fyle balance_transfers get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    balance_transfers = fyle.v1.admin.balance_transfers.list()
    url = balance_transfers.get('url')

    balance_transfers_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=balance_transfers, schema=balance_transfers_schema)


def test_get_advance_requests(fyle, admin_schema):
    """
    Test Fyle advance requests get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    advance_requests = fyle.v1.admin.advance_requests.list()
    url = advance_requests.get('url')

    advance_requests_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=advance_requests, schema=advance_requests_schema)


def test_get_advances(fyle, admin_schema):
    """
    Test Fyle advances get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    advances = fyle.v1.admin.advances.list()
    url = advances.get('url')

    advances_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=advances, schema=advances_schema)


def test_get_categories(fyle, admin_schema):
    """
    Test Fyle categories get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    categories = fyle.v1.admin.categories.list()
    url = categories.get('url')

    categories_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=categories, schema=categories_schema)


def test_get_cost_centers(fyle, admin_schema):
    """
    Test Fyle categories get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    cost_centers = fyle.v1.admin.cost_centers.list()
    url = cost_centers.get('url')

    cost_centers_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=cost_centers, schema=cost_centers_schema)


def test_get_projects(fyle, admin_schema):
    """
    Test Fyle projects get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    projects = fyle.v1.admin.projects.list()
    url = projects.get('url')

    projects_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=projects, schema=projects_schema)
