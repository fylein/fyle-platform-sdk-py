"""
V1 Beta Admin Settlements
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class Settlements(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Settlements APIs."""

    SETTLEMENTS = '/settlements'

    def __init__(self, version, role):
        super().__init__(version, role, Settlements.SETTLEMENTS)
