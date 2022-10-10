"""
V1 Beta Accountant Orgs
"""

from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources


class Orgs(ListResources, ListAllResources):
    """Class for Orgs APIs."""

    ORGS = "/orgs"

    def __init__(self, version, role):
        super().__init__(version, role, Orgs.ORGS)
