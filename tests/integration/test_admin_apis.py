import logging

import jsonschema

logger = logging.getLogger(__name__)


def test_get_employees(fyle, admin_schema):
    """
    Test Fyle employees get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    employees = fyle.v1.admin.employees.get()
    url = employees.get('url')

    employees_schema = admin_schema.get(url).get('get').get('responses').get('200')
    jsonschema.validate(instance=employees, schema=employees_schema)


def test_get_employees_invalid(fyle, admin_schema):
    """
    Test Fyle employees get call
    Parameters:
        fyle (obj): Fyle SDK instance
    """
    employees = fyle.v1.admin.employees.get()
    url = employees.get('url')

    employees_schema = admin_schema.get(url).get('get').get('responses').get('200')
    employees['data'][0]['mileage_rate_labels'].append('invalid')
    # try:
    jsonschema.validate(instance=employees, schema=employees_schema)
    # except Exception as e:
    #     assert isinstance(e, jsonschema.exceptions.ValidationError)
