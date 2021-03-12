"""
V1 Fyler Employees
"""

from ....internals.get_resources import GetResources


class MyProfile(GetResources):
    """Class for Employee Profile API."""

    MY_PROFILE = '/my_profile'

    def __init__(self, version, role):
        super().__init__(version, role, MyProfile.MY_PROFILE)