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


def test_get_reports(fyle, admin_schema):
    """
    Test Fyle reports get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    reports = fyle.v1.admin.reports.list()
    url = reports.get('url')

    reports_schema = admin_schema[url]['get']['responses']['200']
    jsonschema.validate(instance=reports, schema=reports_schema)


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
