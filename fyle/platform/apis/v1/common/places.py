"""
V1 Common Places
"""

from typing import Dict

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources


class Places(ListResources, GetResources):
    """Class for Places APIs."""

    PLACES = '/places'

    def __init__(self, version, role):
        super().__init__(version, role, Places.PLACES)
