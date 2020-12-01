"""
V1 Common Places
"""

from ....internals.get_resources import GetResources
from ....internals.list_resources import ListResources


class Places(ListResources, GetResources):
    """Class for Places APIs."""

    PLACES = '/places'

    def __init__(self, version, role):
        super().__init__(version, role, Places.PLACES)
