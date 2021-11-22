"""
V1 Beta Spender Cost Centers
"""
from ....internals.list_all_resources import ListAllResources
from ....internals.list_resources import ListResources


class CostCenters(ListResources, ListAllResources):
    """Class for Cost Center APIs."""

    COST_CENTERS = '/cost_centers'

    def __init__(self, version, role):
        super().__init__(version, role, CostCenters.COST_CENTERS)
