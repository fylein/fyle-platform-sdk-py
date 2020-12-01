"""
V1 Admin Settlements
"""

from typing import Dict

from ....internals.list_resources import ListResources


class Settlements(ListResources):
    """Class for Settlements APIs."""

    SETTLEMENTS = '/settlements'

    def __init__(self, version, role):
        super().__init__(version, role, Settlements.SETTLEMENTS)
