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
