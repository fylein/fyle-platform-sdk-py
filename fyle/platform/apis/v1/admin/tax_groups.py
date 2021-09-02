"""
V1 Admin Tax Groups
"""

from ....internals.get_resources import GetResources
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class TaxGroups(ListResources, ListAllResources, PostResources, GetResources):
    """Class for Tax Groups APIs."""

    TAX_GROUPS = '/tax_groups'

    def __init__(self, version, role):
        super().__init__(version, role, TaxGroups.TAX_GROUPS)
