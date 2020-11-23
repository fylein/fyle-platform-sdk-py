"""
V1 Admin Employees
"""

from ...api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    def __init__(self, version, role):
        super().__init__(version, role)
