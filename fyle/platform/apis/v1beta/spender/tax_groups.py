"""
V1 Beta Spender Tax Groups
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class TaxGroups(ListResources, ListAllResources):
    """Class for Tax Group APIs."""

    TAX_GROUPS = '/tax_groups'

    def __init__(self, version, role):
        super().__init__(version, role, TaxGroups.TAX_GROUPS)
