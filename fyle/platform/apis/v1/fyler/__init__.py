"""
    Initializing Fyler API's
"""

from .my_profile import MyProfile
from .subscriptions import Subscriptions
from ..version import version

role = 'fyler'

my_profile = MyProfile(version, role)
subscriptions = Subscriptions(version, role)
