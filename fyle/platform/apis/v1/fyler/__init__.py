"""
    Initializing Fyler API's
"""

from .my_profile import MyProfile
from ..version import version

role = 'fyler'

my_profile = MyProfile(version, role)
