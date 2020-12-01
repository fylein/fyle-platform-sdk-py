"""
V1 Admin Cost Center
"""

from ....internals.list_resources import ListResources
from ....internals.post_resources import PostResources


class CostCenters(ListResources, PostResources):
    """Class for Cost Center APIs."""

    COST_CENTERS = '/cost_centers'

    def __init__(self, version, role):
        super().__init__(version, role, CostCenters.COST_CENTERS)
