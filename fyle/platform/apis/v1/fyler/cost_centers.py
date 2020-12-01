"""
V1 Fyler Cost Center
"""

from typing import Dict

from ....internals.list_resources import ListResources
from ....internals.get_resources import GetResources


class CostCenters(ListResources, GetResources):
    """Class for Cost Center APIs."""

    COST_CENTERS = '/cost_centers'

    def __init__(self, version, role):
        super().__init__(version, role, CostCenters.COST_CENTERS)