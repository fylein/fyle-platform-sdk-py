"""
V1 Admin Employees
"""

from typing import Dict

from ...api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    LIST_EMPLOYEES = '/employees'
    POST_EMPLOYEES = '/employees'

    def __init__(self, version, role):
        super().__init__(version, role)

    def list(self, created_at=None, updated_at=None, email=None, limit=None,
        offset=None, order=None, **kwargs) -> Dict:
        """
        Get Employees
        :param created_at:
        :param updated_at:
        :param email:
        :param limit: No. of employees to be fetched
        :param offset: Pagination offset
        :param order:
        :return: List of Employee Objects
        """
        return self.make_get_request(
            api_url=Employees.LIST_EMPLOYEES,
            query_params={
                'created_at': created_at,
                'updated_at': updated_at,
                'email': email,
                'limit': limit,
                'offset': offset,
                'order': order,
                **kwargs
            }
        )

    def post(self, payload) -> Dict:
        """
        Creates or updates employee
        :param payload: Employee object
        :return: Employee Object
        """
        return self.make_post_request(
            api_url=Employees.POST_EMPLOYEES,
            payload=payload
        )
