"""
V1 Admin Employees
"""

from typing import Dict

from .role import role
from ..version import version
from ...api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    GET_EMPLOYEES = '/employees'

    def __init__(self):
        super().__init__(version, role)

    def get(self, created_at=None, updated_at=None, email=None, limit=None, offset=None, order=None, **kwargs) -> Dict:
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
            api_url=Employees.GET_EMPLOYEES,
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
