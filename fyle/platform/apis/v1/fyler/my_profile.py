"""
V1 Fyler My Profile
"""

from ....internals.get_resources import GetResources


class MyProfile(GetResources):
    """Class for My Profile API."""

    MY_PROFILE = '/my_profile'

    def __init__(self, version, role):
        super().__init__(version, role, MyProfile.MY_PROFILE)